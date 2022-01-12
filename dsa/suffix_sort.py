# string, index = input().split()

# n = len(string)
# suffices = []
# for i in range(n):
#     new_suffix = string[i:]
#     j = len(suffices) - 1
#     while j >= 0 and (suffices[j][0] > new_suffix[0]):
#         try: 
#             suffices[j + 1] = suffices[j]
#         except IndexError:
#             suffices.insert(j + 1, suffices[j])
#         j -= 1

#     try: 
#         suffices[j + 1] = new_suffix
#     except IndexError:
#         suffices.insert(j + 1, new_suffix)
    
# print(suffices[int(index) -1])

nums = [-1,0,3,5,9,12]


# def searchInsert(nums, target: int) -> int:
#     start = 0
#     end = len(nums) - 1 
#     if target > nums[end]:
#         return end + 1
#     elif target < nums[start]:
#         return 0

#     while (start <= end):
#         mid = (start + end)//2
#         ele = nums[mid]
#         if target == ele:
#             return mid
#         elif target < ele:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return start + 1

# print(searchInsert([1,3,5,6], 0))

# def sortedSquares(nums):
#     length = len(nums)
#     sorted_sq_list = [-1]*length
#     max_sq = 0
#     for num in nums:
#         num_sq = num*num
#         sq_eles = length - 1
#         while (sq_eles >= 0) and (sorted_sq_list[sq_eles] > num_sq):
#             sorted_sq_list[sq_eles + 1] = sorted_sq_list[sq_eles]
#             sq_eles -= 1
#         print(sorted_sq_list)
#         sorted_sq_list[sq_eles] = num_sq
#     return sorted_sq_list

# print(sortedSquares([-4,-1,0,3,10]))

def reverseString(s) -> None:


reverseString(["h","e","l","l","o"])