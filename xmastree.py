def tree(base, trunk, leaves):
    for x in range(1,base+1,2):
        print ' '*(base-x/2)+leaves*x
    print ' '*(base-3/2)+trunk*3
