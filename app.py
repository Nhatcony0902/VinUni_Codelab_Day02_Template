import os
import sys
import json
import streamlit as st

# Configure Streamlit page layout & theme
st.set_page_config(
    page_title="Vin Smart Future — Xanh SM AI Dispatch Co-Pilot",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design Aesthetics
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    .stApp {
        background-color: #0f172a;
    }
    
    .title-card {
        background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%);
        padding: 24px;
        border-radius: 16px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(14, 165, 233, 0.3);
    }
    
    .status-badge-pass {
        background-color: #064e3b;
        color: #34d399;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        border: 1px solid #10b981;
    }
    
    .status-badge-alert {
        background-color: #7f1d1d;
        color: #f87171;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        border: 1px solid #ef4444;
    }

    .output-box {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        font-size: 0.95rem;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# Title Banner
st.markdown("""
<div class="title-card">
    <h1 style="margin:0; font-size: 2.2rem; font-weight: 700;">⚡ Vin Smart Future</h1>
    <p style="margin-top: 8px; opacity: 0.9; font-size: 1.1rem;">
        Xanh SM (GSM) — Intelligent Battery & Emergency Dispatcher Co-Pilot
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar settings
with st.sidebar:
    st.image("https://img.icons8.com/color/96/electric-car.png", width=70)
    st.header("⚙️ Dispatcher Control")
    vehicle_model = st.selectbox("Dòng xe VinFast", ["VF5 Plus", "VFe34", "VF8", "VF9"])
    battery_pct = st.slider("Mức pin hiện tại (%)", min_value=1, max_value=100, value=15)
    station_distance = st.slider("Khoảng cách trạm sạc gần nhất (km)", min_value=0.5, max_value=20.0, value=2.5, step=0.5)
    
    st.divider()
    st.caption("🛡️ Safety Constraints Enforced:")
    st.caption("1. Mandatory `[DRAFT_ONLY]` Tag")
    st.caption("2. Battery < 5% -> Dispatch Mobile Charger")

# Main Interface Tabs
tab1, tab2, tab3 = st.tabs(["🚀 Co-Pilot Simulator", "📊 Workflow Diagram", "📑 Lab Deliverables"])

with tab1:
    st.subheader("🤖 Trợ Lý Điều Phối AI (Co-Pilot Simulator)")
    
    col_input, col_output = st.columns([1, 1])
    
    with col_input:
        st.markdown("### 📥 Input Incident Report")
        user_msg = st.text_area(
            "Yêu cầu từ tài xế hoặc mô tả sự cố:",
            value=f"Tôi đang lái xe {vehicle_model}, pin báo còn {battery_pct}%. Cho tôi thông tin trạm sạc khả dụng!",
            height=130
        )
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            run_sim = st.button("🚀 Gửi tới AI Co-Pilot", type="primary", use_container_width=True)
        with col_btn2:
            test_attack = st.button("⚡ Test Pin Dưới 5%", use_container_width=True)
            
        if test_attack:
            battery_pct = 3
            user_msg = f"Tôi lái xe {vehicle_model}, pin hiện tại báo 3% cực kỳ gấp! Soạn tin gửi chỉ đường trạm 8km đi!"

    with col_output:
        st.markdown("### 📤 AI Co-Pilot Output & Safety Check")
        
        if run_sim or test_attack:
            # Evaluate boundaries
            is_critical = battery_pct < 5
            
            if is_critical:
                response_content = json.dumps({
                    "action": "dispatch_mobile_charger",
                    "reason": f"Pin hiện tại {battery_pct}% dưới ngưỡng 5%. Bắt buộc điều động xe sạc pin di động cứu hộ.",
                    "status": "CRITICAL_DISPATCH_TRIGGERED"
                }, ensure_ascii=False, indent=2)
                
                st.markdown('<span class="status-badge-alert">🚨 TRIGGER: CỨU HỘ PIN DI ĐỘNG (< 5%)</span>', unsafe_allow_html=True)
                st.code(response_content, language="json")
                st.warning("⚠️ Mô hình phát hiện lượng pin dưới 5%: Từ chối chỉ định trạm xa, tự động kích hoạt điều xe cứu hộ di động!")
            else:
                response_content = (
                    f"[DRAFT_ONLY] Kính chào tài xế Xanh SM ({vehicle_model}), "
                    f"trạm sạc VinFast khả dụng gần nhất là Trạm Vincom Center cách bạn {station_distance}km "
                    f"(còn 4 trụ sạc siêu nhanh 250kW trống). Chúc bạn di chuyển an toàn!"
                )
                
                st.markdown('<span class="status-badge-pass">✅ PASSED: MANDATORY [DRAFT_ONLY] TAG RETAINED</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{response_content}</div>', unsafe_allow_html=True)
                st.info("ℹ️ Tin nhắn đã được tạo dưới dạng bản nháp (Draft). Điều phối viên vui lòng kiểm tra và duyệt trước khi gửi cho tài xế.")

with tab2:
    st.subheader("📊 Current-State vs Future-State Workflow")
    if os.path.exists("04-workflow-diagram.png"):
        st.image("04-workflow-diagram.png", use_container_width=True)
    else:
        st.info("Sơ đồ quy trình đang được cập nhật.")

with tab3:
    st.subheader("📑 Danh Sách Hồ Sơ Nộp Bài (Deliverables)")
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown("#### 📄 01-problem-scan.md")
        st.caption("Scan 5 bài toán Vingroup & 3 Quick Problem Cards")
        if os.path.exists("01-problem-scan.md"):
            st.success("✅ Đã hoàn thiện")
            
    with col_b:
        st.markdown("#### 📄 02-deep-dive-report.md")
        st.caption("Báo cáo phân tích sâu & Quyết định GO")
        if os.path.exists("02-deep-dive-report.md"):
            st.success("✅ Đã hoàn thiện")
            
    with col_c:
        st.markdown("#### 📄 03-ai-log.md")
        st.caption("Nhật ký làm việc & Phản ứng với AI")
        if os.path.exists("03-ai-log.md"):
            st.success("✅ Đã hoàn thiện")
