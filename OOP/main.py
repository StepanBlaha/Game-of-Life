import random
import os
import time


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._render = None
        self._board = None

        # Create initial random board and its render
        self.random_state(width = self.width, height = self.height)
        self.render_state()

    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, new_board):
        if isinstance(new_board, list) and all(isinstance(i, list) for i in new_board):
            self._board = new_board
        else:
            raise ValueError("Board must be a 2d array")
    
    @property
    def render(self):
        return self._render
    
    @render.setter
    def render(self, new_render):
        if isinstance(new_render, str):
            self._render = new_render
        else:
            raise ValueError("Render must be a string")
        
    @staticmethod
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
    
    def random_state(self, width, height):
        """ Create a random board state
        
        Args:
            width (int): width of the desired field
            
            height (int): height of the desired field

        """
        state = self.dead_state(width, height)

        for row in range(len(state)):
            for index in range(len(state[row])):
                random_num = random.random()
                if random_num >= 0.2:
                    state[row][index] = 0
                else:
                    state[row][index] = 1
        
        # Set protected state
        self.board = state
    
    def next_board_state(self):
        """
        Generate the next board state after 1 round of game of life
        """
        board_state = self.board

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

        self.board = new_state

    def render_state(self):
        """
        Render the board to well readable format
        """
        board_state = self.board
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
        self.render = board
    
class Game:
    def __init__(self, width, height, state=None,sleep_time=None):
        self.board_object = Board(width, height)
        self.sleep_time = sleep_time
    
    def run(self):
        alive = True
        while alive:
            board = self.board_object.board

            # Format render in board object
            self.board_object.render_state()
            # Print the render
            print(self.board_object.render)


            alive_cells = sum(_.count(1) for _ in board)
            # Check if any cells are alive
            if alive_cells < 1:
                print("Life ended...")
                alive = False


            # Create the next step
            self.board_object.next_board_state()
            # Check for infinite recursion
            if board == self.board_object.board and alive == True:
                print("Infinite recursion hit..")
                return
            
            time.sleep(self.sleep_time if self.sleep_time else 0.1)

if __name__ == "__main__":
    Life = Game(10, 10)
    Life.run()