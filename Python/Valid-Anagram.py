def isAnagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char_count.get(char, 0) == 0:
            return False
        char_count[char] -= 1
    return True


# Alternative Solution 1:

from collections import Counter

def isAnagramAlt1(s, t):
    return Counter(s) == Counter(t)


# Alternative Solution 2:

from collections import defaultdict

def isAnagramAlt2(s, t):
    if len(s) != len(t):
        return False

    char_count = defaultdict(int)

    for char in s:
        char_count[char] += 1

    for char in t:
        if char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True


print(isAnagram("anagram", "nagaram")) # true
print(isAnagram("rat", "car")) # false
