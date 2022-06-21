list1=[]
list2=[]

value_for_list1=int(input("enter the no of elements in list1: "))
for i in range(0,value_for_list1):
    element=eval(input("enetr the list1 elememts: "))
    list1.append(element)

value_for_list2=int(input("enter the no of elements in list2: "))
for i in range(0,value_for_list2):
    element1=eval(input("enter the list2 elements: "))
    list2.append(element1)

print(list1,list2)

def add(a,b):
    print(a+b)
    return a+b
