<!-- Nhóm: B2
Họ và Tên: Lục Tiến Đạt
Email: luctiendat910@gmail.com -->
# 🏗️ 02-deep-dive-report.md — Phân Tích Sâu Dự Án AI (Vin Smart Future)

> **Dự án Lựa Chọn:** Xanh SM Intelligent Battery & Emergency Dispatcher Co-Pilot  
> **Công ty thành viên:** GSM (Xanh SM)  
> **Đơn vị phát triển:** Vin Smart Future  

---

## 📌 1. Bối cảnh & Lý do chọn bài toán

Trong hệ thống vận hành xe taxi/xe máy điện thông minh **Xanh SM**, trung bình mỗi ngày tại khu vực Hà Nội có khoảng **80-100 sự cố báo cạn pin hoặc hết pin đột xuất** trên đường. 

Các điều phối viên (Dispatchers) phải căng mình xử lý từng trường hợp bằng tay: tra cứu vị trí GPS, đối chiếu danh sách trạm sạc VinFast còn trụ trống phù hợp với dòng xe (VF5, VFe34, VF8, VF9), soạn thảo tin nhắn chỉ đường cho tài xế và gọi xe cứu hộ pin di động (Mobile Charging Vehicle) nếu pin rơi vào ngưỡng nguy hiểm (< 5%). Quy trình này mất tới **15 phút/lượt**, gây nghẽn cổ chai và áp lực nặng nề cho trung tâm điều vận.

---

## 🔄 2. Current-State Workflow Mapping (Quy trình hiện tại)

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn văn bản │
│ gọi sự cố    │ ──→ │ vị GPS xe    │ ──→ │ sạc VinFast  │ ──→ │ hướng dẫn    │
│              │     │              │     │ còn trụ trống│     │ gửi tài xế   │
│ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │
│ ⏱ 2 phút     │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │
│ In: Điện thoại│     │ In: Biển số  │     │ In: Vị trí GPS│     │ In: Raw data │
│ Out: Log sự cố│     │ Out: Toạ độ  │     │ Out: Địa chỉ │     │ Out: SMS/App │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Gọi xe cứu   │
                                                               │ hộ (nếu cần) │
                                                               │ Ai: Dispatch │
                                                               │ ⏱ 1 phút     │
                                                               └──────────────┘
🔴 = Bottlenecks (Bước 3 & 4 tốn 10 phút xử lý thủ công)
⏱ Tổng thời gian xử lý thủ công: 15 phút/lượt sự cố.
```

---

## 📝 3. Problem Statement (6-Field Standard)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM (GSM). |
| **2. Current Workflow** | Điều phối viên nhận báo cáo sự cố sạc từ tài xế, tra cứu định vị GPS xe trên bản đồ, mở dashboard trạm sạc VinFast tra trụ trống phù hợp dòng xe, tự viết tin nhắn hướng dẫn/định vị gửi cho tài xế, và gọi xe sạc pin di động nếu pin quá thấp. 5 bước hoàn toàn thủ công. |
| **3. Bottleneck** | Bước 3 (5 min) & Bước 4 (5 min): Tra cứu thủ công trụ sạc trống theo đúng chuẩn cổng sạc của xe và soạn tin nhắn hướng dẫn đường đi chuẩn hóa bằng Tiếng Việt. |
| **4. Business Impact** | Mỗi ngày lãng phí ~20 giờ làm việc của team điều phối; tăng thời gian xe taxi nằm chờ; rò riri doanh thu ~15% trong giờ cao điểm và gây giảm điểm trải nghiệm khách hàng (CSAT). |
| **5. Success Metric** | 1. Giảm tổng thời gian xử lý sự cố từ **15 phút xuống dưới 3 phút** (giảm 80% thời gian).<br>2. Tỉ lệ hướng dẫn đúng trạm sạc khả dụng và phù hợp loại xe đạt **≥ 98%**. |
| **6. Operational Boundary** | AI được truy xuất API định vị xe, API trạng thái trạm sạc VinFast, tự động draft tin nhắn hướng dẫn kèm thẻ `[DRAFT_ONLY]`. **TUYỆT ĐỐI CẤM:** AI không được gửi thẳng tin nhắn mà không qua con người duyệt (HITL); khi pin < 5% CẤM chỉ định trạm xa hơn 5km mà BẮT BUỘC trigger dispatch xe cứu hộ `dispatch_mobile_charger`. |

---

## 🔮 4. Future-State Flow & AI Fit

### AI-Fit Matrix:
* **Lựa chọn:** **LLM Feature + HITL Gate**
* **Lý do:** Quy trình có tính cấu trúc, rủi ro khi điều phối nhầm trạm sạc rất lớn (gây hết pin giữa đường). Cần sự kết hợp giữa khả năng trích xuất/soạn thảo linh hoạt của LLM và sự phê duyệt cuối cùng của con người.

### Quy trình Tương lai (Future-State):

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ 🔵 Auto-pull │     │ 🔵 AI draft  │     │ 🟢 Dispatch  │
│ gọi sự cố    │ ──→ │ vị trí &     │ ──→ │ SMS chỉ dẫn  │ ──→ │ click duyệt  │
│              │     │ trạm sạc trống│    │ & chỉ đường  │     │ & gửi tài xế │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI draft lỗi
                                                               hoặc vi phạm boundary,
                                                               Dispatcher tự viết lại.
```

---

## 🏁 5. Evaluation & GO Decision

### AI Readiness Checklist:
1. [x] **Dữ liệu mẫu/API:** Đã có hệ thống API định vị xe Xanh SM và API trạng thái trạm sạc VinFast.
2. [x] **Kiểm soát rủi ro:** Đã thiết lập cơ chế Human-In-The-Loop (HITL) qua thẻ `[DRAFT_ONLY]` và Fallback plan.
3. [x] **Sự sẵn sàng của Stakeholders:** Khối vận hành Xanh SM sẵn sàng áp dụng Co-pilot để giảm tải cho điều phối viên.

### Quyết định cuối cùng của Vin Smart Future Board:
**[x] GO (Bắt đầu xây dựng Prototype)**

### Justification (Lý giải kỹ thuật & kinh tế):
1. **Khả thi kỹ thuật:** LLM Feature trên Gemini 2.5 Flash đáp ứng tốc độ phản hồi nhanh (< 2 giây), chi phí API cực thấp.
2. **Kiểm soát rủi ro tuyệt đối:** Ranh giới an toàn được mã hóa trực tiếp trong System Prompt và Assertions test code (`prompt_prototype.py`), loại bỏ rủi ro gửi nhầm tin hoặc chỉ đường sai khi xe cạn pin (< 5%).
3. **Hiệu quả kinh tế:** Tiết kiệm ~20 giờ công điều vận/ngày, nâng cao tỉ lệ phục vụ chuyến xe của đội taxi Xanh SM.
