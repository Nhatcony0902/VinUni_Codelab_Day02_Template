import os
from PIL import Image, ImageDraw, ImageFont

def generate_diagram():
    width, height = 1200, 750
    background_color = (15, 23, 42) # Dark Slate Blue
    img = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Use default font or basic styling
    try:
        title_font = ImageFont.truetype("arial.ttf", 26)
        subtitle_font = ImageFont.truetype("arial.ttf", 18)
        box_title_font = ImageFont.truetype("arial.ttf", 15)
        text_font = ImageFont.truetype("arial.ttf", 13)
    except Exception:
        title_font = subtitle_font = box_title_font = text_font = ImageFont.load_default()

    # Header
    draw.rectangle([0, 0, width, 80], fill=(30, 41, 59))
    draw.text((30, 18), "Vin Smart Future — Xanh SM Battery & Emergency Dispatcher", fill=(255, 255, 255), font=title_font)
    draw.text((30, 50), "Workflow Mapping: Current State vs. Future AI-Assisted State", fill=(148, 163, 184), font=subtitle_font)

    # Section 1: Current State
    draw.text((30, 110), "🔴 CURRENT STATE WORKFLOW (Manual Process — 15 min Total)", fill=(248, 113, 113), font=subtitle_font)
    
    current_steps = [
        ("Step 1: Driver Call", "Dispatcher receives call", "⏱ 2 min", (51, 65, 85)),
        ("Step 2: GPS Lookup", "Manual map search", "⏱ 2 min", (51, 65, 85)),
        ("Step 3: Station Check", "Lookup empty chargers 🔴", "⏱ 5 min (Bottleneck)", (185, 28, 28)),
        ("Step 4: Draft SMS", "Write directions 🔴", "⏱ 5 min (Bottleneck)", (185, 28, 28)),
        ("Step 5: Dispatch", "Send or call tow", "⏱ 1 min", (51, 65, 85)),
    ]

    x_start = 30
    box_w, box_h = 205, 110
    gap = 25
    y_curr = 145

    for i, (title, sub, time_str, color) in enumerate(current_steps):
        bx = x_start + i * (box_w + gap)
        draw.rectangle([bx, y_curr, bx + box_w, y_curr + box_h], fill=color, outline=(100, 116, 139), width=2)
        draw.text((bx + 12, y_curr + 12), title, fill=(255, 255, 255), font=box_title_font)
        draw.text((bx + 12, y_curr + 42), sub, fill=(226, 232, 240), font=text_font)
        draw.text((bx + 12, y_curr + 75), time_str, fill=(254, 240, 138), font=text_font)

        if i < len(current_steps) - 1:
            # Arrow
            ax = bx + box_w
            draw.line([(ax + 2, y_curr + box_h // 2), (ax + gap - 2, y_curr + box_h // 2)], fill=(148, 163, 184), width=3)
            draw.polygon([(ax + gap - 2, y_curr + box_h // 2 - 5), (ax + gap + 3, y_curr + box_h // 2), (ax + gap - 2, y_curr + box_h // 2 + 5)], fill=(148, 163, 184))

    # Divider line
    draw.line([(30, 310), (width - 30, 310)], fill=(71, 85, 105), width=2)

    # Section 2: Future State
    draw.text((30, 335), "⚡ FUTURE STATE WORKFLOW (AI Co-pilot + HITL Gate — < 3 min Total)", fill=(52, 211, 153), font=subtitle_font)

    future_steps = [
        ("Step 1: Driver Call", "Dispatcher receives call", "⏱ 0.5 min", (51, 65, 85)),
        ("Step 2: Auto Pull 🔵", "API GPS & Station data", "⏱ Real-time (< 2s)", (14, 116, 144)),
        ("Step 3: AI Draft 🔵", "Generates [DRAFT_ONLY]", "⏱ Real-time (< 3s)", (14, 116, 144)),
        ("Step 4: HITL Gate 🟢", "Dispatcher reviews & sends", "⏱ 1.5 min", (21, 128, 61)),
        ("Step 5: Fallback ↩️", "Mobile Charger if < 5% pin", "Automated trigger", (180, 83, 9)),
    ]

    y_fut = 370
    for i, (title, sub, time_str, color) in enumerate(future_steps):
        bx = x_start + i * (box_w + gap)
        draw.rectangle([bx, y_fut, bx + box_w, y_fut + box_h], fill=color, outline=(52, 211, 153), width=2)
        draw.text((bx + 12, y_fut + 12), title, fill=(255, 255, 255), font=box_title_font)
        draw.text((bx + 12, y_fut + 42), sub, fill=(226, 232, 240), font=text_font)
        draw.text((bx + 12, y_fut + 75), time_str, fill=(254, 240, 138), font=text_font)

        if i < len(future_steps) - 1:
            ax = bx + box_w
            draw.line([(ax + 2, y_fut + box_h // 2), (ax + gap - 2, y_fut + box_h // 2)], fill=(52, 211, 153), width=3)
            draw.polygon([(ax + gap - 2, y_fut + box_h // 2 - 5), (ax + gap + 3, y_fut + box_h // 2), (ax + gap - 2, y_fut + box_h // 2 + 5)], fill=(52, 211, 153))

    # Operational Boundaries Legend
    draw.rectangle([30, 530, width - 30, 700], fill=(30, 41, 59), outline=(100, 116, 139), width=1)
    draw.text((50, 545), "🛡️ Operational Boundaries & Safety Constraints (Vin Smart Future):", fill=(255, 255, 255), font=box_title_font)
    draw.text((50, 580), "• Rule 1: Output must ALWAYS begin with [DRAFT_ONLY] tag. Direct automated dispatch to driver is prohibited.", fill=(226, 232, 240), font=text_font)
    draw.text((50, 610), "• Rule 2: Critical Battery Threshold (< 5%): Refuse charging stations > 5km. Instantly trigger Mobile Charging Vehicle.", fill=(226, 232, 240), font=text_font)
    draw.text((50, 640), "• Rule 3: Human-In-The-Loop (HITL): Human Dispatcher must approve all AI drafts before sending.", fill=(226, 232, 240), font=text_font)
    draw.text((50, 670), "• Fallback: If AI confidence is low or API fails, Dispatcher seamlessly takes over manual workflow.", fill=(226, 232, 240), font=text_font)

    target_path = r"d:\AIVin\Lab_Group\VinUni_Codelab_Day02_Template\04-workflow-diagram.png"
    img.save(target_path)
    print(f"Diagram saved successfully at {target_path}")

if __name__ == "__main__":
    generate_diagram()
