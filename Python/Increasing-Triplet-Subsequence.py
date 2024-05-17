import math


def increasingTriplet(nums):
    first = second = math.inf

    for num in nums:
        if second < num:
            return True
        if num <= first:
            first = num
        else:
            second = num

    return False

print(increasingTriplet([1,2,3,4,5])) # True
print(increasingTriplet([5,4,3,2,1])) # False
print(increasingTriplet([2,1,5,0,4,6])) # True
print(increasingTriplet([20,100,10,12,5,13])) # True
