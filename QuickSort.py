# CPS305 - F2020 - Lab 3
# Yong Kang He
# 500570639

arr = [75, 0, 4, -12, 42, 6, 34, 62, 55, 97, 33, 16, 87, 6, 19]

def quickSort(arr):
    arrLen=len(arr)
    if arrLen <=1:
        return arr
    else:
        p = arr.pop()
        lessP =[]
        moreP=[]
        for n in arr:
            if n <= p:
                lessP.append(n)
            else:
                moreP.append(n)
    return quickSort(lessP) + [p] +quickSort(moreP) 

# You can add helper functions as well if needed

sorted = quickSort(arr)
print(sorted)