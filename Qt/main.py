import sys
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem


class LogIn(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('log_in_window.ui', self)  # Загружаем дизайн

        self.login = ''
        self.password = ''

        self.btn_login.clicked.connect(self.open_window_for_salesman)

    def open_window_for_salesman(self):  # Открытие нового окна если логин существует и пароль подходит
        self.login = self.Login.text()
        self.password = self.Password.text()
        global login_id
        login_id = self.login

        con = sqlite3.connect("all.db")
        cur = con.cursor()
        result = cur.execute("""SELECT login, hashed_password, status, id FROM users""").fetchall()
        con.close()

        for el in result:
            if self.login == el[0] and self.password == el[1]:
                login_id = el[3]
                if el[2] == 'trd':
                    ex4.show()
                else:
                    ex1.show()
            else:
                print('Неверный логин или пароль!')
        ex1.show()
        ex.hide()


class WindowForSalesman(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_for_salesman.ui', self)  # Загружаем дизайн

        self.connection = sqlite3.connect("all.db")

        self.btn_add.clicked.connect(self.open_window_for_add_product)
        self.btn_r.clicked.connect(self.update)
        self.btn_del.clicked.connect(self.del_product)
        self.select_data()

    def update(self):
        self.select_data()

    def select_data(self):

        res = self.connection.cursor().execute("SELECT * FROM goods").fetchall()

        self.BD.setColumnCount(8)
        self.BD.setRowCount(0)

        for i, row in enumerate(res):
            self.BD.setRowCount(
                self.BD.rowCount() + 1)
            for j, elem in enumerate(row):
                self.BD.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.connection.close()

    def open_window_for_add_product(self):
        ex2.show()

    def del_product(self):
        cur = self.connection.cursor()
        s = self.BD.currentIndex().row()

        res = cur.execute("""SELECT trader_id FROM goods
                        WHERE id = ?""", (s + 1,)).fetchall()
        if res[0][0] == login_id:
            cur.execute("""DELETE FROM goods
                            WHERE id = ?""", (s + 1,)).fetchall()
        self.connection.commit()
        cur.close()


class AddProducts(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_products.ui', self)  # Загружаем дизайн

        self.name_product = ''
        self.lor_product = ''
        self.number_product = 0
        self.category_product = ''
        self.sale = 0.0
        self.con = sqlite3.connect('all.db')

        self.btn_add.clicked.connect(self.add_product)

    def add_product(self):
        if self.NameProduct.text() != '' and self.LorProduct.text() != '' and self.NumberProduct.value() > 0:
            self.name_product = self.NameProduct.text()
            self.lor_product = self.LorProduct.text()
            self.number_product = self.NumberProduct.value()
            self.category_product = self.Category.currentText()
            self.sale = float(self.Sale.text())
            cur = self.con.cursor()

            cur.execute("""INSERT INTO goods (name, trader_id, category, description, photo_name, amount, sell_amount)
                                 VALUES (?, ?, ?, ?, NULL, ?, ?)""", (self.name_product, login_id,
                        self.category_product, self.lor_product, self.number_product, self.sale)).fetchall()

            self.con.commit()
            cur.close()
            ex2.hide()
        else:
            print("Убедитесь, что вы заполнили все поля и указали число отличное от нуля!")


class WindowForAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_for_admin.ui', self)  # Загружаем дизайн

        self.btn_add.clicked.connect(self.open_window_for_add_salesman)

    def open_window_for_add_salesman(self):
        ex3.show()


class AddSalesman(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_salesman.ui', self)  # Загружаем дизайн

        self.login = ''
        self.password = ''
        self.email = ''
        self.phone_number = ''

        self.btn_add.clicked.connect(self.add_salesman)

    def add_salesman(self):
        if self.Login.text() != '' and self.Password.text() != "" and self.Email.text() != '' and\
                self.NumberPhone.text != '':
            self.login = self.Login.text()
            self.password = self.Password.text()
            self.email = self.Email.text()
            self.phone_number = self.NumberPhone.text()
            ex3.hide()
            #  здесь Федина функция добавления
        else:
            print("Убедитесь, что вы заполнили все поля!")


if __name__ == '__main__':
    login_id = ''

    app = QApplication(sys.argv)
    ex = LogIn()
    ex1 = WindowForSalesman()
    ex2 = AddProducts()
    ex3 = AddSalesman()
    ex4 = WindowForAdmin()
    ex.show()
    sys.exit(app.exec_())
