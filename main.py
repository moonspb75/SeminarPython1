"""username = input("Введите имя: ")
if username == "Маша":
    print("Ура, это же Маша!")
elif username == "Марина":
    print("Я так ждала Вас, Марина!")
elif username == "Ильнар":
    print("Ильнар - топ")
else:
    print("Привет, ", username)"""

"""i = 0
while i < 5:
    if i == 3:
        break - нежелательно использовать
    i = i + 1
else:
    print("Пожалуй")
    print("хватит )")
print(i)"""

"""n = int (input())
flag = True
i = 2
while flag:
    if n % i == 0:  # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делитель числа не может превышать введенное число делёное на 2
        print(n)
        flag = False
    i += 1"""

text = "Съешь ещё эти мягкие булочки"
print(len(text))
print("ещё" in text)
print(text.lower()) # Все буквы с маленькой буквы
print(text.upper()) # Все буквы заглавные
print(text.replace("ещё", "ЕЩЁ")) # 

