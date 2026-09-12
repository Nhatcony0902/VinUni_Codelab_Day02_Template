# 01 — Problem Scan & Quick Problem Cards (Vin Smart Future)

**Tên nhóm:** B2  
**Họ và tên:** Dương Hữu Đạt  
**Email:** duongdat6672@gmail.com  
**Đơn vị:** Vin Smart Future (Phối hợp cùng Khối Vận Hành Xanh SM - GSM)  
**Chi nhánh / Mảng:** Vận tải hành khách & Đội xe điện thông minh (EV Fleet Operations)  

---

# 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Vận Hành (4 Lenses)

Áp dụng 4 Lăng kính (*Lặp lại, Tốn thời gian, AI có thể tốt hơn, Pain từ người khác*) để rà soát quy trình vận hành thực tế tại các công ty thành viên Vingroup (trọng tâm là Xanh SM & VinFast):

| # | Subsidiary | Lăng kính (Lens) | Mô tả ngắn bài toán / Điểm nghẽn vận hành |
|---|---|---|---|
| **1** | **Xanh SM** | **Lặp lại** *(Repetitive)* | **Tự động rà soát & điều chỉnh cuốc xe đổi lộ trình:** Khi khách hàng yêu cầu đổi điểm đến giữa hành trình, hệ thống cần tính lại giá vé, phân bổ lại lịch đón tiếp theo của tài xế thay vì điều phối viên phải can thiệp thủ công. |
| **2** | **Xanh SM** | **Tốn thời gian** *(Time-consuming)* | **Xử lý sự cố xe điện cạn kiệt pin giữa đường:** Tài xế gọi báo pin khẩn cấp (< 5%), điều phối viên mất 15-20 phút tra cứu GPS thủ công, kiểm tra trụ sạc VinFast còn trống và soạn tin hướng dẫn hoặc điều xe sạc lưu động. |
| **3** | **Xanh SM** | **AI có thể tốt hơn** *(AI-upgrade)* | **Dự báo nhu cầu & Điều hướng đội xe trước giờ cao điểm:** Thay vì tài xế di chuyển tự do hoặc chờ khách thụ động, trợ lý ảo phân tích dữ liệu chuyến bay đến, thời tiết mưa bão, sự kiện để gợi ý cụm đón khách tiềm năng. |
| **4** | **Xanh SM** | **Pain từ người khác** *(Stakeholder Pain)* | **Xử lý khiếu nại khách bỏ quên tài sản trên xe:** Khách hàng phàn nàn vì mất 24h-48h tổng đài mới liên hệ được tài xế xác minh đồ thất lạc; cần trợ lý tự động đối soát chuyến xe và kết nối an toàn 2 chiều trong 15 phút. |
| **5** | **Xanh SM** | **Tốn thời gian** *(Time-consuming)* | **Phân tích lý do khách hủy chuyến giờ cao điểm:** Đội ngũ back-office mất hàng chục giờ mỗi tuần nghe ghi âm cuộc gọi và đọc ghi chú text rời rạc của tài xế để tìm pattern lỗi hệ thống điều xe. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn Top 3 bài toán cấp thiết nhất từ danh sách trên để hoàn thiện thẻ đánh giá nhanh:

---

### 📇 QUICK PROBLEM CARD #1 (Bài toán Trọng tâm — Deep-Dive)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                   │
│                                                                         │
│ Bài toán: Tài xế Xanh SM báo sự cố cạn pin (< 5%) trên đường, cần điều   │
│           hướng khẩn cấp đến trạm sạc khả dụng hoặc điều xe sạc lưu động.│
│ Công ty thành viên: [x] Xanh SM (GSM)     [x] VinFast                   │
│                                                                         │
│ Ai đang đau (Actor)?                                                    │
│ - Tài xế Xanh SM: Nguy cơ chết máy giữa đường cao tốc/phố đông, hoang mang.│
│ - Điều phối viên (Dispatcher): Quá tải tra cứu bản đồ, tính toán cự ly.  │
│ - Khách hàng: Chuyến đi bị gián đoạn, trải nghiệm dịch vụ giảm sút.     │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Tài xế gọi hotline khẩn cấp báo pin dưới 5%                        │
│   ──> 2. Điều phối viên tra cứu tọa độ GPS xe trên dashboard            │
│   ──> 3. Tra cứu hệ thống trạm sạc VinFast để tìm cổng sạc còn trống     │
│   ──> 4. Soạn tin nhắn hướng dẫn tài xế hoặc liên hệ xe cứu hộ          │
│   ──> 5. Cập nhật trạng thái cuốc xe lên hệ thống điều vận              │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất?                                         │
│   Bước 3 & 4 (⏱ 12-15 phút/lượt; dễ chỉ nhầm trạm đang full hoặc quá xa). │
│                                                                         │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                   │
│   Bước 3 & 4: Tự động trích xuất vị trí, dung lượng pin, đối soát trạm   │
│   trống trong bán kính an toàn, draft sẵn chỉ dẫn hoặc kích hoạt cứu hộ.│
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                    │
│   • Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 2.5 phút/lượt.        │
│   • 0% trường hợp xe dưới 5% pin bị chỉ định trạm sạc xa > 5km.          │
│                                                                         │
│ Quick Architecture: [x] LLM Feature kết hợp Rule-based Guardrails        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #2

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                   │
│                                                                         │
│ Bài toán: Tự động xử lý khiếu nại "để quên hành lý/tài sản" trên xe     │
│           thông qua trích xuất thực thể và kích hoạt quy trình tìm kiếm. │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau (Actor)?                                                    │
│ - Hành khách: Bị mất giấy tờ, điện thoại, lo lắng và gọi giục tổng đài. │
│ - Nhân viên CSKH: Mất thời gian nghe thoại, ghi chép tay đặc điểm đồ vật.│
│                                                                         │
│ Workflow thủ công hiện tại:                                             │
│   1. Khách gửi tin nhắn/gọi tổng đài ──> 2. CSKH tạo ticket thủ công     │
│   ──> 3. CSKH tra mã chuyến ──> 4. Gọi tài xế hỏi thăm                  │
│   ──> 5. Phản hồi lại khách hẹn ngày nhận đồ                            │
│                                                                         │
│ Bước nào tốn thời gian nhất?                                            │
│   Bước 2 & 3 (⏱ 30 phút để đọc mô tả, phân loại mức độ khẩn cấp).        │
│                                                                         │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                   │
│   Bước 2: Dùng LLM trích xuất tự động: Tên đồ vật, màu sắc, vị trí ghế,  │
│   mức độ khẩn cấp (giấy tờ tùy thân/ví tiền = High Priority).            │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                    │
│   • Thời gian phản hồi xác nhận cho khách giảm từ 120 phút ──> < 15 phút.│
│   • Tỉ lệ trích xuất đúng thông tin đồ vật đạt > 92%.                    │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (Entity Extraction & Auto-ticketing)│
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #3

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                   │
│                                                                         │
│ Bài toán: Tự động phân loại lý do hủy chuyến giờ cao điểm từ tin nhắn    │
│           trao đổi giữa tài xế và khách hàng để phát hiện lỗi điều xe.   │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau (Actor)?                                                    │
│ - Trưởng phòng Vận hành Xanh SM: Thiếu báo cáo real-time về điểm nghẽn.  │
│ - Khách hàng & Tài xế: Bực bội vì thuật toán gán cuốc quá xa điểm đón.  │
│                                                                         │
│ Workflow thủ công hiện tại:                                             │
│   1. Hệ thống ghi nhận cuốc xe bị cancel                                │
│   ──> 2. Cuối tuần xuất file Excel chứa hàng chục nghìn đoạn chat/note   │
│   ──> 3. Nhân viên đọc thủ công từng đoạn chat và gắn nhãn phân loại     │
│   ──> 4. Làm báo cáo tổng hợp PowerPoint                                │
│                                                                         │
│ Bước nào tốn thời gian nhất?                                            │
│   Bước 3: Mất 16 giờ làm việc/tuần của 2 chuyên viên phân tích dữ liệu.  │
│                                                                         │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                   │
│   Bước 3: LLM tự động gắn nhãn (Do kẹt xe, Do tài xế từ chối, Do pin,   │
│   Do gán sai vị trí GPS) theo thời gian thực ngay khi hủy cuốc.          │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                    │
│   • Giảm thời gian trích xuất insight từ 7 ngày ──> Real-time (vài giây).│
│   • Độ chính xác phân loại danh mục lỗi đạt > 90%.                       │
│                                                                         │
│ Quick Architecture: [x] LLM Batch Processing / Classification Pipeline  │
└─────────────────────────────────────────────────────────────────────────┘
```
