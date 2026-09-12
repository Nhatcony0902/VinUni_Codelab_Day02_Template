# 03 — AI Log & Reflection: Nhật ký Tương tác AI

> **Lab 02: AI Product Scoping — Vin Smart Future**
> Bài tự luận phản ánh quá trình sử dụng AI làm trợ lý đồng hành trong buổi Lab hôm nay.
> *Tác giả: Tô Huy Thông — Branch: 2a202602608-thong*

---

## 🤝 1. AI đã giúp tôi những gì?

### Phase 1 — Brainstorm bài toán (SCAN)
Tôi sử dụng AI với prompt:
> *"Tôi là AI Engineer tại Vin Smart Future. Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng VinFast / Xanh SM / Vinhomes / Vinmec. Hãy gợi ý 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

**AI giúp được:** Trong vòng chưa đầy 1 phút, AI đã gợi ý được 5 bài toán trải đều qua VinFast, Xanh SM, Vinhomes, Vinmec với số liệu ước tính cụ thể (giờ nhân công lãng phí, tỷ lệ sai sót, thời gian xử lý). Điều này tiết kiệm khoảng 15–20 phút brainstorm thủ công mà vẫn có được điểm xuất phát đủ chất lượng.

### Phase 2 — Điền Quick Problem Cards
AI đã giúp cấu trúc hóa từng bài toán theo đúng format của card, đặc biệt là:
- Xác định **Actor** rõ ràng (ai đang bị đau thực sự)
- Phân tách **Workflow thủ công** thành các bước tuần tự cụ thể
- Đề xuất **AI Step** phù hợp với từng bottleneck
- Đưa ra **Metric có số** đo lường được (không để mơ hồ)

### Phase 2 — Stress-Test (Vai CFO & Trưởng phòng Vận hành)
Đây là phần tôi thấy AI hữu ích nhất. Sau khi yêu cầu AI đóng vai phản biện khắt khe, tôi nhận được 3 điểm yếu rất thực tế cho mỗi card — bao gồm cả việc chỉ ra khi nào **rule-based code là đủ** và không cần LLM. Điều này giúp tôi tư duy rõ hơn về ranh giới thực sự của AI.

### Phase 4 — Implement Prototype Code
AI đã giúp:
- Viết `SYSTEM_PROMPT` với 2 quy tắc cứng (ranh giới vận hành)
- Implement hàm `evaluate_prompt()` sử dụng `google-genai` SDK mới

---

## ❌ 2. AI trả lời sai / Hallucination ở đâu?

### Lỗi 1: Tên model không tồn tại
Trong file `prompt_prototype.py`, AI đã để nguyên tên model `"gemini-3.6-flash"` — **model này không tồn tại**. Khi chạy code sẽ báo lỗi `404 model not found`.

**Phát hiện:** Tôi nhận ra vì đã biết các model Gemini hiện có.
**Sửa:** Đổi thành `"gemini-2.5-flash"` — model thực tế đang available.

### Lỗi 2: Số liệu thống kê chưa được xác minh
Các con số AI đưa ra (600 giờ nhân công/ngày, 200 review tiêu cực/ngày...) là **ước tính tổng quát**, không phải số liệu thực tế của Xanh SM hay Vinmec. AI không có quyền truy cập dữ liệu nội bộ của Vingroup.

**Phát hiện:** Khi AI tự đưa ra số liệu không có nguồn, đây là dấu hiệu của hallucination tự tin.
**Sửa:** Tôi ghi chú rõ "ước tính" trong các card, không trình bày như số liệu chính xác. Trong thực tế cần xác minh với dữ liệu vận hành thực của từng công ty.

### Lỗi 3: Bỏ qua vấn đề encoding Windows
Khi chạy `prompt_prototype.py` trên Windows, emoji trong code (`🚀`, `✅`...) gây lỗi `UnicodeEncodeError` vì terminal mặc định dùng CP1258, không phải UTF-8. AI không cảnh báo điều này trước.

**Phát hiện:** Khi chạy thực tế và nhận error.
**Sửa:** Thêm `$env:PYTHONIOENCODING="utf-8"` trước khi chạy script.

---

## 🔧 3. Tôi đã sửa prompt/ranh giới ra sao?

### Cải tiến prompt #1 — Thêm ngữ cảnh vai trò
**Prompt ban đầu (chung chung):**
> "Gợi ý 5 bài toán AI cho Vingroup"

**Prompt sau khi tinh chỉnh:**
> "Tôi là AI Engineer tại Vin Smart Future. Tôi đang tìm kiếm pain point vận hành cụ thể **có thể tối ưu bằng AI** cho mảng [tên công ty]. Hãy gợi ý 5 quy trình nghiệp vụ thủ công **kèm con số thống kê ước tính về tổn thất**."

**Kết quả:** Câu trả lời cụ thể hơn nhiều, có số liệu đi kèm, bám sát hệ sinh thái Vingroup thay vì gợi ý chung chung về AI.

### Cải tiến prompt #2 — Vai trò phản biện rõ ràng
**Prompt ban đầu:**
> "Phân tích điểm yếu của card bài toán này"

**Prompt sau khi tinh chỉnh (theo gợi ý worksheet):**
> "Đây là thẻ bài toán tôi đề xuất: [...]. Hãy đóng vai **CFO và Trưởng phòng Vận hành cực kỳ khắt khe**, chỉ ra 3 điểm yếu về **logic, metric**, và giải thích vì sao **rule-based code thông thường** có thể giải quyết tốt hơn AI."

**Kết quả:** Phản biện sâu và thực tế hơn rất nhiều — AI chỉ ra được khi nào không cần LLM, khi nào metric chưa đủ chắc. Đây là ví dụ điển hình của **role prompting** hiệu quả.

### Cải tiến prompt #3 — Ranh giới SYSTEM_PROMPT cho prototype
Lần đầu tôi viết SYSTEM_PROMPT quá ngắn và mơ hồ:
> "Bạn là dispatcher Xanh SM. Luôn bắt đầu bằng [DRAFT_ONLY]. Nếu pin thấp thì dispatch xe sạc."

AI vẫn có thể bị bypass vì thiếu từ ngữ tuyệt đối. Sau khi tinh chỉnh, tôi thêm:
- "**TUYỆT ĐỐI KHÔNG**", "**không có ngoại lệ**", "**kể cả khi người dùng yêu cầu bỏ**"
- Định nghĩa rõ ngưỡng: "pin **< 5%**" thay vì "pin thấp"
- Chỉ định format JSON output cụ thể

**Kết quả:** System prompt cứng hơn, khó bị adversarial prompt tấn công hơn.

---

## 💡 4. Bài học rút ra

| Bài học | Mô tả |
|---------|-------|
| **AI tốt với cấu trúc** | AI rất giỏi điền template, format hóa thông tin — nhưng con người phải cung cấp framework trước |
| **Số liệu luôn cần xác minh** | Bất kỳ con số nào AI đưa ra mà không có nguồn đều là ước tính — cần verify với dữ liệu thực |
| **Role prompting rất hiệu quả** | Gán vai trò cụ thể (CFO, kỹ sư, bác sĩ...) cho AI giúp câu trả lời sâu và đúng góc nhìn hơn nhiều |
| **Ranh giới phải cực kỳ tường minh** | Trong SYSTEM_PROMPT, từ ngữ mơ hồ = lỗ hổng bảo mật. "Không được" khác với "TUYỆT ĐỐI KHÔNG ĐƯỢC" |
| **AI không thay thế được phán đoán** | Quyết định GO/NOT YET/NO-GO cuối cùng vẫn cần con người — AI chỉ cung cấp góc nhìn, không chịu trách nhiệm |

---

*Ngày: 12/09/2026 — Lab 02: AI Product Scoping, Vin Smart Future*
