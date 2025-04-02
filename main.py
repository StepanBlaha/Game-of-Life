import random
import os
import time


def dead_state(width, height):
    """ Create a dead board state
    
    Args:
        width (int): width of the desired field
        
        height (int): height of the desired field

    Returns:
        2D-Grid: 2d grid full of zeros with desired size
    """
    board_state = [[0] * width for i in range(height)]
    return board_state

def random_state(width, height):
    """ Create a random board state
    
    Args:
        width (int): width of the desired field
        
        height (int): height of the desired field

    Returns:
        2D-Grid: 2d grid full of zeros and ones placed randomly
    """
    state = dead_state(width, height)

    for row in range(len(state)):
        for index in range(len(state[row])):
            random_num = random.random()
            if random_num >= 0.2:
                state[row][index] = 0
            else:
                state[row][index] = 1
    
    return state

def next_board_state(board_state):
    """Generate the next board state after 1 round of game of life

    Args:
        board_state (2D grid): grid of ones and zeros

    Returns:
        2D-grid: 2d grid with next round of game of life
    """
    new_state = [[0] * len(board_state[0]) for i in range(len(board_state))]
    for row in range(len(board_state)):
        
        for index in range(len(board_state[row])):
            alive_count = 0
            up = row - 1
            down = row + 1
            left = index - 1
            right = index + 1
            for x in (left, right):
                if 0 <= x < len(board_state[row]):
                    alive_count += board_state[row][x]
            
            for y in (up, down):
                if 0 <= y < len(board_state):
                    alive_count += board_state[y][index]

            for diagonal in ([up, left], [up, right], [down, left], [down, right]):
                if 0 <= diagonal[1] < len(board_state[row]) and  0 <= diagonal[0] < len(board_state):
                    alive_count += board_state[diagonal[0]][diagonal[1]]
                    
            match alive_count:
                case x if 2 > x >= 0 and board_state[row][index] == 1:
                    new_state[row][index] = 0
                    continue
                case x if 4 > x >= 2 and board_state[row][index] == 1:
                    new_state[row][index] = 1
                    continue
                case x if x > 3 and board_state[row][index] == 1:
                    new_state[row][index] = 0
                    continue
                case x if x == 3 and board_state[row][index] == 0:
                    new_state[row][index] = 1
                    continue
    return new_state
                    

            
def render(board_state):
    """Render the board to well readable format

    Args:
        board_state (2D grid): 2d grid of ones and zeros to render

    Returns:
        string: Formated grid
    """

    board = ""
    for row in range(len(board_state)):
        board += "|"
        for index in range(len(board_state[row])):
            
            if board_state[row][index] == 0:
                board += "."
            else:
                board += "#"
        board += "|"
        board += "\n"
    return board


def load_board_state(file_path):
    """Load custom board state

    Args:
        file_path (string): path to file to get the grid from

    Returns:
        2D-grid: formated data from the file
    """
    # Check if file is set and exists
    if not file_path:
        print("Missing file path...")
        return

    if not os.path.isfile(file_path):
        print("Invalid file path...")
        return    
    
    # Get the file content
    f = open(file_path, "r")
    content = f.read()

    # Format the content into board format
    board = []
    row = []
    for i in content:
        if i == "\n":
            board.append(row)
            row = []
        else:
            row.append(int(i))
        
    return board




def Game_of_life(width = 10, height = 10, state = None, sleep_time = None):
    """Run the game of life till no cells are alive

    Args:
        width (int, optional): width of the desired field. Defaults to 10.
        height (int, optional): height of the desired field. Defaults to 10.
        state (2d grid, optional): Initial game board state. Defaults to None.
    """
    
    if state:
        board = state
    else:
        board = random_state(width, height)
    alive = True
    while alive:
        alive_cells = sum(_.count(1) for _ in board)
        if alive_cells < 1:
            alive = False
        rendered_board =  render(board)
        print(rendered_board)
        if board == next_board_state(board) and alive == True:
            print("Infinite recursion hit..")
            return
        board = next_board_state(board)
        time.sleep(sleep_time if sleep_time else 2)

Game_of_life(state=load_board_state("patterns/toad.txt"), sleep_time=10)