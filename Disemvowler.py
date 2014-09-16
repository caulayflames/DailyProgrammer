"""
" DailyProgrammer Challenge #149
" Input: A string consisting of a series of words to disemvowel.
"        It will be all lowercase (letters a-z) and without punctuation.
"        The only special character you need to handle is spaces.
" Output: Two strings, one of the disemvoweled text (spaces removed),
"         and one of all the removed vowels.
"""

text = raw_input("Enter String: ").replace(" ","")
vowels = 'aeiou'

print "".join(letter for letter in text if letter not in vowels)
print "".join(letter for letter in text if letter in vowels)
