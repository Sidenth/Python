# Задайте список из k чисел последовательности 
# (1 + 1\k)^k и выведите на экран их сумму.

def fill_list(numb):
    list=[]
    for i in range(1,numb+1):
        list.append((1+1/i)**i)
        i+=1
    return list
def sum_el(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
        i+=1
    return sum
numb=int(input('Введите количество элементов '))
print(sum_el(fill_list(numb)))