import sqlite3
from product import productList


class Send:
    person = None
    result = None
    product = None
    productId = None

    # connect with db
    conn = sqlite3.connect('testw.db')

    cur = conn.cursor()

    def notice(self, numberOfType):
        print("Список пользователей:")
        self.cur.execute("SELECT * FROM users ;")
        self.result = self.cur.fetchall()
        for i in range(0, len(self.result)):
            print(self.result[i])

        # call product on db
        productList.productList()

        # enter the userid who you want send sms and productid
        self.person = input("Ввведите id пользователья которему хотите отправить смс уведомления: ")
        self.productId = input("Ввведите id продукта которему хотите отправить: ")

        #test validation person
        if int(self.person) > len(self.result):
            msg = "Вы вышли из диапазон пользователей !!!"
            print(msg)
            self.errorMsg(msg)
            exit()

        try:

            # get user in the table
            self.product = productList.productList(self.productId)

            # select one person in the table
            self.cur.execute("SELECT * FROM users where userid=" + self.person + ";")
            self.result = self.cur.fetchall()
            self.result = self.result[0]
            self.product = self.product[0]

        except Exception as e:
            self.errorMsg(str(e))

        finally:

            if len(self.result) == None or len(self.product) == None:
                self.errorMsg("\n" + "Пользователь или продукт не найден. Проверьте еще раз!!!")
            else:
                # if we send sms notice than we get result on console
                if numberOfType == 1:
                    msg = "По ", self.result[1], " номер телефоном отправлен смс уведомление о товар ", self.product[1], " с ценой ", self.product[2], " самани смс-ом."
                    self.saveMsg(msg)
                    print(msg)
                else:
                    msg = "По ", self.result[2], " Email адресу отправлен уведомление о товар ", self.product[1], " с ценой ", self.product[2], " самани смс-ом."
                    self.saveMsg(msg)
                    print(msg)
            self.conn.commit()

    def saveMsg(self, msg):
        errorfile = open('sendProductOnUser.txt', "a")
        errorfile.write("\n" + str(msg))
        errorfile.close()

    def errorMsg(self, msg):
        errorfile = open('errorList.txt', "a")
        errorfile.write("\n" + msg)
        errorfile.close()