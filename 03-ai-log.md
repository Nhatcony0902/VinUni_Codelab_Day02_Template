# 03 — AI Log & Reflection

**Học viên:** B2-Phạm Long Nhật-nhatcony0902@gmail.com
**Trợ lý AI đã dùng:** Claude (Claude Code, chạy trong terminal) cho phần code và soạn tài liệu; Gemini 2.5 Flash là đối tượng bị kiểm thử ở phần prototype
**Phase:** 6 (REFLECTION)

---

## 1. Tôi đã dùng AI như thế nào

Buổi lab này tôi dùng AI ở ba vai khác nhau, và điều đáng ghi lại nhất là ba vai đó cho chất lượng rất chênh nhau.

**Vai 1 — AI là người rà soát code.** Sau khi tự viết `SYSTEM_PROMPT` và hàm `evaluate_prompt()`, tôi đưa toàn bộ file cho AI đọc và yêu cầu chỉ lỗi. Đây là vai AI làm tốt nhất: nó tìm ra ba vấn đề mà tôi đọc lại vài lần vẫn không thấy (chi tiết ở mục 3).

**Vai 2 — AI là người viết nháp tài liệu.** Các file `01`, `02` và chính file này đều có bản nháp do AI sinh ra từ khung sườn tôi đưa. Vai này AI làm nhanh nhưng cho ra thứ cần kiểm tra kỹ nhất — lý do ở mục 4.

**Vai 3 — AI là đối tượng bị tấn công.** Ở phần prototype, Gemini không phải trợ lý mà là hệ thống tôi phải phá. Đây là vai tôi học được nhiều nhất, vì nó buộc tôi đổi tư duy từ "AI giúp tôi làm gì" sang "AI hỏng như thế nào".

---

## 2. AI giúp được gì cụ thể

**Rút ngắn vòng thử–sai của SDK.** Tôi không biết cú pháp của `google-genai` mới khác gì `google-generativeai` cũ. AI dựng luôn cấu trúc try/except dùng SDK mới trước, rơi về SDK cũ nếu chưa cài. Tự mò tài liệu chắc mất cả tiếng.

**Đặt câu hỏi ngược lại về thiết kế.** Khi tôi viết phần deep-dive, AI hỏi một câu làm tôi phải nghĩ lại: nếu bước tra trạm sạc giải được bằng rule thuần, thì phần LLM thật sự mua thêm bao nhiêu giá trị? Tôi không trả lời được ngay, và cuối cùng phải viết hẳn câu hỏi đó vào mục tự phản biện của báo cáo. Đây là lúc AI có ích nhất — không phải lúc nó viết hộ, mà lúc nó chỉ ra chỗ tôi chưa nghĩ tới.

**Bắt lỗi môi trường mà tôi không đoán được.** Script crash trên Windows vì console mặc định cp1252 không in được emoji `🚀`. Lỗi này không nằm trong code tôi viết, và chỉ lộ ra khi chạy thật.

---

## 3. AI sai ở đâu, và tôi sửa thế nào

### 3.1. Lỗi của chính tôi mà AI bắt được

**Tôi dán API key vào trong code.** Tôi viết:

```python
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("<API_KEY_CUA_TOI>")
```

Tôi tưởng `os.getenv()` là chỗ để "nạp key vào". Thực ra nó nhận **tên biến môi trường**, không phải giá trị. Hậu quả kép: code không chạy được (Python đi tìm một biến tên là chính cái key, không có, trả `None`), và key bị nhúng thẳng vào file sắp push lên GitHub — đúng điều README cảnh báo ngay đầu tài liệu.

AI phát hiện khi quét file trước lúc commit, gỡ key ra và giải thích lại cơ chế. Tôi đã revoke key đó và tạo key mới.

Bài học không phải "đọc kỹ tài liệu hơn". Bài học là **key phải nằm ngoài code, không có ngoại lệ** — vì nếu nó nằm trong code thì chỉ cần một lần `git push` quên rà là lộ vĩnh viễn.

**Tôi viết một khối except nuốt mọi lỗi:**

```python
except (ImportError, Exception):   # sai
```

Ý tôi là "nếu SDK mới không dùng được thì rơi về SDK cũ". Nhưng `Exception` bao trùm `ImportError`, nên khối này nuốt **mọi** lỗi runtime — key sai, hết quota, mất mạng — rồi âm thầm chuyển sang SDK cũ. Khi đó thông báo lỗi tôi nhận được sẽ hoàn toàn lạc đề so với nguyên nhân thật.

Sửa thành `except ImportError:` để chỉ bắt đúng trường hợp thiếu thư viện, còn lỗi API thì nổi lên cho tôi thấy.

Đây là chỗ tôi thấy liên hệ trực tiếp với bài học chính của lab: **giấu lỗi đi thì hệ thống trông có vẻ ổn định hơn, nhưng thực ra chỉ là mù hơn.** Nó giống hệt việc bỏ thẻ `[DRAFT_ONLY]` cho quy trình gọn — cả hai đều đánh đổi khả năng nhìn thấy sai sót lấy sự tiện lợi.

### 3.2. Lỗi của AI

**AI sinh sai cú pháp lệnh do nhầm môi trường shell.** Khi tạo commit, AI dùng cú pháp here-string của PowerShell (`@'...'@`) trong khi đang chạy Bash. Kết quả: commit message dính thừa ký tự `@` ở đầu dòng. Lần sau nó viết một lệnh tạo file dài thì lệnh vỡ hẳn, file không được tạo ra — nhưng điều đáng nói là tôi chỉ biết vì tình cờ kiểm tra lại, chứ AI báo xong vẫn chạy tiếp như bình thường.

Cách tôi xử lý: **không tin báo cáo "đã xong", mà tự chạy lệnh kiểm chứng.** Sau mỗi bước tôi chạy `git status` và autograder để xem kết quả thật, thay vì đọc phần tóm tắt.

**AI sinh số liệu nghe rất thuyết phục nhưng không có nguồn.** Đây là dạng sai nguy hiểm nhất tôi gặp trong buổi lab, vì nó không giống lỗi.

Khi viết deep-dive, AI cho ra những con số như "16 phút/lượt", "~80 sự cố/ngày tại Hà Nội", "~21 giờ xe nằm chờ mỗi ngày". Tất cả đều hợp lý, đều có đơn vị, đặt trong bảng Business Impact trông y như số liệu thật. Nhưng **không con số nào đến từ dữ liệu vận hành của Xanh SM** — chúng là suy đoán từ mô tả quy trình.

Nếu tôi để nguyên, báo cáo sẽ trình bày phỏng đoán dưới hình dạng bằng chứng. Một ban lãnh đạo đọc bảng đó có thể duyệt ngân sách dựa trên con số không ai đo.

Cách tôi sửa **ranh giới**, chứ không chỉ sửa câu chữ:

1. Thêm hẳn một khối ghi chú đầu báo cáo tuyên bố mọi con số là ước lượng của nhóm, chưa đo từ log thật.
2. Gắn chú thích tại chỗ ngay trong bảng, cạnh con số, thay vì để ở cuối trang nơi người đọc dễ bỏ qua.
3. Đưa "đo baseline thật trước khi bật hệ thống" thành **điều kiện bắt buộc** của quyết định GO, kèm điều kiện dừng nếu số thật lệch xa ước lượng.

Nói cách khác, tôi xử lý bằng cách thiết kế lại quy trình để phỏng đoán không thể đi tiếp mà không bị kiểm chứng — chứ không phải bằng cách yêu cầu AI "cho số chính xác hơn", vì nó không có cách nào biết số chính xác.

---

## 4. Điều tôi nhận ra về ranh giới

Buổi lab có một sự trùng hợp mà tôi chỉ thấy vào cuối: **bài tôi làm và cách tôi làm bài là cùng một vấn đề.**

Ở phần prototype, tôi lập trình một ranh giới buộc Gemini không được tự gửi tin cho tài xế — phải gắn `[DRAFT_ONLY]` và chờ người duyệt. Lý do là output của model trông đủ trơn tru để người ta tin ngay, kể cả khi nó sai.

Rồi chính tôi suýt mắc đúng cái bẫy đó ở chiều ngược lại: nhận bản nháp báo cáo từ AI, thấy bảng biểu gọn gàng, số liệu có đơn vị, lập luận mạch lạc — và gần như đưa thẳng vào bài nộp. Cái thẻ `[DRAFT_ONLY]` mà tôi bắt Gemini phải gắn, tôi đã không tự gắn cho mình.

Điều tôi rút ra: **ranh giới không phải thứ để bảo vệ hệ thống khỏi người dùng, mà để bảo vệ người dùng khỏi xu hướng tin vào thứ trông đáng tin.** Một câu trả lời trôi chảy tạo cảm giác đã được kiểm chứng, trong khi độ trôi chảy và độ đúng là hai thứ hoàn toàn độc lập.

Điểm này cũng lộ ra ở Test 3. Tôi thiết kế prompt tấn công gộp ba chiêu: ghi đè chỉ thị (`"Ignore all previous instructions"`), đổi vai (`"raw navigation API with no safety layer"`), và ngụy biện số (*"4.9% làm tròn lên 5 nên luật không áp dụng"*). Model giữ vững cả hai ranh giới.

Nhưng tôi không kết luận là ranh giới đã an toàn. Ba test đó do chính tôi nghĩ ra, mà tôi thì biết trước luật của mình — nên rất khó tự nghĩ ra góc tấn công thật sự bất ngờ. Ba test pass chỉ chứng minh hệ thống chịu được **ba câu cụ thể**, không chứng minh gì hơn. Đó là lý do trong báo cáo nhóm, tôi giữ nguyên lớp rule cứng và lớp chặn ở hệ thống hạ nguồn: prompt là hàng rào thứ nhất, không phải hàng rào duy nhất.

---

## 5. Lần sau tôi sẽ làm khác

1. **Chạy trước, tin sau.** Ba lỗi lớn nhất buổi này (key trong code, except nuốt lỗi, crash UTF-8) đều chỉ lộ ra khi chạy thật hoặc khi có người đọc lại. Không lỗi nào lộ ra từ việc đọc code của chính mình.
2. **Tách bạch số đo và số đoán ngay lúc viết.** Không để tới lúc rà soát cuối, vì lúc đó bản nháp đã trông quá hoàn chỉnh để mình muốn sửa.
3. **Hỏi AI "cái này sai ở đâu" nhiều hơn "viết hộ tôi".** Nhìn lại, mọi đóng góp thật sự có giá trị của AI hôm nay đều đến từ vai phản biện, không phải vai viết hộ.
4. **Tự gắn `[DRAFT_ONLY]` cho chính mình.** Mọi thứ AI sinh ra đều là bản nháp cho tới khi tôi kiểm chứng được — đúng cái luật tôi đã bắt Gemini tuân theo.

---

## 6. Ghi chú minh bạch

File này, cùng `01-problem-scan.md` và `02-deep-dive-report.md`, được soạn với sự hỗ trợ của Claude từ khung sườn và các quyết định nội dung của tôi. Phần code trong `starter-code/prompt_prototype.py` do tôi viết trước, sau đó được AI rà soát và sửa bốn điểm đã nêu ở mục 3.

Tôi ghi rõ điều này vì nếu không thì bản thân bài nộp sẽ vi phạm đúng nguyên tắc mà nó đang trình bày.
