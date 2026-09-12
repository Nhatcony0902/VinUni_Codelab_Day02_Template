# 02 — Deep Dive Report: AI Product Scoping (Vin Smart Future)

> **Mảng kinh doanh lựa chọn: Vinmec — Tóm tắt hồ sơ bệnh án tự động bằng AI trước khám tái khám.**
> *Tác giả: Tô Huy Thông — Branch: 2a202602608-thong*

---

## 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Thông**, AI Engineer tại **Vin Smart Future**. Nhóm chúng tôi được giao nhiệm vụ phối hợp với Khối Vận hành Lâm sàng của **Vinmec International Hospital** để tìm kiếm các cơ hội tối ưu hóa quy trình bằng AI.

Qua khảo sát thực tế tại phòng khám chuyên khoa Vinmec Times City, tôi nhận thấy các bác sĩ đang mất một lượng thời gian đáng kể để đọc lại toàn bộ hồ sơ bệnh án dài của bệnh nhân tái khám trước khi bắt đầu khám — một tác vụ lặp đi lặp lại, tốn thời gian và hoàn toàn có thể được AI hỗ trợ.

---

## 🗳️ Quyết định lựa chọn bài toán

Nhóm quyết định chọn bài toán **"Vinmec — AI tóm tắt hồ sơ bệnh án tự động trước khám tái khám"** vì:
- Bottleneck rõ ràng, đo được (10–15 phút/bệnh nhân)
- Rủi ro ở mức kiểm soát được nếu có HITL bắt buộc
- Tác động trực tiếp đến throughput và trải nghiệm bác sĩ/bệnh nhân

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm)

## 3.1. Current-State Workflow

Quy trình tái khám hiện tại tại Vinmec trước khi có AI:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Bệnh nhân    │     │ Lễ tân tra   │     │ Bác sĩ mở    │     │ Bác sĩ đọc   │
│ đến đăng ký  │ ──→ │ hệ thống HIS │ ──→ │ hồ sơ bệnh  │ ──→ │ lại toàn bộ  │
│ tái khám     │     │ gọi hồ sơ   │     │ án trên màn  │     │ lịch sử bệnh │
│              │ 🔄  │ bệnh nhân   │     │ hình máy tính│     │ án thủ công  │
│ Ai: Lễ tân  │     │ Ai: Lễ tân  │     │ Ai: Bác sĩ  │     │ Ai: Bác sĩ  │
│ ⏱ 3 phút    │     │ ⏱ 2 phút    │     │ ⏱ 1 phút    │     │ ⏱ 12 phút 🔴│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Bác sĩ bắt  │
                                                               │ đầu hỏi khám│
                                                               │ và chẩn đoán │
                                                               │ Ai: Bác sĩ  │
                                                               │ ⏱ 15 phút   │
                                                               └──────────────┘

🔄 = Handoff (chuyển giao thông tin giữa bộ phận)
🔴 = Bottleneck chính (bước tốn thời gian và có thể tối ưu bằng AI)
⏱ Tổng thời gian trước khi khám: ~18 phút/bệnh nhân (bước 1–4)
```

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung chi tiết |
|-------|-------------------|
| **1. Actor / Operator** | Bác sĩ chuyên khoa Vinmec (nội khoa, tim mạch, nhi khoa...) — người trực tiếp thực hiện tái khám cho bệnh nhân. |
| **2. Current Workflow** | Khi bệnh nhân tái khám đến, lễ tân gọi hồ sơ bệnh án từ hệ thống HIS (Hospital Information System). Bác sĩ phải tự đọc lại toàn bộ hồ sơ — bao gồm lịch sử chẩn đoán, đơn thuốc cũ, kết quả xét nghiệm, ghi chú lâm sàng tự do — hoàn toàn thủ công, mất trung bình 10–15 phút/bệnh nhân trước mỗi ca khám. |
| **3. Bottleneck** | Bước đọc hồ sơ thủ công (Bước 4): Hồ sơ bệnh nhân tái khám nhiều lần dài 10–30 trang, bác sĩ phải tự lọc thông tin quan trọng trong khối văn bản lớn gồm cả structured data (xét nghiệm) lẫn unstructured data (ghi chú tự do). Không có công cụ tóm tắt tự động. |
| **4. Business Impact** | Mỗi bác sĩ Vinmec khám trung bình 20–30 bệnh nhân tái khám/ngày. 12 phút/bệnh nhân × 25 bệnh nhân = **300 phút (5 giờ) đọc hồ sơ/bác sĩ/ngày** — chiếm 40% ca làm việc. Nếu AI giảm còn 2 phút/hồ sơ → tiết kiệm ~250 phút/bác sĩ/ngày, tương đương phục vụ thêm **8–10 bệnh nhân/ngày/bác sĩ**. |
| **5. Success Metric** | 1. Giảm thời gian bác sĩ đọc hồ sơ từ 12 phút → **dưới 2 phút/bệnh nhân** (đo qua HIS log timestamps). 2. **Tỷ lệ tóm tắt được bác sĩ xác nhận là "đủ thông tin"** đạt ≥ 92% (đo qua nút HITL "Xác nhận / Xem lại đầy đủ" trên giao diện). |
| **6. Operational Boundary** | **AI được phép:** Đọc hồ sơ từ HIS, tóm tắt lịch sử chẩn đoán, thuốc đang dùng, dị ứng, kết quả xét nghiệm quan trọng thành bản tóm tắt 1 trang. **TUYỆT ĐỐI KHÔNG:** Tự ý thay đổi chẩn đoán, đề xuất phác đồ điều trị, hoặc ẩn/xóa bất kỳ thông tin nào trong hồ sơ gốc. Bác sĩ **bắt buộc phải xác nhận** (HITL) trước khi bắt đầu khám. |

---

## 3.3. Future-State Flow & AI Fit

**AI Fit:** Chọn **LLM Feature** — không cần Agentic Loop vì quy trình có cấu trúc cố định, đầu vào là hồ sơ bệnh án từ HIS, đầu ra là bản tóm tắt cho bác sĩ review.

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3 🔵    │     │ Bước 4 🟢    │
│ Bệnh nhân    │     │ HIS tự động  │     │ AI đọc hồ sơ │     │ Bác sĩ review│
│ đăng ký tái  │ ──→ │ trigger pull │ ──→ │ & generate   │ ──→ │ tóm tắt AI  │
│ khám & xếp  │     │ hồ sơ bệnh  │     │ tóm tắt 1    │     │ (click Xác  │
│ hàng chờ    │     │ nhân        │     │ trang        │     │ nhận / Xem  │
│              │     │              │     │              │     │ đầy đủ)     │
│ ⏱ 3 phút    │     │ ⏱ <1 phút   │     │ ⏱ <1 phút 🔵│     │ ⏱ 1–2 phút 🟢│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Bác sĩ bắt  │
                                                               │ đầu khám với │
                                                               │ tóm tắt đã  │
                                                               │ được xác nhận│
                                                               │ ⏱ 15 phút   │
                                                               └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu bác sĩ click
                                                               "Xem lại đầy đủ",
                                                               mở hồ sơ gốc HIS
                                                               như workflow cũ.
                                                               AI không can thiệp.

🔵 = AI Step (LLM xử lý)
🟢 = Human Step — HITL bắt buộc (Bác sĩ phê duyệt trước khi khám)
↩️  = Fallback khi AI tóm tắt không đủ thông tin
```

**Nội dung AI tóm tắt (output format chuẩn):**
```
[TÓM TẮT HỒ SƠ — AI DRAFT — CHỜ BÁC SĨ XÁC NHẬN]
Bệnh nhân: [Họ tên] | Tuổi: [X] | Giới: [Nam/Nữ]
────────────────────────────────────
Chẩn đoán gần nhất: [...]  (Lần khám: DD/MM/YYYY)
Thuốc đang dùng: [Danh sách thuốc + liều lượng]
Dị ứng đã ghi nhận: [...]
Kết quả xét nghiệm đáng chú ý: [...]
Ghi chú lâm sàng lần trước: [...]
────────────────────────────────────
[XÁC NHẬN] [XEM HỒ SƠ ĐẦY ĐỦ]
```

---

# 🏁 Phase 5 — EVALUATE

## AI Readiness Checklist

| # | Tiêu chí | Đánh giá |
|---|----------|----------|
| 1 | Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? | ✅ **Có** — Vinmec vận hành HIS đã nhiều năm, hồ sơ bệnh án được số hóa đầy đủ. |
| 2 | Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? | ✅ **Có** — Bác sĩ bắt buộc xác nhận trước khi dùng tóm tắt. Hồ sơ gốc luôn sẵn có qua nút Fallback. |
| 3 | Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? | ⚠️ **Cần xác nhận** — Bác sĩ cần được training và thử nghiệm pilot để xây dựng niềm tin vào AI tóm tắt y tế. |

## Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

**[x] NOT YET — Cần tích lũy thêm dữ liệu / xác lập baseline trước khi triển khai rộng.**

> **Justification (Lý giải quyết định):**
>
> Bài toán có tiềm năng ROI cao và bộ dữ liệu HIS đủ để train/test. Tuy nhiên, có 2 rào cản chưa vượt qua:
>
> **1. Chưa có baseline đo đạc chính xác:** Con số "12 phút/bệnh nhân" hiện là ước tính — cần đo đạc thực tế bằng HIS log timestamps trong 30 ngày để có số chính xác trước khi tuyên bố ROI.
>
> **2. Rủi ro pháp lý y tế chưa được đánh giá đầy đủ:** Việc AI can thiệp vào quy trình lâm sàng cần được phòng Pháp chế Vinmec review về tuân thủ quy định Bộ Y tế và tiêu chuẩn JCI (Joint Commission International) của bệnh viện.
>
> **Bước tiếp theo đề xuất:**
> - Chạy pilot 30 ngày tại 1 phòng khám chuyên khoa (VD: Nội tổng quát) với 3–5 bác sĩ tình nguyện.
> - Thu thập feedback bác sĩ và đo tỷ lệ "Xác nhận" vs "Xem lại đầy đủ" để validate chất lượng tóm tắt.
> - Sau pilot: đánh giá lại để quyết định GO chính thức.

---

*Ngày: 12/09/2026 — Lab 02: AI Product Scoping, Vin Smart Future*
