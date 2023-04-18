from random import randint


all_symb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмно' \
          'прстуфхцчшщъыьэюя'


def password_crypt(password):
    password = password
    ipass = ''
    shift = randint(1, 9)
    for i in range(len(password)):
        if password[i] in all_symb:
            ipass += all_symb[(all_symb.find(password[i]) + shift) % len(all_symb)]
        else:
            ipass += password[i]
    ipass += str(shift)
    return ipass


def password_encrypt(ipass):
    print(ipass)
    shift = int(ipass[-1])
    password = ipass[:-1]
    ipass = ''
    for i in range(len(password)):
        if password[i] in all_symb:
            ipass += all_symb[all_symb.find(password[i]) - shift]
        else:
            ipass += password[i]
    return ipass
