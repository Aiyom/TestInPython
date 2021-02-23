import sqlite3


def productList(productId = None):
    conn = sqlite3.connect('testw.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM products ;")
    result = cur.fetchall()
    if productId == None:
        print("Список продуктов:")
        for i in range(0, len(result)):
            print(result[i])
    elif str(productId) > str(len(result)):
        msg = "Вы вылши из диапазон товаров !!!"
        errorMsg(msg)
        print(msg)
        exit()
    else:
        cur.execute("SELECT * FROM products where productid=" + productId + ";")
        return cur.fetchall()

    conn.commit()


def errorMsg(msg):
    errorfile = open('errorList.txt', "a")
    errorfile.write("\n" + msg)
    errorfile.close()