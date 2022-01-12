def twoSum(numbers, target) -> None:
    length = len(numbers)
    for gap in range(1,length) :
        for i in range(length - gap):
            first = i
            second = i+gap
            print(first, second)
            if numbers[first] + numbers[second] == target:
                 return [first+1,second+1]

print(twoSum([2,7,11,15],17))