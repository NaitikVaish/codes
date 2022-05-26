def reverse(str):
    str1=str[::-1]
    if str==str1:
        print('palindrome')
    else:
        print('not palindrome')
str=input()
reverse(str)
