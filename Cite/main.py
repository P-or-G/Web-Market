from flask import Flask, render_template, redirect
from flask import url_for
from flask import request
from API.lbr import *

app = Flask(__name__)

data1 = "static/img/meats.jpg"
a = [data1, data1, data1, 1]

change_param(2, 6, [])
@app.route('/')
@app.route('/main_page', methods=['GET', 'POST'], defaults={'user_id': 0})
@app.route('/main_page/<int:user_id>', methods=['GET', 'POST'])
def index(user_id):
    print(user_id)
    if request.method == 'POST':
        if request.form['btn'] == 'cors':
            if user_id == 0:
                return redirect(f'/main_page/{user_id}')
            return redirect(f'/cors/{user_id}')
        elif request.form['btn'] == 'prof':
            if user_id != 0:
                return redirect(f'/main_page/{user_id}')
            else:
                return redirect(f'/login/{user_id}')
        elif request.form['btn'] == 'fav':
            print(user_id != 0)
            if user_id == 0:
                return redirect(f'/main_page/{user_id}')
            else:
                return redirect(f'/body/fav/{user_id}')
        return redirect(f'/body/{request.form["btn"]}/{user_id}')
    else:
        return render_template('main_str.html')


@app.route('/login/<int:user_id>', methods=['GET', 'POST'])
def login(user_id):
    if request.method == 'POST':
        if request.form['btn'] == 'Register':
            create_user(request.form['num'], request.form['pass'], request.form['email'], 'usr')
            return redirect(f'/main_page/{get_all_users_ids()[-1]}')
        if request.form["btn"] == 'SignIn':
            if 'Неверный пароль' in get_id(request.form['num'], request.form['email'], request.form['pass']):
                return redirect(f'/login/{user_id}')
            else:
                user_id = int(get_id(request.form['num'], request.form['email'], request.form['pass']))
                return redirect(f'/main_page/{user_id}')
        return redirect(f'/main_page/{user_id}')
    elif user_id != 0:
        return redirect(f'/main_page/{user_id}')
    else:
        return render_template('login.html')


@app.route('/cors/<int:user_id>', methods=['GET', 'POST'])
def cors(user_id):
    if get_current_id(user_id):
        ids = list(map(int, get_current_id(user_id).split(', ')))
        sp = [(get_goods_photo(id), id) for id in ids]
        if request.method == 'POST':
            for id in ids:
                get_goods_amo(id)
                buy_goods(id)
                get_goods_amo(id)
                change_param(user_id, 6, [])
            return redirect(f'/main_page/{user_id}')
        else:
            return render_template('cors.html', spisok=sp)
    else:
        return redirect(f'/main_page/{user_id}')


@app.route('/body/<value>/<int:user_id>', methods=['GET', 'POST'])
def body(value, user_id):
    if value == 'fav':
        if user_id != 0:
            if get_history_id(user_id):
                ids = list(map(int, get_history_id(user_id).split(', ')))
    else:
        ids = get_all_goods_kat(value)
    sp = [(get_goods_photo(id), id) for id in ids]
    if request.method == 'POST':
        if request.form['btn'] == 'cors':
            if user_id == 0:
                return redirect(f'/main_page/{user_id}')
            return redirect(f'/cors/{user_id}')
        elif request.form['btn'] == 'prof':
            if user_id != 0:
                return redirect(f'/main_page/{user_id}')
            else:
                return redirect(f'/login/{user_id}')
        elif request.form['btn'] == 'fav':
            print(user_id != 0)
            if user_id == 0:
                return redirect(f'/main_page/{user_id}')
        else:
            return redirect(f'/prod/{request.form["btn"]}/{user_id}')
    else:
        return render_template('body.html', spisok=sp)


@app.route('/prod/<value>/<int:user_id>', methods=['GET', 'POST'])
def prod(value, user_id):
    print(user_id == 2)
    image = get_goods_photo(value)
    des = get_goods_des(value)
    cost = get_goods_cost(value)
    name = get_goods_name(value)
    if request.method == 'POST':
        if request.form['btn'] == 'add_cor':
            if user_id != 0:
                if get_current_id(user_id):
                    cors = list(map(int, get_current_id(user_id).split(', ')))
                else:
                    cors = []
                cors.append(value)
                change_param(user_id, 6, cors)
                return redirect(f'/main_page/{user_id}')
        elif request.form['btn'] == 'add_fav':
            if user_id != 0:
                if get_history_id(user_id):
                    cors = list(map(int, get_history_id(user_id).split(', ')))
                    cors.append(value)
                    change_param(user_id, 7, cors)
                return redirect(f'/main_page/{user_id}')
            else:
                cors = get_history_id(user_id)
                cors.append(value)
                change_param(user_id, 7, cors)
                return redirect(f'/main_page/{user_id}')
        return redirect(f'/main_page/{user_id}')
    else:
        return render_template('prod.html', image=image, cost=cost, des=des, name=name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
