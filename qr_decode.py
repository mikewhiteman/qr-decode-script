#!/usr/bin/env python3
#Super quick QR code decode routine for HackerOne's h1-415-ctf

import argparse
from pyzbar.pyzbar import decode
from PIL import Image

# Collect file path positional argument
parser = argparse.ArgumentParser()
parser.add_argument("path",help="path to QR code image file")
args = parser.parse_args()

# Decode QR code
data = decode(Image.open(args.path))

# Profit
print(data)