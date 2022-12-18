# Michael Nguyen 260970685
import random as r
import treasure_utils as t

def generate_treasure_map_row(width, boolean):
    """ (int, bool) -> str
    Generates a string of length 'width' with a each symbol having
    5/6 chances of being a MOVEMENT_SYMBOLS or 1/6 chances of being an EMPTY_SYMBOL.
    If bool is True, there is a 50% that one off the characters in the string is replaced
    with a MOVEMENT_SYMBOL_3D.
   
    >>> random.seed(9001)
    >>> generate_treasure_map_row(10, False)
    '.v.v>vv>^<'
    >>> generate_treasure_map_row(10, True)
    '∧∧<<<^^vv>'
    >>> generate_treasure_map_row(10, True)
    '><>v.v.<|v'
    """
    
    treasure_map = ""
    for i in range (width):
        chances = r.randint(1, 6)
        if chances == 1:
            treasure_map += t.EMPTY_SYMBOL
        else:
            chances = r.randint(0,3)
            treasure_map += t.MOVEMENT_SYMBOLS[chances]
    if boolean and r.randint(1,2) == 1:
        index = r.randint(0,width-1)
        treasure_map = treasure_map[0:index] + t.MOVEMENT_SYMBOLS_3D[r.randint(0,1)] \
        + treasure_map[index + 1:]
    return treasure_map

def generate_treasure_map(width, height, boolean):
    """ (int, int, bool) -> str
    Generates a treasure map string of length: width * height having
    5/6 chances of being a MOVEMENT_SYMBOLS or 1/6 chances of being an EMPTY_SYMBOL.
    If bool is True, there is a 50% that one off the characters in each row is replaced
    with a MOVEMENT_SYMBOL_3D.
    
    >>> random.seed(9001)
    >>> generate_treasure_map(3, 3, False)
    '>.v.v>vv>'
    >>> generate_treasure_map(3, 3, True)
    '>^<^|<<<^'
    >>> generate_treasure_map(3, 3, True)
    '>.><>v.|.'
    """
    length = width * height
    treasure_map = t.MOVEMENT_SYMBOLS[0]
    for i in range (length - 1):
        chances = r.randint(1, 6)
        if chances == 1:
            treasure_map += t.EMPTY_SYMBOL
        else:
            chances = r.randint(0,3)
            treasure_map += t.MOVEMENT_SYMBOLS[chances]
            
    for i in range (height):
        if boolean and r.randint(1,2) == 1:
            if i == 1:
                index = i * r.randint(1, width - 1)
            else:
                index = (width * (i - 1)) + r.randint(0,width -1)
            treasure_map = treasure_map[0:index] + t.MOVEMENT_SYMBOLS_3D[r.randint(0,1)] + \
                            treasure_map[index + 1:]
    return treasure_map

def generate_3D_treasure_map(width, height, depth):
    """ (int, int, int) -> str
    Generates a treasure map string of length: width * height * depth.
    There is a 5/6 chances of being a MOVEMENT_SYMBOLS or 1/6 chances of being an EMPTY_SYMBOL.
    There is also a 50% that one off the characters in each row is replaced
    with a MOVEMENT_SYMBOL_3D. The first character of the first map if a right pointing
    MOVEMENT_SYMBOLS.
    
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(3, 3, 3)
    '>|v.v>vv>^<^^<|<^^v|>><>|.v'
    >>> generate_3D_treasure_map(2, 4, 2)
    '>>.>v**<*^^<<<<*'
    >>> generate_3D_treasure_map(5, 2, 3)
    '>^<<^.v.<<.<v<|><^.^>>><^<<v>*'
    """
    length = width * height * depth
    treasure_map = t.MOVEMENT_SYMBOLS[0]
    for i in range (length - 1):
        chances = r.randint(1, 6)
        if chances == 1:
            treasure_map += t.EMPTY_SYMBOL
        else:
            chances = r.randint(0,3)
            treasure_map += t.MOVEMENT_SYMBOLS[chances]
    
    occurances_3D = height * depth
    i = 1
    while i <= occurances_3D:
        if r.randint(1, 2) == 1:
            if i == 1:
                index = i * r.randint(1, width - 1)
            else:
                index = (width * (i - 1)) + r.randint(0,width -1)
            treasure_map = treasure_map[0:index] + t.MOVEMENT_SYMBOLS_3D[r.randint(0,1)] \
            + treasure_map[index + 1:]
        i += 1
    return treasure_map

def follow_trail(treasure_map, row, column, depth_index, width, height, depth, number_of_tiles):
    """ (str, int, int, int, int, int, int, int) -> str
    Takes a treasure_map string of parameters width * height * depth.
    Follows map trail according to MOVEMENT_SYMBOLS, EMPTY_SYMBOL,
    MOVEMENT_SYMBOLS_3D and TREASURE_SYMBOL, and  stops
    when it encounters a BREADCRUMB_SYMBOL or number_of_tiles has been reached.
    Starts trail at starting_row, column depth_index indices.
    Prints the number of treasures collected and symbols visited
    and returns the treasure_map string with all MOVEMENT_SYMBOLS
    followed into BREADCRUMB_SYMBOL.  If number_of_tiles is -1,
    trail only stops when BREADCRUMB_SYMBOL is encountered.
    
    >>> follow_trail('>>*..v>+>+>|', 1, 2, 0, 3, 2, 2, 100)
    Treasures collected: 1
    Symbols visited: 5
    '>>X..XX+X+>|'
    >>> follow_trail('>>v..v', 0, 0, 0, 3, 2, 1, -1)
    Treasures collected: 0
    Symbols visited: 4
    'XXX..X'
    >>> follow_trail('>>v..v', 5, 1, 0, 3, 2, 1, -1)
    '>>v..v'
    """
    
    index = (row * width + column) + depth_index * width * height
    symbols_visited = 0
    treasure_visited = 0
    i = 0
    number_of_tiles_to_travel = number_of_tiles
    
    if row < height and column < width and depth_index < depth:    
        if number_of_tiles == -1:
            number_of_tiles_to_travel = 1
        while i < number_of_tiles_to_travel and treasure_map[index] != t.BREADCRUMB_SYMBOL:
            if number_of_tiles == -1:
                i -= 1
            symbols_visited += 1
                
            if t.MOVEMENT_SYMBOLS.find(treasure_map[index]) != -1 or \
            t.MOVEMENT_SYMBOLS_3D.find(treasure_map[index]) != -1:
                movement = treasure_map[index]
                treasure_map = treasure_map[0:index] + t.BREADCRUMB_SYMBOL + treasure_map[index + 1:]
                
            if treasure_map[index] == t.TREASURE_SYMBOL:
                treasure_visited += 1
                    
            if movement == t.MOVEMENT_SYMBOLS_3D[0]:
                index += (width * height)
            elif movement == t.MOVEMENT_SYMBOLS_3D[1]:
                index -= (width * height)
                    
            if movement == t.MOVEMENT_SYMBOLS[0]:
                if (index + 1) % width == 0:
                    index -= (width -1)
                else:
                    index += 1
            elif movement == t.MOVEMENT_SYMBOLS[1]:
                if index % width == 0:
                    index += (width - 1)
                else:
                    index -= 1
            elif movement == t.MOVEMENT_SYMBOLS[2]:
                if index < width * height and index >= (width * height) - width: 
                    index -= width * (height - 1)
                else:
                    index += width
            elif movement == t.MOVEMENT_SYMBOLS[3]:
                if index < width:
                    index += width * (height - 1)
                else:
                    index -= width
            i += 1
        print("Treasures collected:", treasure_visited)
        print("Symbols visited:", symbols_visited)
    return treasure_map
    
