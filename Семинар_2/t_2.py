# Напишите программу, которая принимает на 
# вход число N и выдает набор произведений чисел от 1 до N.

def fill_list(num):
    list=[]
    for i in range(1,num+1):
        list.append(i)
        i+=1
    return list

def mult_progress(list):
    for i in range(1,len(list)):
        list[i]=list[i-1]*list[i]
        i+=1
    return list

numb=int(input('Введите число '))
print(mult_progress(fill_list(numb)))
