import re

"""Визначити і вивести на екран всі цифри цілого числа n"""

print('Лабораторна робота №2; Варіант №7.Завдання №1:\
 \nВизначити і вивести на екран всі цифри цілого числа n')
print('Доротюк Т.В. КМ-91')

while True:
    print('Ця програма здатна розбивати цілі числа на цифри, з яких вони складаються')
    numb_1 = input('Введіть ваше число: ')
    if bool(re.match("^[+-]?([0-9]+)$", numb_1)):
        pass
    else:
        print('Ви ввели неправильний тип даних. Програма працює лише з цілими числами!')
        continue
    res_1 = list(str(numb_1))
    print('Введене вами число містить наступні цифри: ', res_1)
    to_exit = input("Щоб продовжити розрахунки, просто натисніть A, або будь-який інший символ для завершення роботи")
    if to_exit == "A":
        continue
    else:
        break
print('Роботу з програмою завершено')





