def palindrome(string):
    reverse = string[::-1]
    
    if string == reverse:
        print string, "is a palindrome"
    else:
        print string, "is not a palindrome"

word = raw_input("Enter string: ")
palindrome(word)


