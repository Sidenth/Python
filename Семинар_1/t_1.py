# Напишите программу, которая принимает на 
# вход цифру, обозначающую день недели, и 
# проверяет, является ли этот день выходным.

print('Введите номер дня недели')
num = int(input())
if (num == 6) or (num==7):
    print('Выходной')
else:
    print('Рабочий день')
