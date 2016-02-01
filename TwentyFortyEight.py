"""
Clone of 2048 game.
"""
from random import randint
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

#_move_init = [[], [(0, 0), (0, 1), (0, 2), (0, 3)], [(4, 0), (4, 1), (4, 2), (4, 3)], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]]

def remzero(line):
    """
    Function that moves all zeros to end in a list.
    """
    origlen = len(line)
    line[:] = filter(None, line)
    line.extend([0] * (origlen - len(line)))
    return line

def add(line):
    """
    Function that add consecutive same elements in list.
    """
    for dummy_i in range(0, len(line)):
        if dummy_i+1 < len(line):
            if  line[dummy_i] == line[dummy_i+1]:
                line[dummy_i] += line[dummy_i+1]
                line[dummy_i+1] = 0
    return line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line_result = list(line)
    return remzero(add(remzero(line_result)))

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        print "INIT"
        self._height = grid_height
        self._width = grid_width
        self._grid = [[0 for dummy_x in range(self._width)] for dummy_x in range(self._height)]

        self._move_init = [[], [(0, dummy_x) for dummy_x in range(self._width)], [(self._height-1, dummy_x) for dummy_x in range(self._width)], [(dummy_x,0) for dummy_x in range(self._height)], [(dummy_x, self._width-1) for dummy_x in range(self._height)]]

    def reset(self):
        """
        Reset the game so the _grid is empty except for two
        initial tiles.
        """
        print "Reset"
        # replace with your code
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the _grid for debugging.
        """
        # replace with your code
        return ('\n'.join([''.join([(str(item) + " ") for item in row])
                           for row in self._grid]))

    def get_grid_height(self):
        """
        Get the _height of the board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the _width of the board.
        """
        # replace with your code
        return self._width

    def traverse_grid(self, start_cell, direction, side):
        """
        Traverse the _grid in given direction and get the elements
        as a list.
        """
        #print direction
        list_out = []#[self._grid[start_cell[0]][start_cell[1]]]
        #print "trav"
        #print side
        #print direction, start_cell
        if side < 3:
            num_steps = self._height
        else:
            num_steps = self._width
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            #print "Processing cell", (row, col)
            list_out.append(self._grid[row][col])
        return list_out

    def traverse_grid_set(self, merge_list, start_cell, direction, side):
        """
        Traverse the _grid in given direction and set the elements
        as given in the merge_list.
        """
        #print direction
        #print "travs"
        #print side
        #print merge_list
        old_list = []
        if side < 3:
            num_steps = self._height
        else:
            num_steps = self._width
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            #print "setting cell", (row, col)
            old_list.append(self.get_tile(row, col))
            self.set_tile(row, col, merge_list[step])
            #self._grid[row][col] = merge_list[step];
        #print "len comp"
        #print len([x for x in merge_list if x>0])
        #print len([x for x in old_list if x>0])
        if merge_list != old_list:
            print "found change"
            return False
        return True

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        #print direction
        #print _move_init[direction]
        #print self.traverse_grid(_move_init[direction][0], OFFSETS[direction], direction)
        # replace with your code
        out = True
        for ele in self._move_init[direction]:
            #print ele
            out = self.traverse_grid_set(merge(self.traverse_grid(ele, OFFSETS[direction], direction)), ele, OFFSETS[direction], direction) and out
        if out is False:
            print "Adding tile"
            self.new_tile()
        else:
            print "no tile added"

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        #print "Entered new tile"
        rand_seed = randint(1, 10)
        check = False
        while check != True:
            rand_row = randint(0, self._height-1)
            rand_col = randint(0, self._width-1)
            if self._grid[rand_row][rand_col] != 0:
                continue
            else:
                check = True
            print rand_col, rand_row, rand_seed
            if rand_seed < 10:
                self._grid[rand_row][rand_col] = 2
            else:
                self._grid[rand_row][rand_col] = 4
        #print self

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(2, 2))

