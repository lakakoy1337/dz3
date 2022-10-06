from random import randint

print("Введите количество цифр")

num = int(input())

symapolozh = 0
symaotric = 0
spisok = []

for i in range(num): 
    rnd = randint(-100, 100) 
    if rnd == 0: 
        while rnd == 0: 
            rnd = randint(-100, 100) 
    if rnd > 0: 
        symapolozh = symapolozh + rnd
    elif rnd < 0: 
        symaotric = symaotric + rnd
    spisok.append(rnd)

    print("Сумма положительных: ", symapolozh)
    print("Сумма отрицательных=: ", symaotric)
    print("Список чисел: ", spisok)