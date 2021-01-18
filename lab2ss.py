#Yong Kang He
#500570639
#Lab 2 Selection Sort
def selectionSort(alist):
   for slot in range(len(alist)-1,0,-1):
       largesti=0
       for i in range(1,slot+1):
           if alist[i]<alist[largesti]:
               largesti = i

       temp = alist[slot]
       alist[slot] = alist[largesti]
       alist[largesti] = temp

alist = [86, 0, 66, 31, 90, 78, 54, 72, 91, 27, 69, 6, 41, 3, 96, 99, 94, 68, 56, 12]
selectionSort(alist)
print(alist)