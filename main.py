import qrcode

url = "" #put the link which you want to convert into qrcode

img=qr.make(url)
img.save('qrcode.png')
print('Qrcode Successfully generated')
