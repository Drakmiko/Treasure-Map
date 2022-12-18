# Michael Nguyen 260970685

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map(treasure_map, n, width, height):
    """ (str, int, int, int) -> str
    The treasure_map string is of length: width * height. Returns the
    nth row of the treasure map. If n is not valid row, returns an empty string.
    
    >>> get_nth_row_from_map('∧..>>>..v', 1, 3, 3)
    '>>>'
    >>> get_nth_row_from_map('∧.<>.<..v..>', 1, 4, 3)
    '.<..'
    >>> get_nth_row_from_map('∧.<>.<..v..>', -1, 4, 3)
    ''
    """
    
    if n >= height or n<0:
        new_map = ''
    
    else:
        character = n * width
        new_width = character + width
        new_map = treasure_map[character:new_width]
        
    return new_map

    
def print_treasure_map(treasure_map, width, height):
    """ (str, int, int) -> Nonetype
    Prints out the treasure map of parameters: width * height.
    
    >>> print_treasure_map('<..vvv..∧', 3, 3)
    <..
    vvv
    ..∧
    >>> print_treasure_map('>.<<.>>.<...∧><', 5, 3)
    >.<<.
    >>.<.
    ..∧><
    >>> print_treasure_map('<>>.', 2, 2)
    <>
    >.
    """
    original_width = width
    index= 0
    for i in range (height):
        print(treasure_map[index:width])
        index += original_width
        width += original_width
        
def change_char_in_map(treasure_map, row, column, c, width, height):
    """ (str, int, int, strt, int, int) -> str
    Takes treasure_map string of length: width * height. Changes treasure_map string
    at row and column inputs with string c. If row or columns are out of bounds, returns
    treasure map string unchanged.

    >>> change_char_in_map('.........', 1, 1, 'X', 3, 3)
    '....X....'
    >>> change_char_in_map('.........', 1, 4, 'X', 3, 3)
    '.........'
    >>> change_char_in_map('....>>>>....', 2, 2, '+', 4, 3)
    '....>>>>..+.'
    """
    
    if row < height and column < width:
        row_index = row * width
        character = row_index + column 
        treasure_map = treasure_map[0: character] + c + treasure_map[character + 1:]
    return treasure_map
    
def get_proportion_travelled(treasure_map):
    """ (str) -> float
    Returns the percentage of BREADCRUMB_SYMBOL from the total characters in the
    treasure_map string rounded to two decimal places.
    
    >>> get_proportion_travelled('.X..X.XX.')
    0.44
    >>> get_proportion_travelled('.XXXXXX.')
    0.75
    >>> get_proportion_travelled('..')
    0.0
    """
    
    total_characters = 0
    index = 0
    while index < len(treasure_map):
        if treasure_map[index] == BREADCRUMB_SYMBOL:
            total_characters += 1
        index += 1
    return round(total_characters/len(treasure_map),2)

def get_nth_map_from_3D_map(treasure_map, n , width, height, depth):
    """ (str, int, int, int, int) -> str
    Returns the nth map of a 3d treasure_map string of parameters:
    width * height * depth. If n is out of bounds, then returns empty string.
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2)
    '.X.XXX.X.'
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 1, 3, 3, 2)
    '.v.vXv.v.'
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 5, 3, 3, 2)
    ''
    """
    
    if n >= depth:
        new_map = ''
    
    else:
        map_size = width * height
        index = n * map_size
        nth_map = index + map_size
        new_map = treasure_map[index:nth_map]
    
    return new_map

def print_3D_treasure_map(treasure_map, width, height, depth):
    """ (str, int, int, int) -> Nonetype
    Prints out treasure_map string of size: width * height * depth.
    
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 3, 3, 2)
    .X.
    XXX
    .X.

    .v.
    vXv
    .v.
    >>> print_3D_treasure_map('><..><<<<>∧∧', 2, 3, 2)
    ><
    ..
    ><
    
    <<
    <>
    ∧∧
    >>> print_3D_treasure_map('∧∧....>><>∧<><∧', 5, 1, 3)
    ∧∧...

    .>><>

    ∧<><∧
    """
    original_width = width
    index= 0
    for j in range (depth):
        for i in range (height):
            print(treasure_map[index:width])
            index += original_width
            width += original_width
        if j == depth - 1:
            break
        print("")
    
def change_char_in_3D_map(treasure_map, row, column, depth_index, c, width, height, depth):
    """ (str, int, int, int, str, int, int, int) -> str
    Takes treasure_map string of dimensions width * height * depth. Returns a copy of
    treasure_map string with the character at index row, column, depth to the character c.
    
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    >>> change_char_in_3D_map('..>><>∧><..><', 0, 0, 1, '%', 3, 2, 2)
    '..>><>%><..><'
    >>> change_char_in_3D_map('..>><>∧><..><', 0, 4, 1, '%', 3, 2, 2)
    '..>><>∧><..><'
    """
    if row < height and column < width and depth_index < depth:
        row_index = row * width
        map_size = width * height
        single_map = row_index + column
        character = single_map + map_size * depth_index
        treasure_map = treasure_map[0: character] + c + treasure_map[character + 1:]
    return treasure_map

    
        
    
    