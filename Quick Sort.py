def partition(start,end,l1):
    # print(l1)
    i = start
    j = end-1
    pivot = l1[end]

    while i < j:
        while l1[i] < pivot:
            i += 1

        while l1[j] > pivot:
            j -= 1

        if i < j:
            l1[i],l1[j] = l1[j],l1[i]

    if l1[i] > pivot:
        l1[i],l1[end] = l1[end],l1[i]
    # print(l1)
    return i 


def quick_sort(start,end,l1):
    if start < end:
        pi = partition(start,end,l1)
        quick_sort(start,pi-1,l1)
        quick_sort(pi+1,end,l1)
        
l1=[3,5,8,1,2,9,9,4,7,6,6,11,23,45,19,5,12,34,0,-2,-11-1]
print("List before quick sort ->",l1)
quick_sort(0,len(l1)-1,l1)
print("list after quick sort ->",l1)