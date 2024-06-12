# Time Complexity: O(log n) where `n` is number of elements in `nums`
# Space Complexity: O(1)

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Alternative Solution 1:

# Time Complexity: O(n)
# Space Complexity: O(1)

def searchInsertAlt1(nums, target):
    for idx, num in enumerate(nums):
        if num >= target:
            return idx

    return len(nums)

print(searchInsert([1,3,5,6], 5)) # 2
print(searchInsert([1,3,5,6], 2)) # 1
print(searchInsert([1,3,5,6], 7)) # 4
