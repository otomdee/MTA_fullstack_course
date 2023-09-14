
#dict of x values
x_dict = {"x1":1, "x2":2, "x3":3, "x4":4, "x5":5, "x6":6, "x7":7, "x8":8, "x9":9}
#dict of r values
r_dict = {"r1":0, "r2":0, "r3":0, "r4":0, "r5":0, "r6":0, "r7":0, "r8":0, "r9":0}

def print_board():
    print("|", x_dict["x1"],"|",x_dict["x2"],"|",x_dict["x3"],"|"," \n|",x_dict["x4"],"|",x_dict["x5"],"|",x_dict["x6"],"|"," \n|",x_dict["x7"],"|",x_dict["x8"],"|",x_dict["x9"],"|")

#scoring logic
def scoring():    
    for i in x_dict:
        if x_dict[i] == "X":
            i_to_r = i.replace("x","r")
            r_dict[i_to_r] = 10
        #elif i == "O":
            #r_dict[i] = 20
        
r_dict_list = list(r_dict.values())
win_or_lose = False

#winning logic
def win_logic():
    global win_or_lose
    global r_dict_list
    r_dict_list = list(r_dict.values())
    #check rows for X
    
    if sum(r_dict_list[:3]) == 30:
        print("X wins!")
        win_or_lose = True
    elif sum(r_dict_list[3:6]) == 30:
        print("X wins!")
        win_or_lose = True
    elif sum(r_dict_list[6:]) == 30:
        print("X wins!")
        win_or_lose = True
    #check columns
    
def p1_play():
    global win_or_lose
    global r_dict_list
    r_dict_list = list(r_dict.values())
    p1_input_str = input("Pick a number to play(X): ")
    p1_input = int(p1_input_str)
    x_dict["x{}".format(p1_input)] = "X"
    #print the current board
    print_board()
    scoring()
    win_logic()
    if win_or_lose == True:
        print("Congrats, X wins!")
        
        
def p2_play():        
    global win_or_lose
    global r_dict_list
    r_dict_list = list(r_dict.values())
    p2_input_str = input("Pick a number to play(O): ")
    p2_input = int(p2_input_str)
    x_dict["x{}".format(p2_input)] = "O"

    print_board()
    scoring()
    win_logic()
    if win_or_lose == True:
        print("Congrats, O wins!")

print_board()
while win_or_lose == False:
    p1_play()
    if win_or_lose == True:
        break
    p2_play()

