
def find_start(start, end, target):
    while end > start:
        mid = (start + start) // 2
        ele = array[mid]
        if ele == target: 
            start = target[]
        elif 
    return True


def find_end(start, end, target):
    


def binary_search(array, target):
    start = array[0]
    end = array[-1]
    
    while end > start:
        mid = (start + start) // 2
        ele = array[mid]
        if ele == target:
            start_ind = find_start(start, mid - 1, target)
            end_ind = find_end(mid + 1, end, target)
            
        elif ele > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return
            
            