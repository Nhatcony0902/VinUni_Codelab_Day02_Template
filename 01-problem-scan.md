# 01 — Problem Scan & Quick Cards (Ý tưởng Cá nhân)

> **Lab 02: AI Product Scoping — Vin Smart Future**
> File này tổng hợp kết quả **Phase 1 (SCAN)** và **Phase 2 (QUICK-ASSESS)** của cá nhân.

---

## 🔍 Phase 1 — SCAN: Bảng quét cơ hội AI

Áp dụng **4 Lenses** để quét các pain point vận hành trong hệ sinh thái Vingroup:

1. 🔁 **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày.
2. ⏱️ **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công.
3. 🤖 **AI có thể tốt hơn (AI-upgrade):** Dịch vụ hiện tại còn chậm hoặc phản hồi rập khuôn.
4. 🔴 **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên phàn nàn.

### 📝 List bài toán của tôi:

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|-----------|------|---------------------|
| 1 | Xanh SM (GSM) | 🔴 Pain từ người khác (Stakeholder Pain) | Dispatcher thủ công gọi điện/nhắn tin xử lý lịch sạc khẩn cấp khi pin xe < 20%, mất 8–12 phút/ca/xe. Với đội 5,000+ xe, ước tính ~600 giờ nhân công/ngày bị lãng phí. |
| 2 | Xanh SM (GSM) | ⏱️ Tốn thời gian (Time-consuming) | Nhân viên CSKH soạn thủ công phản hồi review 1-sao trên app/Google Maps, mất ~15 phút/phản hồi. Với ~200 review tiêu cực/ngày, tốn 50 giờ nhân công, tỷ lệ phản hồi chỉ đạt ~30%. |
| 3 | Vinhomes | 🔁 Lặp lại (Repetitive) | Nhân viên tổng đài phân loại thủ công ~500 ticket bảo trì/ngày từ app cư dân (điện, nước, thang máy...). Sai tuyến ~18%, gây xử lý lại mất thêm 2–3 ngày/ticket. |
| 4 | Vinmec | 🤖 AI có thể tốt hơn (AI-upgrade) | Bác sĩ mất 10–15 phút đọc lại hồ sơ bệnh án dài của bệnh nhân tái khám. AI tóm tắt tự động có thể tiết kiệm ~25% thời gian khám, tương đương thêm 2–3 bệnh nhân/ngày/bác sĩ. |
| 5 | VinFast | 🔴 Pain từ người khác (Stakeholder Pain) | Kỹ thuật viên ghi tay phiếu lỗi xe, nhân viên back-office nhập lại hệ thống ~20 phút/phiếu. Với 300+ phiếu/ngày, phát sinh 100 giờ nhập liệu, tỷ lệ sai ~12%, trì hoãn bảo hành. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn **top 3 bài toán** tiềm năng nhất để phân tích sâu hơn (10 phút/card).

---

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Nhân viên CSKH Xanh SM phải soạn thủ     │
│ công từng phản hồi cho review 1-sao trên app/Google Maps,  │
│ gây chậm trễ và tỷ lệ phản hồi thấp (~30%).                │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH Xanh SM (GSM)          │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận notification review 1-sao                         │
│   ──> 2. Đọc nội dung review & tra cứu thông tin chuyến    │
│   ──> 3. Soạn phản hồi cá nhân hóa thủ công (~15 phút)    │
│   ──> 4. Supervisor review & gửi phản hồi                  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–3 (⏱ 15 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào?                      │
│   Bước 2–3: AI tự tra cứu thông tin chuyến xe + generate   │
│   draft phản hồi cá nhân hóa, nhân viên chỉ review & gửi  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   "Giảm thời gian soạn từ 15 phút ──> dưới 2 phút/phản hồi │
│    Tỷ lệ phản hồi từ 30% ──> trên 85% trong vòng 30 ngày" │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent│
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #4                                       │
│                                                             │
│ Bài toán (1 câu): Bác sĩ Vinmec mất 10–15 phút đọc lại hồ │
│ sơ bệnh án dài của bệnh nhân tái khám, chiếm 25% thời gian │
│ khám và làm giảm số lượng bệnh nhân được phục vụ/ngày.     │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ chuyên khoa Vinmec             │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Bệnh nhân tái khám đặt lịch & đến phòng khám          │
│   ──> 2. Lễ tân gọi hồ sơ bệnh án từ hệ thống HIS         │
│   ──> 3. Bác sĩ mở hồ sơ & đọc lại toàn bộ lịch sử        │
│          (~10–15 phút/bệnh nhân)                            │
│   ──> 4. Bác sĩ bắt đầu hỏi khám và chẩn đoán             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 12 phút/lượt)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                      │
│   Bước 2–3: AI tự động tóm tắt hồ sơ thành 1 trang         │
│   highlight (chẩn đoán gần nhất, thuốc đang dùng, dị ứng,  │
│   kết quả xét nghiệm quan trọng) trước khi bác sĩ vào khám │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   "Giảm thời gian đọc hồ sơ từ 12 phút ──> dưới 2 phút    │
│    Tăng thêm 2–3 bệnh nhân/bác sĩ/ngày (~15% throughput)"  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent│
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                       │
│                                                             │
│ Bài toán (1 câu): Kỹ thuật viên VinFast ghi tay phiếu lỗi  │
│ xe, nhân viên back-office nhập lại thủ công vào hệ thống   │
│ (~20 phút/phiếu, sai 12%), gây chậm trễ phê duyệt bảo hành.│
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│   Kỹ thuật viên bảo hành + Nhân viên back-office VinFast   │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. KTV kiểm tra xe & ghi tay phiếu lỗi (mã lỗi, mô tả)  │
│   ──> 2. Chuyển phiếu giấy về văn phòng cuối ngày          │
│   ──> 3. Nhân viên nhập liệu vào hệ thống ERP (~20 phút)  │
│   ──> 4. Supervisor phê duyệt lệnh bảo hành                │
│   ──> 5. Gửi linh kiện & thực hiện sửa chữa                │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 20 phút/phiếu) │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                      │
│   Bước 1–3: KTV chụp ảnh phiếu → AI OCR + extract thông   │
│   tin cấu trúc (mã lỗi, số khung, mô tả) → tự điền ERP    │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   "Giảm thời gian nhập liệu từ 20 phút ──> dưới 2 phút    │
│    Giảm tỷ lệ sai từ 12% ──> dưới 2% trong vòng 60 ngày"  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent│
└─────────────────────────────────────────────────────────────┘
```

---

## 🔥 Stress-Test (CFO & Trưởng phòng Vận hành)

Áp dụng prompt phản biện để đánh giá chất lượng từng card:

### Card #2 — Xanh SM CSKH Review 1-sao
> **Điểm yếu phát hiện:**
> 1. Metric "tỷ lệ phản hồi 85%" không đo chất lượng — AI có thể phản hồi nhiều nhưng rập khuôn, gây tác dụng ngược với brand.
> 2. Baseline "15 phút/phản hồi" cần xác nhận bằng dữ liệu thực tế.
> 3. Template library 20–30 mẫu (rule-based) có thể giải quyết phần lớn trường hợp đơn giản mà không cần LLM.
>
> **Kết luận:** ✅ Giữ LLM — bổ sung metric CSAT và giới hạn phạm vi xử lý review phức tạp.

### Card #4 — Vinmec Tóm tắt bệnh án
> **Điểm yếu phát hiện:**
> 1. Rủi ro y tế nghiêm trọng nếu LLM tóm tắt sai — cần HITL bắt buộc trước khi bác sĩ dùng.
> 2. HIS hiện đại đã có tính năng tóm tắt structured data — cần kiểm tra hệ thống hiện tại trước.
> 3. Baseline 12 phút cần được đo thực tế, không phải ước tính.
>
> **Kết luận:** ⚠️ Tiềm năng nhưng cần thu hẹp scope — chỉ tóm tắt phần narrative/ghi chú tự do, thêm HITL bắt buộc.

### Card #5 — VinFast Phiếu lỗi xe
> **Điểm yếu phát hiện:**
> 1. OCR truyền thống + regex đủ để extract mã lỗi chuẩn hóa — không cần LLM.
> 2. Lỗi 12% có thể do quy trình, không phải do nhập liệu — cần phân tích root cause trước.
> 3. Chi phí xây AI có thể cao hơn lương nhân viên 1 năm nếu volume không đủ lớn.
>
> **Kết luận:** ❌ Hạ xuống Rule/OCR — dùng structured form + barcode/QR để loại nhập tay.

---

*Tác giả: Tô Huy Thông — Branch cá nhân: 2a202602608-thong*
