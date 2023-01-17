grid = { 1 : ' ', 2 : ' ', 3: ' ',
         4 : ' ', 5 : ' ', 6 : ' ', 
         7 : ' ', 8 : ' ', 9 : ' '}

count = 0	
winner = False	
play = True		
tie = False
currentplayer = ''	
player_details = []


def player_deatails(cuurentplayer):
    if cuurentplayer == "1":
        return ["2","O"]
    else:
        return ["1", "X"]
    
  
  # Prints the board  
def print_grid():
    for i in range(len(grid)):
        print( i, ":", grid[i], " ")
        if i%3 == 0:
            print()
            
        
        
def win_checker(marker, playerid):
    if grid[1] == marker and grid[2] == marker and grid[3] == marker or \
    grid[1] == marker and grid[4] == marker and grid[7] == marker or \
    grid[1] == marker and grid[5] == marker and grid[9] == marker or \
    grid[2] == marker and grid[5] == marker and grid[8] == marker or \
    grid[3] == marker and grid[5] == marker and grid[7] == marker or \
    grid[3] == marker and grid[6] == marker and grid[9] == marker or \
    grid[4] == marker and grid[5] == marker and grid[6] == marker or \
    grid[7] == marker and grid[8] == marker and grid[9] == marker:
        print_grid()
        print("Player :" + playerid + "wins")
        return True
    
    else: 
        return False
    
    
def input(gridpos, marker):
    """Function for capturing user inputs"""
    while grid[gridpos] != ' ':
        print("spot taken, pick another no.")
        grid = int(input())
    grid[gridpos] = marker