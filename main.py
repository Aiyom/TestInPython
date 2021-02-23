from send.sendSms import Send
from createDirectory.createOnDB import Create


print("Если хотите отправит продукт по смс отправьте цифру 1")
print("Если хотите отправит продукт на почту отправьте цифру 2")
print("Если хотите добавить пользователья отправьте  цифру 3")
print("Если хотите добавить продукта отправьте  цифру 4")

numberOfType = int(input("Введите какую цифру надо отправить: "))

if numberOfType == 1:
    Send().notice(numberOfType)
elif numberOfType == 2:
    Send().notice(numberOfType)
elif numberOfType == 3:
    Create().createUser()
elif numberOfType == 4:
    Create().createProduct()
