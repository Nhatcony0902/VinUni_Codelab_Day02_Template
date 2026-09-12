# Lab 02 - Problem Scan

## Phase 1 - SCAN

### Context

I act as an AI Product Engineer at Vin Smart Future.
The goal is to identify operational bottlenecks across Vingroup
subsidiaries where AI, rules, or workflow automation may create
measurable value.


## Problem Scan

| # | Subsidiary | Lens | Problem |
|---|---|---|---|
| 1 | Xanh SM | Repetitive | Điều phối lại chuyến khi khách hàng thay đổi điểm đón/trả, khiến dispatcher phải kiểm tra và phân bổ lại chuyến thủ công. |
| 2 | Xanh SM | Time-consuming | Xử lý sự cố xe hết pin giữa đường, dispatcher phải tra cứu vị trí xe, tìm trạm sạc phù hợp và hướng dẫn tài xế. |
| 3 | VinFast | Repetitive | Đối chiếu hóa đơn sạc điện với dữ liệu trạm sạc đối tác để phát hiện sai lệch. |
| 4 | Vinhomes | AI-upgrade | Phân loại và chuyển khiếu nại của cư dân đến đúng bộ phận xử lý. |
| 5 | Vinmec | Stakeholder Pain | Bác sĩ mất nhiều thời gian tạo bản tóm tắt hồ sơ xuất viện từ nhiều thông tin trong bệnh án. |

## Initial Observation

Trong 5 bài toán trên, bài toán Xanh SM về xử lý sự cố sạc có
bottleneck rõ ràng, workflow dễ mô hình hóa và có thể đo thời gian
xử lý trước và sau khi áp dụng AI.

Bài toán này cũng có ranh giới an toàn rõ ràng:
AI có thể hỗ trợ tra cứu và tạo draft hướng dẫn nhưng không nên tự
thực hiện hành động vận hành quan trọng mà không có người điều phối
review.


#2 Xanh SM - Sự cố sạc
#4 Vinhomes - Khiếu nại cư dân
#5 Vinmec - Tóm tắt hồ sơ


# Phase 2 - Quick Problem Cards

## Quick Problem Card #1

### Problem

Tài xế Xanh SM gặp sự cố hết pin giữa đường và cần được
hướng dẫn đến trạm sạc phù hợp hoặc điều phối hỗ trợ.

### Company

Xanh SM (GSM)

### Actor

- Driver
- Dispatcher
- Mobile charging / rescue team

### Current Workflow

1. Driver gọi hoặc gửi thông báo sự cố.
2. Dispatcher kiểm tra vị trí xe.
3. Dispatcher tra cứu các trạm sạc gần đó.
4. Dispatcher kiểm tra khả năng đáp ứng.
5. Dispatcher gửi hướng dẫn cho tài xế hoặc điều phối cứu hộ.

### Bottleneck

Bước tra cứu trạm sạc và soạn hướng dẫn mất nhiều thời gian,
đặc biệt trong giờ cao điểm.

Estimated processing time:

15 phút/lượt.

### AI Opportunity

AI hỗ trợ dispatcher:

- đọc thông tin sự cố;
- tổng hợp trạng thái xe;
- tạo draft hướng dẫn;
- phát hiện trường hợp pin quá thấp cần cứu hộ/mobile charger.

### Success Metric

Giảm thời gian xử lý sự cố từ khoảng 15 phút xuống dưới 3 phút/lượt.

### Quick Architecture

LLM Feature + Rule-based safety logic.

### Human Oversight

Dispatcher phải review trước khi hướng dẫn được gửi cho tài xế.


## Quick Problem Card #2

### Problem

Khiếu nại của cư dân Vinhomes cần được phân loại và chuyển
đến đúng bộ phận xử lý nhanh chóng.

### Company

Vinhomes

### Actor

- Resident
- Customer Service
- Maintenance / Security / Operations teams

### Current Workflow

1. Cư dân gửi khiếu nại.
2. CSKH đọc nội dung.
3. CSKH xác định loại vấn đề.
4. CSKH chọn bộ phận xử lý.
5. CSKH chuyển ticket.

### Bottleneck

Đọc và phân loại nội dung khiếu nại bằng tay.

Estimated processing time:

Khoảng 5 phút/ticket.

### AI Opportunity

LLM phân tích nội dung khiếu nại và đề xuất:

- category;
- severity;
- responsible department;
- summary.

### Success Metric

Ít nhất 90% ticket được phân loại đúng và thời gian phân loại
giảm từ khoảng 5 phút xuống dưới 1 phút.

### Quick Architecture

LLM Feature.

### Human Oversight

CSKH review category và department trước khi ticket được route.