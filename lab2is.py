#Yong Kang He
#500570639
#Lab 2 Insertion Sort
def insertionSort(alist):
   for i in range(1,len(alist)):

     currentvalue = alist[i]
     position = i

     while position>0 and alist[position-1]<currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [86, 0, 66, 31, 90, 78, 54, 72, 91, 27, 69, 6, 41, 3, 96, 99, 94, 68, 56, 12]
insertionSort(alist)
print(alist)
