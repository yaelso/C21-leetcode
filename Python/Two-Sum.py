def twoSum(nums, target):
    values = {}

    for i, val in enumerate(nums):
      if (target - val) in values:
          return [values[target - val], i]
      else:
          values[val] = i

print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]
print(twoSum([3,3], 6)) # [0,1]
