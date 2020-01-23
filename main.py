import qrcode
import datetime
from PIL import Image

print('input url convert >> ', end='')
url = input()

img = qrcode.make(url)
dt = datetime.datetime.now()
filename = 'img/{}.png'.format(dt.strftime('%Y%m%d%H%M%S'))
img.save(filename)
