#Yong Kang He
#500570639
#Lab 2 bubble sort
def bubbleSort(alist):
    for num in range(len(alist)-1,0,-1):
        for i in range(num):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [86, 0, 66, 31, 90, 78, 54, 72, 91, 27, 69, 6, 41, 3, 96, 99, 94, 68, 56, 12]
bubbleSort(alist)
print(alist)