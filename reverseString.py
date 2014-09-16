def reverseString(words):
    wordlist = words.split(" ")
    print words[::-1]
    print wordlist[::-1]

string = raw_input("Enter a string: ")
reverseString(string)
