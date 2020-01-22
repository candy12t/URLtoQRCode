import qrcode
from PIL import Image

print('input url convert >> ', end='')
url = input()
print('input image name >> ', end='')
name = input()
img = qrcode.make(url)
img.save('img/{}.png'.format(name))
