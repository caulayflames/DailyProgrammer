def sumNums(num):
    if num <= 10:
        return num
    else:
        return sumNums(sum([int(i) for i in str(num)]))

def sum_nums(num):
    if num < 10:
        print "=",num
    else:
        
        total = 0
        for i in str(num):
            print i, "+"
            total += int(i)
        print "=",total

    return sum_nums(total)
        
number = raw_input("Enter the number: ")
print sumNums(number)
