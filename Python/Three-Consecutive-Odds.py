def threeConsecutiveOdds(arr):
    if len(arr) < 3:
        return False

    for idx, num in enumerate(arr):
        if idx == 0 or idx == len(arr) - 1:
            continue

        if not num % 2 == 0:
            if not arr[idx - 1] % 2 == 0 and not arr[idx + 1] % 2 == 0:
                    return True
    return False

# Alternative Solution 1

def threeConsecutiveOddsAlt1(arr):
    if len(arr) < 3:
        return False

    for num in range(1, len(arr) - 1):
        if not arr[num] % 2 == 0:
            if not arr[num - 1] % 2 == 0 and not arr[num + 1] % 2 == 0:
                return True
    return False

print(threeConsecutiveOdds([1,1,2,1,1]))  # False
print(threeConsecutiveOdds([1,3,2]))  # False
print(threeConsecutiveOdds([1,2,1,1])) # False
print(threeConsecutiveOdds([2,6,4,1])) # False
print(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])) # True
print(threeConsecutiveOdds([1,1,1]))  # True
print(threeConsecutiveOdds([102,780,919,897,901])) # true
