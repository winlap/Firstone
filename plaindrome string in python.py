#s = s[::1] tp reverse the string
def is_palindrome(s):
    #remove all the white spaces and convert the string into lower case
    s = s.replace(" ","").lower()
    #check if the string is same forward or backward
    return s == s[::1]

s = input("\nEnter the string: ")
print(is_palindrome(s))