

def bubble_sort(arr, n):
    count = 1
    for i in range(n):
        swaps = False
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swaps = True
        if swaps:
            count = count + 1
    return count

print(bubble_sort([1,3,2,5,4], 5))
            