# 🔍 01-problem-scan.md — Problem Scan & Quick Cards (Vin Smart Future)

> **Dự án:** Vin Smart Future — AI Product Scoping Lab 02  
> **Thành viên thực hiện:** Team AI Product Engineers (Vin Smart Future)  
> **Mảng tập trung:** Xanh SM (GSM), VinFast, Vinhomes, Vinmec, Vinpearl  

---

# 🚀 Phase 1 — SCAN: Quét cơ hội bài toán AI tại Vingroup

Sử dụng **4 Lenses** (Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain) để phân tích hoạt động vận hành tại các đơn vị thành viên:

| # | Subsidiary | Lens | Mô tả ngắn bài toán & Pain point hiện tại |
|---|------------|------|-------------------------------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian / Pain | Điều phối viên xử lý thủ công các cuộc gọi sự cố cạn pin/sạc pin thực địa của tài xế taxi điện, tra cứu trụ sạc trống và vị trí GPS (mất 12-15 min/lượt). |
| 2 | **VinFast** | Lặp lại | So khớp đối chiếu hóa đơn điện tiêu thụ và dữ liệu giao dịch sạc pin của khách hàng tại các trạm sạc đối tác hằng tuần. |
| 3 | **Vinhomes** | AI-upgrade | Phân loại tự động và gợi ý phản hồi cho các khiếu nại/yêu cầu sửa chữa của cư dân trên App Vinhomes Resident (hiện mất 8-12h xử lý thủ công). |
| 4 | **Vinmec** | Time-consuming | Tóm tắt tự động hồ sơ bệnh án và lịch sử xét nghiệm để hỗ trợ bác sĩ soạn giấy xuất viện (hiện mất 20-30 phút/bệnh nhân). |
| 5 | **VinWonders** | AI-upgrade | Trợ lý tư vấn lịch trình tham quan tự động dựa trên thời gian thực, thời tiết và độ dài hàng chờ tại các trò chơi. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

## 🎴 CARD #1 — Xanh SM: Xử lý sự cố cạn pin & Điều phối cứu hộ thực địa (ĐƯỢC CHỌN)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Hỗ trợ điều phối viên Xanh SM tra cứu vị   │
│ trí, trạm sạc VinFast khả dụng và tự động draft chỉ dẫn     │
│ cứu hộ pin cho tài xế taxi điện khi gặp sự cố trên đường.   │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Tài xế taxi (chờ đợi),                 │
│                      Điều phối viên Trung tâm (quá tải)     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo cạn pin               │
│   ──> 2. Điều phối viên tra cứu vị trí GPS xe trên bản đồ   │
│   ──> 3. Tra cứu thủ công các trạm sạc VinFast còn trụ trống │
│   ──> 4. Soạn tin nhắn hướng dẫn/đường đi gửi cho tài xế    │
│   ──> 5. Liên hệ xe sạc pin di động (Mobile Charger) nếu cần│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 10 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4             │
│ (AI Auto-pull vị trí + gợi ý trạm + Draft tin nhắn chỉ dẫn) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm tổng thời gian xử lý sự cố từ 15 min ──> under 3 min.│
│                                                             │
│ Quick Architecture: [x] LLM Feature (Co-pilot với HITL)     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎴 CARD #2 — Vinhomes: Trợ lý AI Phân loại & Route Khiếu nại Cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại, trích xuất thực thể   │
│ và soạn bản thảo phản hồi khiếu nại cư dân Vinhomes.        │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Cư dân (chờ lâu), Ban Quản lý (quá tải) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản hồi trên app                           │
│   ──> 2. Nhân viên CSKH đọc và phân loại phòng ban         │
│   ──> 3. Chuyển tiếp ticket cho bộ phận kỹ thuật/vận hành  │
│   ──> 4. Soạn phản hồi cho cư dân                           │
│   ⏱ Thời gian xử lý: 8 - 12 giờ/ticket                      │
│                                                             │
│ AI nhảy vào bước nào? Bước 2 & 4                             │
│ Đo thành công bằng gì? Giảm thời gian phản hồi từ 12h down 1h │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎴 CARD #3 — Vinmec: Tóm tắt Hồ sơ Bệnh án & Giấy Xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Trợ lý AI tổng hợp dữ liệu lâm sàng và    │
│ tóm tắt hồ sơ xuất viện cho bác sĩ Vinmec.                  │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ (tốn thời gian hành chính)      │
│ Workflow thủ công: Đọc lại toàn bộ lịch sử khám -> Soạn tóm  │
│ tắt xuất viện (⏱ 25 phút/bệnh nhân).                        │
│ AI nhảy vào bước nào? Tóm tắt tự động hồ sơ lâm sàng.       │
│ Đo thành công bằng gì? Giảm thời gian soạn từ 25 min ──> 5 min│
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```
