import qrcode

qrg = input("Enter the url:-\t")

img = qrcode.make(qrg)
img.save("myqr.jpg")