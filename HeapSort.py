# CPS305 - F2020 - Lab 3
# Yong Kang He
# 500570639

arr = [75, 0, 4, -12, 42, 6, 34, 62, 55, 97, 33, 16, 87, 6, 19]

def heapSort(arr):
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,i)
    
    sorted = []
    for i in range(len(arr)):
        arr[0],arr[-1] = arr[-1],arr[0]
        sorted.append(arr[-1])
        arr.pop()
        heapify(arr,0)
    return sorted
def heapify(arr,i):
    lefti = (i*2)+1
    righti = (i*2)+2
    arrLen = len(arr)-1
    smallest = i
    
    if lefti <= arrLen:
        leftC = arr[(i*2)+1]
        if leftC < arr[smallest]:
            smallest = lefti
    if righti <= arrLen:
        rightC = arr[(i*2)+2]
        if rightC < arr[smallest]:
            smallest = righti
    if smallest != i:
        arr[smallest],arr[i] = arr[i], arr[smallest]
        heapify(arr,smallest)


sorted = heapSort(arr)
print(sorted)