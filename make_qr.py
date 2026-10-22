#!/usr/bin/env python3
"""Generate the 'found' QR code (PNG + SVG) at print resolution."""
import os, sys, qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = sys.argv[1] if len(sys.argv) > 1 else 'https://darrenhopwood13-maker.github.io/randalls-london-archive/'
OUT = '/root/.hermes/profiles/banksy/work/allies-review/web/qr'
os.makedirs(OUT, exist_ok=True)

qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=40, border=4)
qr.add_data(URL)
qr.make(fit=True)

# print master: near-black on cream, generous quiet zone
img = qr.make_image(fill_color=(18, 17, 16), back_color=(242, 237, 228)).convert('RGB')
png = os.path.join(OUT, 'found-qr.png')
img.save(png, optimize=True)

# vector for a printer
import qrcode.image.svg as svg
v = qrcode.QRCode(version=qr.version, error_correction=ERROR_CORRECT_H, box_size=1, border=4)
v.add_data(URL); v.make(fit=True)
svgimg = v.make_image(image_factory=svg.SvgPathImage)
svg_path = os.path.join(OUT, 'found-qr.svg')
svgimg.save(open(svg_path, 'wb'))

print('url:', URL)
print('version:', qr.version, '| modules:', qr.modules_count, '| error correction: H')
print('png:', png, img.size, os.path.getsize(png) // 1024, 'KB')
print('svg:', svg_path, os.path.getsize(svg_path) // 1024, 'KB')
