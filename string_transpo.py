def string_transpo():
    num_strings = raw_input("Enter Number of Strings to transpose: ")
    words = []
    max_len = 0
    
    for i in range(int(num_strings)):
        word = raw_input()
        words.append(word)
        if len(word) > max_len:
            max_len = len(word)

    print words
    print max_len

    words = [i + (' ' * (max_len - len(i))) for i in words]

    for i in range(max_len):
        for j in range(int(num_strings)):
            print words[j][i],
        print
    
string_transpo()
