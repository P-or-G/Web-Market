from API_settings import *


db_session.global_init("db/all.db")


def create_user(login, password, email, status='usr', tgm='Z'):
    user = User()
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
    else:
        print('error')


