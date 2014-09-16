# -*- coding: cp1252 -*-
def uniqueWordCount():
#    string = "The quick brown fox jumps over the lazy dog."
    string = "The film Gattaca raises some very controversial topics about genetically altering unborn children’s genes. Modifying Childs genes to create the most perfect child possible. Genetically altering unborn babies genes is bad. A parent being given the option to give their child whatever eye, hair, skin color, the Childs height and personality is bad. The way parents are given the option to create their idea child seems very similar to build a bear. Many famous people would never have been given the chance to succeed if they were judged they way they were in the film. People like Stephen Hawking, who had ALS would never get the chance to share his brilliance, or he may not even have ever been born. In cultures where one sex is preferred over others would cause a imbalance. Places like china where boy children are valued more then girls, there would be an imbalance of boys. People who were born to be perfect would also have trouble accepting failure, rather then people who are born naturally learn from their failure and become more successful then genetically created children. Also genetically creating foods is similar to the way children were created in Gattaca. It does have its benefits but is also very controversial. "
    string = string.lower()
    uniqueWords = {}
    uniqueLetters = []
    
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '"', "'"]

    print string

    for word in punctuation:
        string = string.replace(word,"")

    words = string.split(" ")

#   print words
    for i in words:
        if i not in uniqueWords:
            uniqueWords[i] = 1
        else:
            uniqueWords[i] = uniqueWords.get(i)+1

#    print uniqueWords
            
    for items in uniqueWords:
        print "%s: %i" % (items, uniqueWords.get(items))

    
