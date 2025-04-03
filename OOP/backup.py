import random
import os
import time


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._board = self.random_state(width = self.width, height = self.height)
        
    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, new_board):
        if isinstance(new_board, list) and all(isinstance(i, list) for i in new_board):
            self._board = new_board
        else:
            raise ValueError("Board must be a 2d array")
        
    def dead_state(self, width, height):
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

        Returns:
            2D-Grid: 2d grid full of zeros and ones placed randomly
        """
        state = self.dead_state(width, height)

        for row in range(len(state)):
            for index in range(len(state[row])):
                random_num = random.random()
                if random_num >= 0.2:
                    state[row][index] = 0
                else:
                    state[row][index] = 1
        
        return state
    
    def next_board_state(self, board_state):
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

    def render(self, board_state):
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
    
class Game:
    def __init__(self, width, height, state=None,sleep_time=None):
        self.board_object = Board(width, height)
        self.board = self.board_object.board
        self._state = False
        self.sleep_time = sleep_time
    
    
        
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, new_state):
        if type(new_state) is bool:
            self._state = new_state
        else:
            raise ValueError("State must be a boolean")
        
        
        
    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, new_board):
        if isinstance(new_board, list) and all(isinstance(i, list) for i in new_board):
            self._board = new_board
        else:
            raise ValueError("Board must be a 2d array")
        
    def run(self):
        alive = True
        while alive:
            alive_cells = sum(_.count(1) for _ in self.board)
            # Check if any cells are alive
            if alive_cells < 1:
                print("Life ended...")
                alive = False
            # Formated board
            rendered_board =  self.board_object.render(self.board)
            print(rendered_board)
            # Check for infinite loop
            if self.board == self.board_object.next_board_state(self.board) and alive == True:
                print("Infinite recursion hit..")
                return
            
            self.board = self.board_object.next_board_state(self.board)
            time.sleep(self.sleep_time if self.sleep_time else 2)


g = Game(10, 10)
g.run()














































































































import random
import os
import time


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Create initial random board and its render
        self.random_state(width = self.width, height = self.height)
        self.render()

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

        Returns:
            2D-Grid: 2d grid full of zeros and ones placed randomly
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
        """Generate the next board state after 1 round of game of life

        Args:
            board_state (2D grid): grid of ones and zeros

        Returns:
            2D-grid: 2d grid with next round of game of life
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

    def render(self):
        """Render the board to well readable format

        Args:
            board_state (2D grid): 2d grid of ones and zeros to render

        Returns:
            string: Formated grid
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
        self.board = Board(width, height)
        self._state = False
        self.sleep_time = sleep_time
    
    
        
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, new_state):
        if type(new_state) is bool:
            self._state = new_state
        else:
            raise ValueError("State must be a boolean")
        
        

    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, new_board):
        if isinstance(new_board, list) and all(isinstance(i, list) for i in new_board):
            self._board = new_board
        else:
            raise ValueError("Board must be a 2d array")


        
    def run(self):
        alive = True
        while alive:
            alive_cells = sum(_.count(1) for _ in self.board)
            # Check if any cells are alive
            if alive_cells < 1:
                print("Life ended...")
                alive = False
            # Formated board
            rendered_board =  self.board_object.render(self.board)
            print(rendered_board)
            # Check for infinite loop
            if self.board == self.board_object.next_board_state(self.board) and alive == True:
                print("Infinite recursion hit..")
                return
            
            self.board = self.board_object.next_board_state(self.board)
            time.sleep(self.sleep_time if self.sleep_time else 2)


g = Game(10, 10)
g.run()