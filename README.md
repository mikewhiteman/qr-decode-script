# qr-decode-script
Dead simple Python script using the `zbar library` to decode QR codes offline (useful for CTFs)

# Installation
There may be a way to do this with native Python libraries but few seemed actively maintained. For the script to work, you'll need to install the `zbar shared library` on Linux/Mac OS X systems:

Mac OS X:
`brew install zbar`

Linux:
`sudo apt-get install libzbar0` 

# Usage
`./qr_decode.py [path to local file]`
