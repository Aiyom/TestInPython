import sqlite3


class Create:

    conn = sqlite3.connect('testw.db')
    cur = conn.cursor()

    def createProduct(self):
        title = input("Введите название товара: ")
        product_price = input("Введите цену товара: ")
        product = (title, product_price)

        self.cur.execute("INSERT INTO products(title, price) VALUES(?, ?);", product)
        self.conn.commit()

    def createUser(self):
        phone = int(input("Введите номер телефона: "))
        email = input("Введите Email адресс: ")
        user = (phone, email)

        self.cur.execute("INSERT INTO users(phoneNumber, email) VALUES(?, ?);", user)
        self.conn.commit()
