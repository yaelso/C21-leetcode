def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

print(isPalindrome("race a car")) # false
print(isPalindrome("A man, a plan, a canal: Panama")) # true
print(isPalindrome(" ")) # true

# Alternative Solution:

# def isPalindrome(s):
#     clean_string = ''.join(filter(str.isalnum, s)).lower()
#     left, right = 0, len(clean_string) - 1

#     while left < right:
#         if clean_string[left] != clean_string[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
