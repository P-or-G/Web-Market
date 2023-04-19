from API.lbr_settings import *

db_session.global_init("../db/all.db")


def get_all_users_ids():
    db_sess = db_session.create_session()
    users_ids_list = []

    for user in db_sess.query(User).all():
        users_ids_list.append(user.__repr__().split(' *** ')[0])
    db_sess.close()

    return users_ids_list


def get_all_goods_ids():
    db_sess = db_session.create_session()
    all_goods_ids = []

    for goods in db_sess.query(Goods).all():
        all_goods_ids.append(goods.__repr__().split(' *** ')[0])
    db_sess.close()

    return all_goods_ids


def create_user(login, password, email, status='usr', tgm='Z'):
    user = User()
    user.id = int(get_all_users_ids()[-1]) + 1
    user.login = login
    user.hashed_password = password_crypt(password)
    user.email = email
    user.status = status
    if tgm != 'Z':
        user.telegram_id = tgm
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_sess.close()


def get_login(id=0, email=''):
    db_sess = db_session.create_session()
    if email != '':
        for i in db_sess.query(User).filter(User.email == email):
            db_sess.close()
            return i.__repr__().split(' *** ')[1]
    elif id != 0:
        for i in db_sess.query(User).filter(User.id == id):
            db_sess.close()
            return i.__repr__().split(' *** ')[1]
    db_sess.close()
    return None


def get_email(id=0, login=''):
    db_sess = db_session.create_session()
    if login != '':
        for i in db_sess.query(User).filter(User.login == login):
            db_sess.close()
            return i.__repr__().split(' *** ')[2]
    elif id != 0:
        for i in db_sess.query(User).filter(User.id == id):
            db_sess.close()
            return i.__repr__().split(' *** ')[2]
    db_sess.close()
    return None


def get_id(login, email, password, telegramm_id=0):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.login == login, User.email == email).first()

    if password_encrypt(user.__repr__().split(' *** ')[3]) == password:
        db_sess.close()
        return user.__repr__().split(' *** ')[0]

    db_sess.close()
    return 'Неверный пароль'


def get_id_teleg(teleg_id):
    db_sess = db_session.create_session()
    try:
        user = db_sess.query(User).filter(User.telegram_id == teleg_id).first()
        return user.__repr__().split(' *** ')[0], user.__repr__().split(' *** ')[4]
    except:
        return 0, usr


def get_password(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return password_encrypt(i.__repr__().split(' *** ')[3])


def get_status(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[4]


def get_telegram_id(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[5]


def get_current_id(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[6]


def get_history_id(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[7]


def change_param(id, param, new_val):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id).first()
    if param == 1:
        user.login = new_val
    elif param == 2:
        user.email = new_val
    elif param == 3:
        user.hashed_password = password_crypt(new_val)
    elif param == 4:
        user.status = new_val
    elif param == 5:
        user.telegram_id = new_val
    elif param == 6:
        user.current_id = new_val
    elif param == 7:
        user.history_id = new_val
    db_sess.commit()
    db_sess.close()


def create_goods(name, trader_id, category, description, photo, amount=0, sell_amount=0, cost=0):
    goods = Goods()
    goods.name = name
    goods.trader_id = trader_id
    goods.category = category
    goods.description = description
    goods.photo_name = photo
    goods.amount = amount
    goods.sell_amount = sell_amount
    goods.cost = cost
    db_sess = db_session.create_session()
    db_sess.add(goods)
    db_sess.commit()
    db_sess.close()


def get_goods_name(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[1]


def get_goods_seller(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[2]


def get_goods_kat(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[3]


def get_goods_des(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[4]


def get_goods_photo(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[5]


def get_goods_amo(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[6]


def get_goods_sam(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[7]


def get_goods_cost(id):
    db_sess = db_session.create_session()
    yep = int(id)
    goods = db_sess.query(Goods).filter(Goods.id == yep).first()
    db_sess.close()
    return goods.__repr__().split(' *** ')[7]


def get_all_user_goods(user_id):
    db_sess = db_session.create_session()
    answer = []
    yep = int(user_id)
    for i in db_sess.query(Goods).filter(Goods.trader_id == yep):
        answer.append(str(i).replace("'", ''))
    db_sess.close()
    return answer


def get_all_goods_kat(kat):
    right_ids = []
    for id in get_all_goods_ids():
        if get_goods_kat(id) == kat:
            right_ids.append(id)
    return right_ids


