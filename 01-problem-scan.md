# 01 — Problem Scan & Quick Cards

**Học viên:** Phạm Long Nhất
**Vai trò:** AI Product Engineer — Vin Smart Future (Vingroup)
**Mảng tập trung:** Y tế & Giáo dục (Vinmec / VinUni)
**Phase:** 1 (SCAN) + 2 (QUICK-ASSESS)

---

# 🔍 Phase 1 — SCAN: List bài toán của tôi

Quét hoạt động vận hành của Vinmec và VinUni qua 4 lenses. Các con số bên dưới là **ước lượng của tôi** dựa trên quan sát thực tế và mô tả quy trình công khai — cần đối chiếu lại với log vận hành thật trước khi đưa vào kế hoạch đầu tư.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | **Vinmec** | Tốn thời gian | **Soạn tóm tắt hồ sơ xuất viện (Discharge Summary).** Bác sĩ phải đọc rải rác bệnh án điện tử, kết quả xét nghiệm, ghi chú điều dưỡng rồi tự viết lại bản tóm tắt bằng ngôn ngữ bệnh nhân hiểu được. Ước tính 20–30 phút/ca, thường bị dồn vào cuối ca trực. |
| 2 | **Vinmec** | Pain từ người khác | **Phân luồng chuyên khoa khi đặt lịch khám.** Khách mô tả triệu chứng bằng lời thường ngày ("tức ngực, khó thở khi leo cầu thang"), tổng đài viên phải tự đoán Tim mạch hay Hô hấp. Đặt sai khoa buộc bệnh nhân khám lại, mất thêm một lượt chờ. |
| 3 | **VinUni** | Lặp lại | **Phản hồi bài lab lập trình.** Autograder chỉ trả về pass/fail. Trợ giảng phải tự đọc code từng sinh viên để giải thích sai ở đâu, lặp lại gần như nguyên văn cho những lỗi phổ biến giống nhau. |
| 4 | **Vinmec** | Lặp lại | **Đối chiếu hồ sơ thanh toán bảo hiểm.** Nhân viên so tay giữa chỉ định điều trị và danh mục chi trả của từng hãng bảo hiểm. Sai sót khiến hồ sơ bị trả về, kéo dài chu kỳ thu tiền. |
| 5 | **VinUni** | AI có thể tốt hơn | **Trả lời câu hỏi hành chính của sinh viên.** Câu hỏi về hạn đăng ký môn, quy định điểm danh, thủ tục xin giấy xác nhận lặp lại mỗi kỳ. Email phòng đào tạo trả lời chậm, sinh viên hỏi lại nhiều lần. |

> **Nhận xét sau khi quét:** cả 5 bài toán đều là *xử lý ngôn ngữ trên dữ liệu đã có*, không bài nào đòi mô hình chẩn đoán. Đây là vùng an toàn để đưa LLM vào, vì ranh giới "AI không được ra quyết định y khoa" có thể giữ vững mà vẫn còn đủ giá trị.

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn 3 bài toán tiềm năng nhất: #1, #2, #3.

---

## QUICK PROBLEM CARD #1

**Bài toán (1 câu):** Bác sĩ Vinmec mất 20–30 phút mỗi ca để tự tay soạn bản tóm tắt xuất viện từ dữ liệu nằm rải rác trong bệnh án điện tử.

**Công ty thành viên:** [x] Vinmec

**Ai đang đau (Actor)?** Bác sĩ điều trị nội trú — người ký tên chịu trách nhiệm trên bản tóm tắt. Người đau thứ hai là bệnh nhân, phải chờ xuất viện lâu hơn.

**Workflow thủ công hiện tại:**
```
1. Mở bệnh án điện tử, đọc diễn biến từng ngày
   ──> 2. Tra kết quả xét nghiệm / chẩn đoán hình ảnh ở phân hệ khác
   ──> 3. Đọc ghi chú điều dưỡng để nắm diễn biến ngoài giờ
   ──> 4. Gõ tay bản tóm tắt, diễn giải thuật ngữ y khoa sang lời dễ hiểu
   ──> 5. Tự đọc soát lại rồi ký
```

**Bước nào tốn thời gian/lỗi nhất?** Bước 4 — soạn và diễn giải (⏱ **15–20 phút/lượt**, chiếm phần lớn tổng thời gian). Bước 1–3 tốn thêm khoảng 8 phút chỉ để gom dữ liệu.

**AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 1–4: đọc toàn bộ hồ sơ, trích xuất mốc điều trị, sinh **bản nháp** tóm tắt theo mẫu chuẩn của Vinmec. Bước 5 giữ nguyên cho bác sĩ — đây là chốt chặn Human-in-the-loop.

**Đo thành công bằng gì (Metric có số)?** Giảm thời gian soạn tóm tắt xuất viện từ **25 phút → dưới 8 phút/ca**, trong đó bác sĩ chỉ còn đọc soát và sửa. Đồng thời **100% bản nháp phải được bác sĩ ký duyệt** trước khi vào hồ sơ chính thức — không có ngoại lệ.

**Quick Architecture:** [x] LLM

---

## QUICK PROBLEM CARD #2

**Bài toán (1 câu):** Tổng đài Vinmec phải tự suy đoán chuyên khoa từ mô tả triệu chứng bằng lời thường ngày của khách, đặt sai khoa khiến bệnh nhân phải khám lại từ đầu.

**Công ty thành viên:** [x] Vinmec

**Ai đang đau (Actor)?** Tổng đài viên đặt lịch (không có chuyên môn y khoa sâu). Bệnh nhân gánh hậu quả trực tiếp khi bị xếp sai khoa.

**Workflow thủ công hiện tại:**
```
1. Khách gọi/chat mô tả triệu chứng bằng lời thường ngày
   ──> 2. Tổng đài viên tra bảng tham chiếu triệu chứng ──> chuyên khoa
   ──> 3. Trường hợp mơ hồ thì hỏi lại khách hoặc hỏi điều dưỡng trực
   ──> 4. Chốt lịch, gửi xác nhận
```

**Bước nào tốn thời gian/lỗi nhất?** Bước 2–3 — phân loại triệu chứng (⏱ **3–5 phút/cuộc**, các ca mơ hồ kéo dài hơn). Đây cũng là bước sinh lỗi: triệu chứng chồng lấn giữa nhiều khoa.

**AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2: gợi ý **top 2 chuyên khoa kèm độ tin cậy** cho tổng đài viên tham khảo. AI **không** được tự chốt lịch, và phải chuyển ngay sang người thật khi gặp dấu hiệu cấp cứu (đau ngực dữ dội, khó thở cấp, chảy máu không cầm).

**Đo thành công bằng gì (Metric có số)?** Giảm tỷ lệ đặt sai chuyên khoa từ mức nền hiện tại xuống **dưới 5%**, và rút thời gian phân loại từ 4 phút → **dưới 1 phút/cuộc**. Cần đo baseline thật trước khi chốt con số cam kết.

**Quick Architecture:** [x] LLM

---

## QUICK PROBLEM CARD #3

**Bài toán (1 câu):** Autograder của VinUni chỉ trả pass/fail, nên trợ giảng phải đọc tay code từng sinh viên và gõ lại gần như cùng một lời giải thích cho các lỗi phổ biến.

**Công ty thành viên:** [x] Khác — **VinUni**

**Ai đang đau (Actor)?** Trợ giảng (TA) của môn lập trình. Sinh viên đau gián tiếp: nhận kết quả "Failed" mà không biết sai ở đâu, phải chờ tới buổi sau mới được giải đáp.

**Workflow thủ công hiện tại:**
```
1. Autograder chạy test, trả về pass/fail
   ──> 2. TA mở code của từng sinh viên fail
   ──> 3. TA đọc, xác định lỗi cú pháp/logic
   ──> 4. TA gõ phản hồi giải thích, thường lặp lại cho nhiều bạn cùng lỗi
```

**Bước nào tốn thời gian/lỗi nhất?** Bước 3–4 (⏱ **5–8 phút/bài**). Với lớp 60 sinh viên và tỷ lệ fail khoảng 30%, riêng vòng phản hồi đã ngốn gần **2 giờ mỗi bài lab**.

**AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 3–4: đọc code + log lỗi, sinh **nháp phản hồi mang tính gợi mở** (chỉ ra vùng code có vấn đề và đặt câu hỏi dẫn dắt). Ranh giới bắt buộc: **không được đưa code lời giải hoàn chỉnh** — làm vậy là phá mục tiêu sư phạm. TA duyệt trước khi gửi.

**Đo thành công bằng gì (Metric có số)?** Giảm thời gian TA xử lý phản hồi từ **2 giờ → dưới 40 phút/bài lab**, với **ít nhất 80% bản nháp được TA duyệt mà chỉ cần sửa nhẹ**.

**Quick Architecture:** [x] LLM

---

# 🎯 Đề xuất bài toán mang ra thảo luận nhóm

Tôi đề xuất **Card #1 — Tóm tắt hồ sơ xuất viện Vinmec** cho phần Deep-Dive của nhóm, vì ba lý do:

1. **Tác động đo được rõ nhất.** Tiết kiệm ~17 phút × số ca xuất viện mỗi ngày là con số quy đổi thẳng ra giờ công bác sĩ, dễ thuyết phục ban lãnh đạo hơn hai card còn lại.
2. **Ranh giới an toàn vẽ được dứt khoát.** AI chỉ đọc và soạn nháp, bác sĩ ký duyệt. Không có đường nào để AI tự ý đẩy thông tin tới bệnh nhân — đúng tinh thần ranh giới `[DRAFT_ONLY]` mà tôi đã lập trình và stress-test ở phần prototype.
3. **Dữ liệu đã sẵn có.** Bệnh án điện tử vốn đã được số hóa, không cần dự án thu thập dữ liệu mới trước khi làm được prototype.

**Điểm yếu cần nhóm phản biện:** dữ liệu bệnh án là dữ liệu nhạy cảm bậc nhất. Trước khi nói tới mô hình, phải trả lời được câu hỏi dữ liệu rời khỏi hạ tầng Vinmec hay không, và nếu không thì phương án self-hosted có khả thi về chi phí không. Nếu câu trả lời là không, bài toán này phải xuống **NOT YET** bất kể giá trị nghiệp vụ lớn tới đâu.
