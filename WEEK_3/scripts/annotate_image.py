# annotate_image.py
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import getpass
from datetime import datetime

png = Path("reports/critical_path.png")
out = Path("reports/critical_path_annotated.png")
if not png.exists():
    print("Error: input PNG not found:", png); raise SystemExit(1)

img = Image.open(png).convert("RGBA")
w,h = img.size

# draw translucent bar and text
overlay = Image.new("RGBA", img.size, (255,255,255,0))
draw = ImageDraw.Draw(overlay)

# basic font selection - fallback to default if not found
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
except Exception:
    font = ImageFont.load_default()

text = f"user: {getpass.getuser()}    ts: {datetime.now().isoformat(' ')}"
padding = 8
text_w, text_h = draw.textsize(text, font=font)
bar_h = text_h + 2*padding

# draw semi-transparent rectangle at top-left
draw.rectangle([(0,0),(text_w+2*padding, bar_h)], fill=(0,0,0,160))
draw.text((padding, padding), text, fill=(255,255,255,255), font=font)

combined = Image.alpha_composite(img, overlay)
combined.convert("RGB").save(out)
print("Annotated image saved to", out)

