def isPalindrome(s):    
    return s.strip() == s[::-1].strip()

s = input("Enter a string: ")

if isPalindrome(s):
    print("Palindrome")
else:
    print("Not a palindrome")
