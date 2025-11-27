import qrcode



file_path = "C:\\Users\\moham\\Desktop\\py\\qrcode.png"

img = qrcode.make("https://www.instagram.com/4lucard_37/")

img.save(file_path)

