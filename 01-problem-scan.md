# Tên nhóm: B2
# Họ và tên: Chu Thuỳ Dương

---

# 01 — Problem Scan & Quick Problem Cards
**Đơn vị:** Vin Smart Future (Vingroup)  
**Dự án:** AI Product Scoping & Operational Boundary Prototyping  
**Mảng vận hành trọng tâm:** Xanh SM (GSM) — Vận hành đội xe điện thông minh  
**Học viên thực hiện:** Chu Thùy Dương  
**Vai trò:** AI Product Engineer — Vin Smart Future  

---

## 🏛️ Bối cảnh nhiệm vụ: AI Engineer tại Vin Smart Future

Vin Smart Future được thành lập nhằm hợp nhất toàn bộ năng lực công nghệ, AI và tự động hóa cốt lõi của Tập đoàn Vingroup, phục vụ các công ty thành viên: **VinFast, Xanh SM (GSM), Vinhomes, Vinmec, Vinpearl**.

Nhiệm vụ của tôi trong đợt scoping này là:
1. Sử dụng **4 Lenses** quét qua toàn diện các hoạt động vận hành của các công ty thành viên để định vị các điểm rò rỉ hiệu suất, lãng phí thời gian và điểm nghẽn (bottleneck).
2. Phát triển **3 Quick Problem Cards** theo chuẩn đo lường của Vingroup.
3. Lựa chọn bài toán có độ sẵn sàng cao nhất, giá trị kinh doanh lớn và rủi ro có thể kiểm soát được bằng ranh giới vận hành (Operational Boundary).

---

# 🔍 Phase 1 — SCAN: Quét cơ hội bài toán AI (4 Lenses)

Áp dụng 4 Lăng kính (Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain) vào hệ sinh thái Vingroup:

| # | Công ty thành viên | Lăng kính (Lens) | Tên quy trình / Bài toán | Mô tả ngắn hiện trạng vận hành |
|---|-------------------|------------------|--------------------------|--------------------------------|
| 1 | **Xanh SM (GSM)** | **Lặp lại (Repetitive)** | Phân bổ & điều phối lại chuyến xe | Tự động xử lý và tối ưu điều phối khi khách hàng thay đổi điểm đến giữa hành trình hoặc tài xế yêu cầu đổi cuốc. |
| 2 | **Xanh SM (GSM)** | **Tốn thời gian (Time-consuming)** | **Xử lý sự cố pin khẩn cấp & điều phối trạm sạc thực địa** | **Điều phối viên (Dispatcher) tra cứu thủ công vị trí GPS xe, kiểm tra trạng thái trụ sạc VinFast còn trống và soạn thảo tin nhắn hướng dẫn cho tài xế đang cạn kiệt pin (mất 12-15 phút/cuộc gọi).** |
| 3 | **VinFast** | **Lặp lại (Repetitive)** | Đối soát hóa đơn phiên sạc đối tác | So khớp hàng trăm nghìn giao dịch sạc điện hàng tuần giữa hệ thống backend VinFast và dữ liệu thanh toán đối tác bên thứ ba. |
| 4 | **Vinhomes** | **AI-upgrade (Nâng cấp AI)** | Phân loại & route phản ánh của cư dân | Tự động đọc và điều hướng các ticket/khiếu nại (mất nước, sự cố thang máy, phí dịch vụ) trên ứng dụng Vinhomes Resident tới đúng ban quản lý tòa nhà. |
| 5 | **Vinmec** | **Stakeholder Pain (Đau từ người khác)** | Soạn tóm tắt bệnh án xuất viện (Discharge Summary) | Bác sĩ lâm sàng mất 20–30 phút/bệnh nhân để tổng hợp kết quả xét nghiệm, chẩn đoán thành bản tóm tắt xuất viện dễ hiểu cho người bệnh. |
| 6 | **Vinpearl** | **Tốn thời gian (Time-consuming)** | Xử lý yêu cầu đặt phòng đoàn (MICE/Group Booking) | Đọc và bóc tách email đặt phòng phức tạp từ các đại lý du lịch, kiểm tra phòng trống theo danh mục và draft báo giá. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Từ danh sách SCAN, 3 bài toán được đưa vào đánh giá nhanh gồm:
* **Card #1:** Xanh SM — Xử lý sự cố pin khẩn cấp & điều hướng trạm sạc thực địa.
* **Card #2:** Vinhomes — Phân loại & điều hướng khiếu nại cư dân trên App Resident.
* **Card #3:** Vinmec — Trợ lý tổng hợp tóm tắt hồ sơ xuất viện cho bệnh nhân.

---

### 🎴 QUICK PROBLEM CARD #1 (Lựa chọn chính của nhóm)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                   │
│                                                                         │
│ Bài toán: Hỗ trợ điều phối viên Xanh SM xử lý khẩn cấp sự cố xe điện     │
│           hết pin trên đường, tự động tra cứu trụ sạc VinFast khả dụng   │
│           hoặc kích hoạt xe sạc lưu động khi pin dưới ngưỡng nguy hiểm. │
│                                                                         │
│ Công ty thành viên: [x] Xanh SM (GSM)     [ ] VinFast     [ ] Vinhomes  │
│                     [ ] Vinmec            [ ] Vinpearl                  │
│                                                                         │
│ Ai đang đau (Actor)?                                                    │
│ - Điều phối viên (Dispatcher): Quá tải xử lý cuộc gọi giờ cao điểm.    │
│ - Tài xế Xanh SM: Lo lắng xe chết máy giữa đường, mất cuốc, tắc đường. │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Nhận cuộc gọi khẩn cấp từ tài xế qua tổng đài                      │
│   ──> 2. Tra cứu thủ công toạ độ GPS xe trên hệ thống giám sát hành trình│
│   ──> 3. Mở portal mạng lưới trụ sạc VinFast tìm trạm còn cổng trống    │
│   ──> 4. Soạn thảo tin nhắn SMS/In-app hướng dẫn chi tiết đường đi       │
│   ──> 5. Gọi điện liên hệ đội xe sạc pin di động nếu xe cạn kiệt pin    │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất?                                         │
│ - Bước 3 & Bước 4: Mất 10-12 phút/lượt xử lý.                           │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                   │
│ - Bước 3 & Bước 4: Tự động trích xuất dữ liệu, định vị trạm sạc gần     │
│   nhất theo chuẩn cổng sạc của xe, và tự động soạn thảo bản nháp       │
│   [DRAFT_ONLY] cho điều phối viên duyệt 1-click.                       │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ - Metric 1: Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt. │
│ - Metric 2: 100% tin nhắn hướng dẫn có nhãn [DRAFT_ONLY] bắt buộc duyệt.│
│ - Metric 3: 0% trường hợp hướng dẫn xe pin < 5% đi xa hơn 5km.          │
│                                                                         │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature  [ ] Agent     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 🎴 QUICK PROBLEM CARD #2

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                   │
│                                                                         │
│ Bài toán: Tự động phân loại, trích xuất thực thể và điều hướng phản ánh │
│           của cư dân trên ứng dụng Vinhomes Resident về đúng phòng ban. │
│                                                                         │
│ Công ty thành viên: [ ] Xanh SM     [ ] VinFast     [x] Vinhomes        │
│                     [ ] Vinmec      [ ] Vinpearl                        │
│                                                                         │
│ Ai đang đau (Actor)?                                                    │
│ - Nhân viên CSKH/Ban quản lý Vinhomes: Mất thời gian đọc thủ công hàng  │
│   nghìn ý kiến, phân loại nhầm dẫn đến chậm trễ giải quyết.             │
│ - Cư dân: Chờ phản hồi quá 24h, bức xúc vì câu trả lời rập khuôn.       │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Cư dân gửi ticket khiếu nại qua App Vinhomes Resident              │
│   ──> 2. Nhân viên CSKH đọc nội dung text/ảnh, phân loại thủ công       │
│   ──> 3. Forward ticket tới bộ phận liên quan (Kỹ thuật/An ninh/Lễ tân) │
│   ──> 4. Soạn thảo phản hồi tiếp nhận gửi cho cư dân                    │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất?                                         │
│ - Bước 2 & Bước 3: Mất 8–10 phút/ticket, thường xuyên phân loại nhầm.   │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                   │
│ - Bước 2: Dùng LLM phân loại nhãn (kỹ thuật, an ninh, vệ sinh...) và     │
│   trích xuất mức độ khẩn cấp (Emergency Detection).                     │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ - Độ chính xác phân loại tự động đạt >= 92%.                            │
│ - Rút ngắn thời gian phản hồi ban đầu từ 12 giờ xuống dưới 15 phút.     │
│                                                                         │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature  [ ] Agent     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 🎴 QUICK PROBLEM CARD #3

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                   │
│                                                                         │
│ Bài toán: Trợ lý AI tổng hợp dữ liệu khám bệnh, xét nghiệm để dự thảo   │
│           bản tóm tắt bệnh án xuất viện dễ hiểu cho bệnh nhân Vinmec.   │
│                                                                         │
│ Công ty thành viên: [ ] Xanh SM     [ ] VinFast     [ ] Vinhomes        │
│                     [x] Vinmec      [ ] Vinpearl                        │
│                                                                         │
│ Ai đang đau (Actor)?                                                    │
│ - Bác sĩ điều trị: Áp lực hành chính sau giờ khám, tốn 20-30 phút/hồ sơ.│
│ - Bệnh nhân & người nhà: Không hiểu thuật ngữ chuyên môn phức tạp.       │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Bác sĩ mở bệnh án điện tử (EMR), đọc lại diễn tiến điều trị        │
│   ──> 2. Sao chép các chỉ số xét nghiệm quan trọng và đơn thuốc         │
│   ──> 3. Gõ tay bản tóm tắt xuất viện và dặn dò tái khám                │
│   ──> 4. In ấn và giải thích trực tiếp cho bệnh nhân                    │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất?                                         │
│ - Bước 2 & 3: Mất 20 phút/bệnh nhân, dễ sót thông tin tiền sử dị ứng.  │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                   │
│ - Bước 2 & 3: LLM tổng hợp diễn tiến và draft bản dặn dò song ngữ.      │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ - Tiết kiệm 70% thời gian soạn hồ sơ (từ 25 phút xuống 7 phút).         │
│ - 100% hồ sơ xuất viện phải có chữ ký điện tử xác nhận của Bác sĩ.      │
│                                                                         │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature  [ ] Agent     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn bài toán Deep-Dive của nhóm

Nhóm quyết định chọn **Quick Problem Card #1 — Xanh SM Xử lý sự cố pin khẩn cấp & điều phối trạm sạc thực địa** làm bài toán trọng tâm để tiến hành Deep-Dive và xây dựng Technical Prompt Prototype.

### Lý do lựa chọn:
1. **Tính cấp thiết thời gian thực (Real-time Mission Critical):**
   Xe điện hết pin giữa đường gây ách tắc giao thông, rủi ro an toàn cho tài xế/khách hàng và làm gián đoạn doanh thu tức thì của Xanh SM (~80 ca/ngày tại các đô thị lớn).
2. **Ranh giới an toàn rõ ràng và có thể kiểm thử (Clear Operational Boundaries):**
   Bài toán có các ngưỡng vật lý và an toàn cụ thể:
   - Ngưỡng pin nguy hiểm (< 5%): Cấm tuyệt đối điều xe đi trạm sạc xa (> 5km), bắt buộc chuyển sang điều xe sạc di động (Mobile Charger).
   - Cơ chế Human-in-the-loop: Bắt buộc gắn thẻ `[DRAFT_ONLY]` để điều phối viên kiểm tra trước khi gửi, ngăn chặn AI tự ý gửi lệnh sai lệch.
3. **Giá trị kinh doanh (ROI) vượt trội:**
   Cắt giảm thời gian xử lý từ 15 phút xuống dưới 3 phút giúp giải phóng hàng trăm giờ công của đội ngũ điều vận mỗi tháng, tăng tỉ lệ sẵn sàng của đội xe.

### Lý do loại trừ 2 thẻ còn lại:
* **Card #2 (Vinhomes CSKH):** Mặc dù khối lượng lớn nhưng tính cấp bách thời gian thực thấp hơn (SLA theo giờ/ngày thay vì phút). Phần lớn tác vụ phân loại giai đoạn đầu có thể xử lý tốt bằng Rule-based keyword matching mà chưa nhất thiết cần LLM.
* **Card #3 (Vinmec Y tế):** Mảng y tế đòi hỏi tuân thủ pháp lý cực kỳ khắt khe về bảo mật dữ liệu sức khỏe (HIPAA/Luật Khám chữa bệnh), trách nhiệm pháp lý cao và cần quy trình thử nghiệm lâm sàng kéo dài, chưa phù hợp cho giai đoạn scoping prototype nhanh.

