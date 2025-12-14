import qrcode

url = "" #enter the link or the text which you want to convert into qrcode

img=qr.make(url)
img.save('qrcode.png')
print('Qrcode Successfully generated')
