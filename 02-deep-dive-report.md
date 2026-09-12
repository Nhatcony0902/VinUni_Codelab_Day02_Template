# 02 — Báo Cáo Phân Tích Sâu (Deep-Dive Report): Xanh SM Intelligent Battery Dispatcher

**Dự án:** Trợ lý Điều phối Sự cố Pin & Điều vận Xe Cứu hộ Thông minh  
**Đơn vị phát triển:** Vin Smart Future (Vingroup)  
**Đơn vị thụ hưởng:** Khối Vận Hành Xanh SM (GSM) & Hệ sinh thái Trạm sạc VinFast  
**Kỹ sư phụ trách:** Dương Hữu Đạt  

---

# 🏗️ Phase 3 — DEEP-DIVE: Phân Tích Kỹ Thuật Chi Tiết

## 3.1. Current-State Workflow Mapping (Quy trình Vận hành Hiện tại)

Khi xảy ra sự cố xe taxi điện Xanh SM cạn kiệt dung lượng pin (State of Charge - SoC < 5%) trên đường vận hành thực địa, quy trình thủ công diễn ra qua 5 bước:

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │
│ Nhận cuộc gọi   │ ────> │ Tra cứu GPS xe  │ ────> │ Tra cứu trạm    │
│ khẩn cấp        │  🔄   │ trên Dashboard  │  🔄   │ sạc VinFast     │
│ Actor: Tài xế   │       │ Actor: Dispatch │       │ Actor: Dispatch │
│ ⏱ 2 phút       │       │ ⏱ 2 phút       │       │ ⏱ 5 phút 🔴     │
└─────────────────┘       └─────────────────┘       └─────────────────┘
                                                             │
                                                             ▼
┌─────────────────┐                                 ┌─────────────────┐
│ Bước 5          │                                 │ Bước 4          │
│ Điều xe cứu hộ  │ <────────────────────────────── │ Soạn tin nhắn   │
│ hoặc đóng cuốc  │               🔄                │ hướng dẫn SMS   │
│ Actor: Dispatch │                                 │ Actor: Dispatch │
│ ⏱ 3 phút       │                                 │ ⏱ 4 phút 🔴     │
└─────────────────┘                                 └─────────────────┘
```

* ⏱ **Tổng thời gian xử lý trung bình:** **16 phút / lượt xử lý sự cố**.
* 🔄 **Handoff (Điểm chuyển giao thông tin):**
  1. *Handoff 1:* Tài xế truyền đạt thông tin (biển số xe, mức pin hiện tại, vị trí ước lượng) qua điện thoại cho điều phối viên.
  2. *Handoff 2:* Điều phối viên chuyển đổi tọa độ GPS sang bản đồ mạng lưới trạm sạc VinFast.
  3. *Handoff 3:* Điều phối viên gửi tin nhắn SMS / Zalo hướng dẫn cho tài xế.
* 🔴 **Bottlenecks (Điểm nghẽn cổ chai nghiêm trọng):**
  * **Bước 3 (Tra cứu trạm sạc - 5 phút):** Điều phối viên phải kiểm tra thủ công trạm nào còn trụ sạc DC nhanh trống, công suất phù hợp dòng xe (VF e34, VF5, VF8) và khoảng cách thực tế. Vào giờ cao điểm, trạm hiển thị trống trên app có thể bị chiếm chỗ ngay khi xe đến nơi.
  * **Bước 4 (Soạn tin nhắn chỉ đường - 4 phút):** Soạn thảo thủ công dễ gây nhầm lẫn địa chỉ, đặc biệt khi tài xế đang hoảng loạn vì xe có nguy cơ sập nguồn giữa đường giao thông đông đúc.

---

## 3.2. Problem Statement (Khung 6-Field Chuẩn Vin Smart Future)

| Field | Nội dung phân tích kỹ thuật & nghiệp vụ |
|:---|:---|
| **1. Actor / Operator** | • **Người vận hành chính:** Điều phối viên (Dispatcher) tại Trung tâm Điều hành Vận tải Xanh SM.<br>• **Người thụ hưởng trực tiếp:** Bác tài Xanh SM (taxi điện, xe máy điện) và hành khách trên xe. |
| **2. Current Workflow** | Điều phối viên tiếp nhận cuộc gọi khẩn cấp từ tài xế ➔ Tra cứu thủ công tọa độ GPS xe trên bản đồ quản lý đội xe ➔ Tra cứu hệ thống trạm sạc VinFast để tìm trạm khả dụng gần nhất ➔ Tính nhẩm khoảng cách ➔ Gõ tin nhắn SMS chỉ đường gửi tài xế hoặc gọi điện cho đội xe cứu hộ sạc lưu động (Mobile Charging Van). |
| **3. Bottleneck** | **Xử lý thủ công, phân mảnh dữ liệu và độ trễ cao:** Mất 12-16 phút cho mỗi sự cố. Rủi ro lớn nhất là điều phối viên ước lượng sai quãng đường hoặc chọn trạm sạc xa > 5km trong khi pin xe chỉ còn dưới 5%, khiến xe bị sập nguồn hoàn toàn trên đường phố, gây cản trở giao thông và hư hại tuổi thọ pin LFP. |
| **4. Business Impact** | • **Tổn thất chi phí cứu hộ:** Mỗi ca xe chết máy cần xe cẩu kéo về xưởng tốn 1.200.000 VNĐ - 2.000.000 VNĐ.<br>• **Rò rỉ doanh thu:** Xe nằm đường trung bình 4 - 6 tiếng, làm giảm 35% hiệu suất khai thác cuốc xe của tài xế trong ngày.<br>• **Trải nghiệm khách hàng:** Gián đoạn hành trình của khách, đánh giá 1-sao và nguy cơ khủng hoảng truyền thông thương hiệu xe điện xanh. |
| **5. Success Metric** | 1. **Thời gian xử lý (Resolution Time):** Giảm thời gian từ khi nhận tin đến khi phát lệnh điều hướng từ **16 phút ➔ dưới 2.5 phút** (giảm > 84%).<br>2. **Độ an toàn ranh giới (Safety Boundary Enforcement):** **100% các trường hợp pin < 5%** được tự động kích hoạt điều xe sạc lưu động hoặc hướng dẫn trạm dưới 3km; **0%** bị chỉ định trạm sạc > 5km.<br>3. **Năng suất điều phối viên:** Một nhân viên có thể xử lý đồng thời 8 - 10 ca sự cố thay vì tối đa 2 ca như trước đây. |
| **6. Operational Boundary (Ranh giới Vận hành Bắt buộc)** | 🛑 **QUY TẮC BẢO VỆ TUYỆT ĐỐI (NON-NEGOTIABLE GUARDRAILS):**<br>1. **Tag bắt buộc `[DRAFT_ONLY]`:** Mọi phản hồi, khuyến nghị do AI tạo ra **BẮT BUỘC** phải gắn thẻ `[DRAFT_ONLY]` ở đầu văn bản. AI KHÔNG ĐƯỢC PHÉP tự ý gửi tin trực tiếp đến tài xế khi chưa qua màn hình xác nhận (1-click approve) của Điều phối viên (Human-in-the-loop).<br>2. **Ngưỡng pin tới hạn (< 5% SoC):** Nếu mức pin xe dưới 5%, AI **TUYỆT ĐỐI KHÔNG** được đề xuất trạm sạc cách xa > 5km. Trong trường hợp này, AI phải tự động xuất cấu trúc lệnh điều động xe sạc lưu động: `{"action": "dispatch_mobile_charger", "reason": "<lý do chi tiết>"}`.<br>3. **Quyền riêng tư vị trí:** Không xuất thông tin tọa độ GPS cá nhân của khách hàng trên xe ra ngoài phạm vi điều vận. |

---

## 3.3. Future-State Flow & Đánh Giá Mức Độ Phù Hợp AI (AI Fit)

### 📊 AI-Fit Matrix: So sánh lựa chọn kiến trúc

| Tiêu chí | 1. Pure Rule-Based Code | 2. LLM Feature + Guardrails (ĐƯỢC CHỌN) | 3. Autonomous Multi-Agent Loop |
|:---|:---|:---|:---|
| **Khả năng hiểu ngữ cảnh** | ❌ Kém: Khó parse được tin nhắn khẩn cấp, tiếng Việt nói nhanh, sai chính tả của tài xế. | ✅ Xuất sắc: Hiểu đa dạng câu từ tài xế (mã lỗi, tình trạng pin, vị trí tương đối). | ⚠️ Thừa thãi: Quá phức tạp so với yêu cầu bài toán điều vận cứu hộ. |
| **Thời gian phản hồi** | ⚡ Rất nhanh (< 100ms) | ⚡ Nhanh (1 - 2 giây với Gemini 2.5 Flash) | 🐢 Chậm (10 - 30 giây qua nhiều bước suy luận) |
| **Khả năng kiểm soát ranh giới** | 🔒 Tuyệt đối nhưng cứng nhắc | 🔒 Vững chắc khi kết hợp System Prompt + Regex Filter | ⚠️ Rủi ro rò rỉ ranh giới (Agent drift) cao |
| **Kết luận lựa chọn** | Dùng làm lớp lọc dữ liệu và tính khoảng cách địa lý. | **LỰA CHỌN TỐI ƯU:** Dùng Gemini 2.5 Flash để trích xuất ngữ cảnh, draft tin nhắn và quyết định hành động cứu hộ. | Không phù hợp ở giai đoạn này. |

---

### 🔄 Future-State Workflow (Quy trình Tương lai Tích hợp AI)

```text
[Tài xế gửi tin nhắn/báo sự cố] 
              │
              ▼
🔵 AI STEP (LLM Feature):
   • Trích xuất mã xe, mức pin (SoC), tọa độ GPS.
   • Kiểm tra ranh giới an toàn:
     - Nếu Pin >= 5%: Tìm trạm VinFast trống gần nhất (< 5km) ➔ Draft tin hướng dẫn.
     - Nếu Pin < 5%: Kích hoạt {"action": "dispatch_mobile_charger"} ➔ Cảnh báo nguy hiểm.
   • Gắn cờ bắt buộc [DRAFT_ONLY].
              │
              ├─────────────────────────────────────────┐
              │ (Nếu API lỗi / Parse thất bại)          │ (Luồng bình thường)
              ▼                                         ▼
↩️ FALLBACK STEP:                             🟢 HUMAN-IN-THE-LOOP (HITL):
   • Tự động chuyển còi báo động về              • Điều phối viên nhìn bản thảo
     màn hình Điều phối viên thủ công.             trên giao diện Dispatch Dashboard.
   • Hiển thị trạm sạc gần nhất theo             • Nhấn [1-Click Approve] để gửi tin
     thuật toán Haversine truyền thống.            cho tài xế hoặc gọi xe sạc lưu động.
```

---

# 🏁 Phase 5 — EVALUATE: Đánh Giá Sẵn Sàng & Quyết Định Đầu Tư

### 📋 AI Readiness Checklist

1. [x] **Dữ liệu mẫu/logs sạch:** Hệ thống GSM và VinFast đã có sẵn telemetry API truyền dữ liệu real-time về vị trí xe, dung lượng pin (SoC), trạng thái các trụ sạc VinFast theo cổng CCS2.
2. [x] **Kiểm soát rủi ro an toàn:** Rủi ro AI bị hallucination được kiểm soát 100% nhờ:
   * Thẻ `[DRAFT_ONLY]` bắt buộc con người duyệt trước khi phát lệnh.
   * Ranh giới cứng: Pin < 5% bắt buộc chuyển luồng `dispatch_mobile_charger`.
   * Luồng Fallback quy tắc cứng nếu Gemini API không phản hồi trong 3 giây.
3. [x] **Stakeholders sẵn sàng:** Khối Vận Hành Xanh SM và Ban Giám Đốc Vin Smart Future đều thống nhất ưu tiên giảm tải cho Điều phối viên và triệt tiêu tình trạng xe sập nguồn trên đường.

---

### 🎯 Quyết định của Ban Giám Đốc Vin Smart Future:

# ✅ **QUYẾT ĐỊNH: GO (Triển khai Bản mẫu Hẹp - Pilot Prototype)**

### 📝 Lý giải Quyết định (Justification):
1. **Giá trị kinh tế vượt trội:** Giảm thời gian chết máy cứu hộ từ 16 phút xuống dưới 2.5 phút, ước tính tiết kiệm cho Xanh SM hơn 850 triệu VNĐ mỗi tháng tiền chi phí xe cẩu kéo và thiệt hại do ngưng trệ cuốc xe tại Hà Nội và TP.HCM.
2. **Kiến trúc kỹ thuật khả thi & tiết kiệm chi phí:** Sử dụng mô hình **Gemini 2.5 Flash** với độ trễ cực thấp (< 1.5s), chi phí token không đáng kể (dưới 0.0005 USD / lượt xử lý).
3. **Mức độ an toàn cao:** Có sự kết hợp chặt chẽ giữa AI tạo sinh và Human-in-the-loop, không tạo ra bất kỳ rủi ro vận hành hay pháp lý nào cho thương hiệu Vingroup.
