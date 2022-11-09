# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.

def sum_elems(num):
    num.split
    i=3
    sum=int(num[2])
    while i<len(num):
        sum=sum+int(num[i])
        i+=1
    return sum
num = input('Введите число ')
print(f'{sum_elems(num)}')