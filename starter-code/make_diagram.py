"""Dung so do Current-State Workflow (Phase 3.1) ra file PNG."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

# Font ho tro tieng Viet tren Windows
plt.rcParams["font.family"] = ["Segoe UI", "Arial", "DejaVu Sans"]

INK = "#1a2332"
MUTED = "#5b6b7f"
BOX = "#ffffff"
EDGE = "#c3ccd8"
RED = "#c0392b"
RED_BG = "#fdf0ee"
AMBER = "#b8860b"
BLUE_BG = "#eef4fb"
LANE_BG = "#f7f9fc"

fig, ax = plt.subplots(figsize=(17, 9.5))
ax.set_xlim(0, 17)
ax.set_ylim(0, 9.5)
ax.axis("off")
fig.patch.set_facecolor("white")

# ---------------------------------------------------------------- Tieu de
ax.text(0.4, 9.05, "CURRENT-STATE WORKFLOW", fontsize=20, fontweight="bold", color=INK)
ax.text(0.4, 8.62,
        "Xanh SM — Xử lý sự cố pin khẩn cấp & điều phối trạm sạc thực địa",
        fontsize=12.5, color=MUTED)
ax.plot([0.4, 16.6], [8.38, 8.38], color=EDGE, lw=1.2)

# ---------------------------------------------------------------- Lane 1
ax.add_patch(Rectangle((0.4, 4.35), 16.2, 3.65, facecolor=LANE_BG,
                       edgecolor=EDGE, lw=1, zorder=0))
ax.text(0.65, 7.72, "LÀN ĐIỀU PHỐI VIÊN  (Dispatcher)",
        fontsize=11.5, fontweight="bold", color=INK)

steps = [
    dict(n="Bước 1", title="Nhận báo sự cố\nqua hotline / app",
         t="2 phút", inp="Lời kể tài xế", out="Log sự cố", hot=False),
    dict(n="Bước 2", title="Tra định vị GPS xe\ntrên bản đồ nội bộ",
         t="2 phút", inp="Biển số xe", out="Toạ độ", hot=False),
    dict(n="Bước 3", title="Tra dashboard trạm\nsạc còn trụ trống",
         t="5 phút", inp="Toạ độ + dòng xe", out="DS trạm", hot=True),
    dict(n="Bước 4", title="Quyết định: đi trạm\nhay gọi cứu hộ?",
         t="1 phút", inp="% pin + khoảng cách", out="Hướng xử lý", hot=False),
    dict(n="Bước 5", title="Soạn tin hướng dẫn\n& gửi tài xế",
         t="6 phút", inp="Dữ liệu thô", out="Tin nhắn", hot=True),
]

x0, w, gap = 0.75, 2.85, 0.33
ybot, h = 4.85, 2.6

for i, s in enumerate(steps):
    x = x0 + i * (w + gap)
    face = RED_BG if s["hot"] else BOX
    edge = RED if s["hot"] else EDGE
    ax.add_patch(FancyBboxPatch((x, ybot), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=face, edgecolor=edge,
                                lw=2.1 if s["hot"] else 1.3, zorder=2))
    ax.text(x + 0.16, ybot + h - 0.33, s["n"], fontsize=10,
            fontweight="bold", color=MUTED, zorder=3)
    if s["hot"]:
        ax.text(x + w - 0.16, ybot + h - 0.33, "● BOTTLENECK", fontsize=8.5,
                fontweight="bold", color=RED, ha="right", zorder=3)
    ax.text(x + 0.16, ybot + h - 0.95, s["title"], fontsize=11,
            color=INK, va="top", zorder=3, linespacing=1.45)
    ax.plot([x + 0.16, x + w - 0.16], [ybot + 0.92, ybot + 0.92],
            color=EDGE, lw=0.9, zorder=3)
    ax.text(x + 0.16, ybot + 0.55, "In:  " + s["inp"], fontsize=8.5, color=MUTED, zorder=3)
    ax.text(x + 0.16, ybot + 0.26, "Out: " + s["out"], fontsize=8.5, color=MUTED, zorder=3)
    tcol = RED if s["hot"] else INK
    ax.text(x + w - 0.16, ybot + 0.4, s["t"], fontsize=12.5, fontweight="bold",
            color=tcol, ha="right", zorder=3)

    if i < len(steps) - 1:
        ax.add_patch(FancyArrowPatch((x + w + 0.03, ybot + h / 2),
                                     (x + w + gap - 0.03, ybot + h / 2),
                                     arrowstyle="-|>", mutation_scale=17,
                                     color=MUTED, lw=1.6, zorder=3))
        ax.text(x + w + gap / 2, ybot + h / 2 + 0.24, "↻", fontsize=13,
                color=AMBER, ha="center", fontweight="bold", zorder=4)

ax.text(0.75, 4.52,
        "↻ Handoff — điều phối viên phải đổi phần mềm và chép tay dữ liệu qua từng bước "
        "(hotline → bản đồ → dashboard trạm sạc → app nhắn tin)",
        fontsize=9.5, color=AMBER, style="italic")

# ---------------------------------------------------------------- Lane 2
ax.add_patch(Rectangle((0.4, 1.75), 16.2, 2.2, facecolor="#fdf6f5",
                       edgecolor=RED, lw=1.4, zorder=0))
ax.text(0.65, 3.62, "LÀN TÀI XẾ  (Driver) — chạy song song, không ai theo dõi",
        fontsize=11.5, fontweight="bold", color=RED)

ax.add_patch(FancyBboxPatch((0.75, 1.95), 12.6, 1.35,
                            boxstyle="round,pad=0.02,rounding_size=0.12",
                            facecolor="#ffffff", edgecolor=RED, lw=1.8, zorder=2))
ax.text(0.95, 2.92, "●  XE ĐỨNG CHỜ  —  16 phút", fontsize=13,
        fontweight="bold", color=RED, zorder=3)
ax.text(0.95, 2.38,
        "Không đón được khách  ·  pin tiếp tục tụt  ·  nếu cạn pin trước khi có "
        "hướng dẫn → xe chết máy giữa đường",
        fontsize=10, color=INK, zorder=3)

ax.add_patch(FancyArrowPatch((13.45, 2.62), (13.95, 2.62), arrowstyle="-|>",
                             mutation_scale=17, color=RED, lw=1.8, zorder=3))
ax.add_patch(FancyBboxPatch((14.05, 1.95), 2.5, 1.35,
                            boxstyle="round,pad=0.02,rounding_size=0.12",
                            facecolor=BLUE_BG, edgecolor=EDGE, lw=1.3, zorder=2))
ax.text(14.25, 2.78, "Nhận hướng dẫn", fontsize=10.5,
        fontweight="bold", color=INK, zorder=3)
ax.text(14.25, 2.34, "Sau 16 phút chờ", fontsize=9.5, color=MUTED, zorder=3)

# Noi lane 1 -> lane 2
ax.add_patch(FancyArrowPatch((15.48, 4.85), (15.3, 3.3), arrowstyle="-|>",
                             mutation_scale=15, color=MUTED, lw=1.4,
                             linestyle="--", zorder=1))

# ---------------------------------------------------------------- Chan trang
ax.plot([0.4, 16.6], [1.05, 1.05], color=EDGE, lw=1.2)
ax.text(0.4, 0.62,
        "TỔNG THỜI GIAN XỬ LÝ:  16 phút/lượt  —  "
        "cũng đúng bằng thời gian tài xế bị treo",
        fontsize=12.5, fontweight="bold", color=INK)
ax.text(0.4, 0.26,
        "Hai bottleneck khác bản chất:  Bước 3 là bài toán truy vấn dữ liệu  ·  "
        "Bước 5 là bài toán ngôn ngữ  —  hai bước này chiếm 11/16 phút",
        fontsize=10, color=MUTED)
ax.text(16.6, 0.26, "Ước lượng của nhóm, chưa đo từ log thật",
        fontsize=8.5, color=MUTED, style="italic", ha="right")

plt.tight_layout()
out = "04-workflow-diagram.png"
plt.savefig(out, dpi=170, facecolor="white", bbox_inches="tight")
print("saved", out)
