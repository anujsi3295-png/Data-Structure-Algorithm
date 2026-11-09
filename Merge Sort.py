def mergesort(arr):
    if len(arr)>1:
        m=len(arr)//2
        ll=arr[:m]
        rl=arr[m:]
        mergesort(ll)
        mergesort(rl)

        i=j=k=0
        while i<len(ll) and j < len(rl):
            if ll[i]<rl[j]:
                arr[k]=ll[i]
                i+=1
            else:
                arr[k]=rl[j]
                j+=1
            k+=1

        while i<len(ll):
            arr[k]=ll[i]
            i+=1
            k+=1

        while j<len(rl):
            arr[k]=rl[j]
            j+=1
            k+=1
    return arr

l=[7,8,2,9,3,1,4,6]
print(mergesort(l))
