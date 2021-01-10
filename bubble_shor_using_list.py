def bubble_sort(mylist):
    for i in range(len(mylist)-1,0,-1):
        for j in range(i):
            if mylist[j]>mylist[j+1]:
                temp, mylist[j]=mylist[j], mylist[j+1]
                mylist[j+1] = temp

#mylist = [30,50,45,1,6,3,20,90,78]


mylist = list(input("enter element"))

print('Elements of list before sorting:',mylist)
bubble_sort(mylist)
print('Elements of list after sorting:',end='')
print(mylist)
