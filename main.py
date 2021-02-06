# Code which I made for implement palindrome function
def is_palindrome(word):
    reverse_word = []
    word_list = []
    i = 0
    while i < len(word):
        reverse_word.append(word[(len(word) - 1) - i])
        word_list.append(word[i])
        i += 1
    if reverse_word == word_list:
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(f'{is_palindrome("hello")}\n')

# Code which codeit(site for studying code in Korea) recommend for implement palindrome function
def is_palindrome2(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False
    return True

# 테스트
print(is_palindrome2("racecar"))
print(is_palindrome2("stars"))
print(is_palindrome2("토마토"))
print(is_palindrome2("kayak"))
print(is_palindrome2("hello"))
