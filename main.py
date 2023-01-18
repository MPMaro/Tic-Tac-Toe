
 # Global Grid
grid = { 1 : ' ', 2 : ' ', 3: ' ',
         4 : ' ', 5 : ' ', 6 : ' ', 
         7 : ' ', 8 : ' ', 9 : ' '}

 # Variables
count = 0		
winner = False		
play = True		
tie = False		
currentplayer = " "
player_details = []	

# Helper functions
def get_player_details(currentplayer):

    if currentplayer == '1':
        return ['2','O']
    else:
        return ['1','X']
    

def print_grid():
    for i in grid:
        print( i, ':', grid[i], ' ', end='')
        if i%3 == 0:
            print()


def win_game(marker, player_id):
    win_positions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for position in win_positions:
        if all(grid[i] == marker for i in position):
            print_grid()
            
            print("Player" + " " + player_id +  " " + "wins!")
            return True

    return False


def insert_input(gridpos, marker):
    if grid[gridpos] == ' ':
        grid[gridpos] = marker
        
    else:
        print("spot taken, pick another number.")

def play_again():
    print("Do you want to play again?, if so type Y")
    option= input()

    if option.upper() == 'Y':
        for x in grid:
            grid[x] = ' '
        return True
    else:
        print("Game Ended")
        return False
    
    
# Main program
while play:

    print_grid()

    player_details = get_player_details(currentplayer)
    currentplayer = player_details[0]
    print("Player" + " " + currentplayer + " " + "Enter a number between 1 and 9")
    input_slot = int(input())

    #Insert'X' or 'O'
    insert_input(input_slot, player_details[1])
    count += 1
    

    winner = win_game(player_details[1], currentplayer)
    if count == 9 and not winner:
        print("It's a Tie")
        tie = True
        print_grid()

    if winner or tie:
        play = play_again()
        if play:
            currentplayer = ''
            count = 0
