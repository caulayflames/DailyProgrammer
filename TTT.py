def makeMove(player, board, position):
    if  not board[position]:
	    board[position] = player
	    return True
    else:
        return False
    return board


def hasAll(listof3, player):
    for item in listof3:
	    if item is not player:
		    return False
    return True

def winTest(player, board):
    for x in [0,3,6]:
        listof3 = board[x:x+3]
        if hasAll(listof3, player):
            return True
    for x in [0,1,2]:
        listof3 = board[x::3]
        if hasAll(listof3, player):
            return True
    listof3 = board[0::4]
    if hasAll(listof3, player):
        return True
    listof3 = board[2:7:2]
    if hasAll(listof3, player):
        return True
    return False

board = [None]*9
player = 'X '

while True:
    while player != None:
        print "------------------------------" #displays exisitng board to players
        print "       Board:           Key:  "
        print "%s = [0, 1, 2]" % board[:3]
        print "%s = [3, 4, 5]" % board[3:6]
        print "%s = [6, 7, 8]" % board[6:9]
        print "------------------------------"
        try:
            position = int(raw_input(
                "It is %s's move. Please enter an unoccupied position:" % player))
            assert position <= 8 and position >= 0
        except:
            print 'error getting input. Try again.'
            continue
        
        if makeMove(player, board, position):
            if winTest(player, board):
                print " --------------"
                print "|Player %sWins!|" % player
                print " --------------"
                player = None
                break
            if None not in board:
                print " -----------"
                print "|It's a Tie!|"
                print " -----------"
                player = None
                break
            player = {'X ':'O ','O ':'X '}[player]
        else:
            print "That is not a valid position. Try again."


    while player == None:
        try:
            rematch = raw_input( "Game Over. Would you like to play again? y/n?: ")
        except:
            print "That is not 'y' or 'n'. Please try again."
            continue
        if rematch == 'y':
            board = [None]*9
            player = 'X '
        elif rematch == 'n':
            print "Thank you for playing!"
            break
        else:
            print "Only the letters 'y' or 'n' are valid answers. Please try again."