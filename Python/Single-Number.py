# Time Complexity: O(n)
# Space Complexity: O(1)

def singleNumber(nums):
    xor = 0

    for num in nums:
        xor ^= num

    return xor

print(singleNumber([2,2,1])) # 1
print(singleNumber([4,1,2,1,2])) # 4
print(singleNumber([1])) # 1
