# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

import random

def mult_el(num, pos_1, pos_2):
    list=[]
    for i in range(num):
        list.append(random.randrange(-num, num+1))
        i+=1
    mult=list[pos_1-1]*list[pos_2-1]
    print(list)
    return mult
num=int(input('Введите количество элементов '))
# pos_one=int(input('Введите позицию первого эл-та '))
# pos_two=int(input('Введите позицию второго эл-та '))
pos_one, pos_two=map(int, input('Введите через пробел позиции эл-тов ').split())
print(mult_el((num), pos_one, pos_two))
