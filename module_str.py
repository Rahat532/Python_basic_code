# lest create some string manipulations
def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
def palimdrome_check(s):
    if palindrome(s):
        return "yes it is a palindrome"
    else:
        return "no it is not a palindrome"