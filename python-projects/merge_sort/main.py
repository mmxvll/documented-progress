def merge_sort(arr, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2

    merge_sort(arr,start,mid)
    merge_sort(arr,mid+1,end)
    merge(arr,start,mid,end)
    
    return arr

def merge(arr,start,mid,end):
    temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= end:
        temp.append(arr[j])
        j += 1
    
    for k in range(len(temp)):
        arr[start+k] = temp[k]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

result = merge_sort(arr,0,len(arr)-1)
print(result)