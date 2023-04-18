from msilib.schema import File
from PIL import Image
from flask import Flask, render_template, redirect
from flask import url_for
from flask import request

app = Flask(__name__)

data1 = open('static/img/profile.png', 'rb').read()
a = [data1, data1, data1, 1]


@app.route('/')
@app.route('/main_page', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('main_str.html')
    else:
        return render_template('main_str.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')


@app.route('/body', methods=['GET', 'POST'])
def body():
    with Image.open('static/img/profile.png') as img:
        img.load()
        if request.method == 'POST':
            return render_template('body.html', spisok=a)
        else:
            return render_template('body.html', spisok=a, img='..img/add_cor.png')


@app.route('/prod', methods=['GET', 'POST'])
def prod():
    if request.method == 'POST':
        if request.form['btn'] == 'cor':
            print('aaa')
        return render_template('body.html', spisok=a)
    else:
        return render_template('prod.html', spisok=a, img='..img/add_cor.png')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
