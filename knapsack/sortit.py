def merge2(arrA, arrB, item_a, item_b):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    merged_items = [0] * elements
    
    a = 0
    b = 0

    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            merged_items[i] = item_b[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            merged_items[i] = item_a[a]
            a += 1

        elif arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            merged_items[i] = item_a[a]
            a +=1
        
        else:
            merged_arr[i] = arrB[b]
            merged_items[i] = item_b[b]
            b += 1
    return(merged_arr, merged_items)



def merge_sort2(arr, arr_items):

    if len(arr) > 1:
        left = merge_sort2(arr[:len(arr)//2], arr_items[:len(arr)//2])
        right = merge_sort2(arr[len(arr)//2:], arr_items[len(arr)//2:])
      
       

        arr, arr_items = merge2(left[0], right[0], left[1], right[1])

    return(arr, arr_items)

#print(merge_sort2([5,9,2,3], [[5,5,5],[9,9,9], [2,2,2], [3,3,3]]))