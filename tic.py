class state:
    key =[" "," "," "," "," "," "," "," "," "]
    turn = True
    
    def __init__(self,x=None,symb=None,father=None,turns = True):
        if father:
            self.key = father.key.copy()
            self.key[x]=symb
            self.turn = turns
    
    def possible(self):
        poss =[]
        if self.turn:
            symb='X'
        else:
            symb='O'

        for i in range(9):
            if self.key[i]==' ':
                poss.append(state(i,symb,self,not self.turn))
        
        return poss



def is_win(p):
    x = p.key
    if x[0]=='X'and x[1]=='X' and x[2]=='X':
        return 10
    elif x[3]=='X'and x[4]=='X' and x[5]=='X':
        return 10
    elif x[6]=='X'and x[7]=='X' and x[8]=='X':
        return 10
    elif x[0]=='X'and x[3]=='X' and x[6]=='X':
        return 10
    elif x[1]=='X'and x[4]=='X' and x[7]=='X':
        return 10
    elif x[2]=='X'and x[5]=='X' and x[8]=='X':
        return 10
    elif x[0]=='X'and x[4]=='X' and x[8]=='X':
        return 10
    elif x[2]=='X'and x[4]=='X' and x[6]=='X':
        return 10
    elif x[0]=='O'and x[1]=='O' and x[2]=='O':
        return -10
    elif x[3]=='O'and x[4]=='O' and x[5]=='O':
        return -10
    elif x[6]=='O'and x[7]=='O' and x[8]=='O':
        return -10
    elif x[0]=='O'and x[3]=='O' and x[6]=='O':
        return -10
    elif x[1]=='O'and x[4]=='O' and x[7]=='O':
        return -10
    elif x[2]=='O'and x[5]=='O' and x[8]=='O':
        return -10
    elif x[0]=='O'and x[4]=='O' and x[8]=='O':
        return -10
    elif x[2]=='O'and x[4]=='O' and x[6]=='O':
        return -10
    elif " " not in x:
        return 0
    else :
        return 30


def evaluate(S):
    P = S.possible()
    Score =[]

    if len(P)==0 or is_win(S) != 30:
        return(is_win(S))
    else:
        for i in P:
            temp =evaluate(i)
            Score.append(temp)

        if S.turn:
            return max(Score)
        else:
            return min(Score)

def drawBoard(x):
    board = x.key
    
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def next(X):
    Q = X.possible()
    poss =[]
    
    for i in Q:
        if is_win(i)==10:
            return i
        else:
            poss.append(evaluate(i))

    g = max(poss)
    x = poss.index(g)
    return Q[x]

def main():
    x = int(input("Who goes first?\n1.Computer\n2.You\nGive Input: "))

    if x==1:
        P = state()
        pointed = next(P)
        drawBoard(pointed)

        while(True):
            x = int(input("Enter your move (1-9): "))-1
            if pointed.key[x] != " ":
                print("Invalid space\n")
                continue
            pointed = state(x,symb='O',father=pointed,turns=True)
            if is_win(pointed)!=30:
                break
            pointed = next(pointed)
            drawBoard(pointed)
            if is_win(pointed)!=30:
                break
        
        result = is_win(pointed)
        if result ==10:
            print("Computer won!!!")
        elif result ==-10:
            print("You won!!!")
        else:
            print("Draw")
    else:
        pointed = state()
        pointed.turn =False
        drawBoard(pointed)

        while(True):
            x = int(input("Enter your move (1-9): "))-1
            if pointed.key[x] != " ":
                print("Invalid space\n")
                continue
            pointed = state(x,symb='O',father=pointed,turns=True)
            if is_win(pointed)!=30:
                break
            pointed = next(pointed)
            drawBoard(pointed)
            if is_win(pointed)!=30:
                break
            
        
        result = is_win(pointed)
        if result ==10:
            print("Computer won!!!")
        elif result ==-10:
            print("You won!!!")
        else:
            drawBoard(pointed)
            print("Draw")
        
if __name__=='__main__':
    main()



