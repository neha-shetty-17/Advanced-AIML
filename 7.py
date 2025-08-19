import qrcode

data = "https://openai.com"
qr = qrcode.make(data)
qr.save("myqrcode.png")
print("QR Code saved as myqrcode.png")
