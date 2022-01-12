def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    index = 0 
    i2 = 0
    while i2 < length:

        ele = nums[index]
        if ele == 0:
            nums.pop(index)
            nums.append(0)
        else:
            index += 1
        i2 = i2 + 1
        print(i2,' ',nums)
    return nums

print(moveZeroes([0,1,0,3,12]))