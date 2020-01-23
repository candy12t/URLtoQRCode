from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import qrcode
import datetime


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/convert', methods=['GET', 'POST'])
def convert():
  if request.method == 'POST':
    url = request.form['url']
    qr_code = QRCode(url)
    return render_template('index.html', qr_code=qr_code)
  else:
    return redirect(url_for('index'))


def QRCode(url):
  img = qrcode.make(url)
  dt = datetime.datetime.now()
  filename = './static/img/{}.png'.format(dt.strftime('%Y%m%d%H%M%S'))
  img.save(filename)
  return filename


if __name__ == '__main__':
  app.run()