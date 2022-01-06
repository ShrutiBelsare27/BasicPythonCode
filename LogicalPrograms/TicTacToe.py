'''
@Author: Shruti
@Date: 2022-1-4
@Last Modified by: Shruti
@Last Modified time: 2022-1-6
@Title : To play tic-tac-toe game
'''


def start():
    board = {'1': ' ',  '2': ' ',  '3': ' ',
         '4': ' ',  '5': ' ',  '6': ' ',
         '7': ' ',  '8': ' ',  '9': ' '}

    player=1 
    total_moves=0   #count moves1
    end_check=0


    def check():
    #checking moves of player 1
    #for horizontal 
        if board['1']== 'X' and board['2']== 'X' and board['3']== 'X':
            print("player one won")
            return 1
        if board['4']== 'X' and board['5']== 'X' and board['6']== 'X':
            print("player one won")
            return 1
        if board['7']== 'X' and board['8']== 'X' and board['9']== 'X':
            print("player one won")
            return 1
    
    #diagonal
        if board['1']== 'X' and board['5']== 'X' and board['9']== 'X':
            print("player one won")
            return 1
    
    #vertical
        if board['1']== 'X' and board['4']== 'X' and board['7']== 'X':
            print("player one won")
            return 1
        if board['2']== 'X' and board['5']== 'X' and board['8']== 'X':
            print("player one won")
            return 1
        if board['3']== 'X' and board['6']== 'X' and board['9']== 'X':
            print("player one won")
            return 1
    
    
    #checking moves player 2
    #horizontal
        if board['1']== 'O' and board['2']== 'O' and board['3']== 'O':
            print("player two won")
            return 1
        if board['4']== 'O' and board['5']== 'O' and board['6']== 'O':
            print("player two won")
            return 1
        if board['7']== 'O' and board['8']== 'O' and board['9']== 'O':
            print("player two won")
            return 1
    
    #diagonal
        if board['1']== 'O' and board['5']== 'O' and board['9']== 'O':
            print("player two won")
            return 1
    #vertical
        if board['1']== 'O' and board['4']== 'O' and board['7']== 'O':
            print("player two won")
            return 1
        if board['2']== 'O' and board['5']== 'O' and board['8']== 'O':
            print("player two won")
            return 1
        if board['3']== 'O' and board['6']== 'O' and board['9']== 'O':
            print("player two won")
            return 1
    
        return 0


    while True:
        total_moves=0
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        end_check=check()
        if total_moves==9 or end_check==1:
             break
    
        while True: #input from player
            if player == 1:
                p1=input("Player one   ")
        
                if p1 in board and  board[p1] == ' ': #to check valid key and white space only
                    board[p1] = 'X'
                    player=2
                    break
                else:
                    print("invalid input,plz try again")
                    continue
            
            else:  #player 2
            
                p2=input("Player two")
                if p2 in board and board[p2] == ' ':
                    board[p2] = 'O'
                    player=1
                    break
                else:
                    print("invalid input,plz try again")
                    continue    
        total_moves+=1
    
        print('* * * * * * * * *')  
        print()   



    flag=True

    while flag:
        print("Do you want to play again?(y/n)")
        response=input("Enter y for yes ,n for no ")
        if(response=='y'):
            start()
    
        else:   
        
            flag=False
start()
    
        
        


