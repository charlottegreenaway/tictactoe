import random
import time

def intro():
    print("WELCOME TO TIC TAC TOE!")
    global name
    name=input("What is your name?>>")
    print(" "," 1 "," 2 "," 3 ")
    print("1",["","",""])
    print("2",["","",""])
    print("3",["","",""])
    


def xoro():
    global usersymbol
    global computersymbol
    usersymbol=input("Would you like to be X or O?>>")
    while (usersymbol != "X") and (usersymbol !="x") and (usersymbol !="O") and (usersymbol !="o") and (usersymbol !="0"):
        usersymbol=input("Would you like to be X or O?>>")


    if usersymbol== "X" or usersymbol== "x":# sets comp symbol to opposite of user and discards any variation of Xs or Os
        computersymbol="O" 
        usersymbol="X"
    if usersymbol=="o" or usersymbol=="O" or usersymbol=="0":
        computersymbol="X"
        usersymbol="O"
    #print(computersymbol, usersymbol)




def grid():
    global grid
    grid =[["","",""],
          ["","",""],
          ["","",""]]
    return grid

def answer():
    global answer
    print("\n \n--------------------")
    print("YOUR  TURN \n\n")
    row= int(input("Which row? 1-3>>"))
    
    while row != 1 and row != 2 and row != 3:
        row= int(input("Which row? 1-3>>"))

        
    column= int(input("Which column? 1-3>>"))
    while column != 1 and column != 2 and column != 3:
        column= int(input("Which column? 1-3>>"))
    
    while grid[row-1][column-1] != "":
        print("Please select an untaken slot")
        row= int(input("Which row? 1-3>>"))
        column= int(input("Which column? 1-3>>"))
        while row != 1 and row != 2 and row != 3:
            row= int(input("Which row? 1-3>>"))
            column= int(input("Which column? 1-3>>"))
        while column != 1 and column != 2 and column != 3:
            row= int(input("Which row? 1-3>>"))
            column= int(input("Which row? 1-3>>"))
    grid[row-1][column-1]=usersymbol
    print(grid[0])
    print(grid[1])
    print(grid[2])
    print("--------------------\n")
    winner()
    

def companswer():
    print("\n\n--------------------")
    print("Computers turn")
    print("THINKING...")
    time.sleep(0.5)
    print("THINKING...")
    time.sleep(0.5)
    print("THINKING...")
    time.sleep(0.5)
    rrow= random.randint(1,3)
    ccolumn= random.randint(1,3)
    while grid[rrow-1][ccolumn-1] != "":
        rrow= random.randint(1,3)
        ccolumn= random.randint(1,3)
    grid[rrow-1][ccolumn-1]= computersymbol
    print(grid[0])
    print(grid[1])
    print(grid[2])
    print("--------------------\n")
    winner()

def winner():
    global win
    global who

    if grid[0][0]== usersymbol and grid[0][1]== usersymbol and grid[0][2]== usersymbol:# checks if user won horizontal
        win= True
        who= True
        return True,True
    if grid[1][0]== usersymbol and grid[1][1]== usersymbol and grid[1][2]== usersymbol:
        win= True
        who= True
        return True,True
    if grid[2][0]== usersymbol and grid[2][1]== usersymbol and grid[2][2]== usersymbol:
        win= True
        who= True
        return True,True

    if grid[0][0]== usersymbol and grid[1][0]== usersymbol and grid[2][0]== usersymbol:# checks if user won horizontal
        win= True
        who= True
        return True,True
    if grid[0][1]== usersymbol and grid[1][1]== usersymbol and grid[2][1]== usersymbol:
        win= True
        who= True
        return True,True
    if grid[0][2]== usersymbol and grid[1][2]== usersymbol and grid[2][2]== usersymbol:
        win= True
        who= True
        return True,True

    if grid[0][0]== usersymbol and grid[1][1]== usersymbol and grid[2][2]== usersymbol:# checks if user won diagonal
        win= True
        who= True
        return True,True
    if grid[2][0]== usersymbol and grid[1][1]== usersymbol and grid[0][2]== usersymbol:
        win= True
        who= True

        return True,True
    



        

        
        
    if grid[0][0]== computersymbol and grid[0][1]== computersymbol and grid[0][2]== computersymbol:# checks if comp wins horizontal
        win= True
        who= False
        return True,False
    if grid[1][0]== computersymbol and grid[1][1]== computersymbol and grid[1][2]== computersymbol:
        win= True
        who= False
        return True,False
    if grid[2][0]== computersymbol and grid[2][1]== computersymbol and grid[2][2]== computersymbol:
        win= True
        who= False
        return True,False

    if grid[0][0]== computersymbol and grid[1][0]== computersymbol and grid[2][0]== computersymbol:# checks if comp won horizontal
        win= True
        who= True
        return True,False
    if grid[0][1]== computersymbol and grid[1][1]== computersymbol and grid[2][1]== computersymbol:
        win= True
        who= True
        return True,False
    if grid[0][2]== computersymbol and grid[1][2]== computersymbol and grid[2][2]== computersymbol:
        win= True
        who= True
        return True,False

    if grid[0][0]== computersymbol and grid[1][1]== computersymbol and grid[2][2]== computersymbol:# checks if comp won diagonal
        win= True
        who= True
        return True,False
    if grid[2][0]== computersymbol and grid[1][1]== computersymbol and grid[0][2]== computersymbol:
        win= True
        who= True
        return True,False
    else:
        return False,False

def tied():
    if winner!= True and grid[0][1]!="" and grid[1][1]!="" and grid[2][1]!="" and grid[0][2]!="" and grid[1][2]!="" and grid[2][2]!="" and grid[0][0]!="" and grid[1][0]!="" and grid[2][0]!="":
        return True
    else:
        return False

def main():
    intro()

    xoro()

    grid()

    win= False
    tie=False

    while win!= True and tie != True:
        answer()
        win, who= winner()
        tie=tied()
        if win== True:
            break
        if tie== True:
            break
        companswer()
        win, who= winner()
        tie=tied()
        if win== True:
             break
        if tie== True:
            break
        


        
    if who== True:
        print(name,"wins")
    if who== False:
            print("computer wins!")

    if tie== True:
        print("Its a tie")
main()
