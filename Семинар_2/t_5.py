# Реализуйте алгоритм перемешивания списка.
import random
def fill_list(num):
    list=[]
    for i in range(num):
        list.append(random.randrange(-10,10))
        i+=1
    print(list)
    return list
def sort_list(list):
    max=list[0]
    i=0
    j=i+1
    while i<len(list):
        while j<len(list):
            if list[i]>list[j]:
                max=list[i]
                list[i]=list[j]
                list[j]=max
            j+=1
        i+=1
    print(list)
    return list
num=6
sort_list(fill_list(num))
