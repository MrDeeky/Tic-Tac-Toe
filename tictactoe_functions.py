import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """

    return min_value <= value <= max_value

    
def game_board_full(game_board):
    """ (str) -> bool
    
    Return True if the EMPTY character cannot be found in the game_board.
    
    >>> game_board_full('XOXOXOXOX')
    True
    >>> game_board_full('XOX-')
    False
    """
    
    return game_board.find(EMPTY) == -1
    
def get_board_size(game_board):
    """ (str) -> int
    
    Return the length of the game board by square rooting the length of the 
    string.
    
    >>> get_board_size('XOXOXOXOX')
    3
    >>> get_board_size('XOXO')
    2
    """
    
    return int(math.sqrt(len(game_board)))

def make_empty_board(board_size):
    """ (int) -> str
    
    Return a string with EMPTY characters according to the board_size.
    
    >>> make_empty_board(3)
    '---------'
    >>> make_empty_board(4)
    "----------------"
    """
    
    return EMPTY * (board_size ** 2)

def get_position (row_index, column_index, board_size):
    """ (int, int, int) -> int
    
    Return position of the cell in the given row_index and column_index
    according to the board_size.
    
    >>> get_position (3, 3, 5)
    12
    >>> get_position (3, 5, 6)
    16
    """
    
    return (row_index - 1) * board_size + column_index - 1

def make_move (game_piece, row_index, column_index, game_board):
    """ (str, int, int, str) -> str
    
    Return a new game_board after a game_piece is placed in the specified
    row_index and column_index.
    
    >>> make_move ('X', 2, 1, 'XO---XOXO')
    'XO-X-XOXO'
    >>> make_move ('O', 1, 2, 'X--O')
    'XO-O'
    """
    
    board_size = get_board_size (game_board)
    cell_position = get_position (row_index, column_index, board_size)
    return game_board [:cell_position] + game_piece \
           + game_board [cell_position + 1:] 

def extract_line (game_board, direction, board_index):
    """ (str, str, int) -> str
    
    Return a string that contains the game pieces from the game_board starting
    from the given board_index and then following the given direction.
    
    >>> extract_line ('XOXO', 'down', 1)
    'XX'
    >>> extract_line ('-OX-O-XO-', 'up_diagonal', 3)
    'XOX'
    """
    
    board_size = get_board_size (game_board)
    if direction == 'across':
        cell_position = get_position (board_index, 1, board_size)
        line_extracted = game_board [cell_position: cell_position + board_size]
    elif direction == 'down':
        line_extracted = game_board [board_index - 1:: board_size]
    elif direction == 'down_diagonal':
        line_extracted = game_board [:: board_size + 1]
    else:
        line_extracted = game_board [board_size - 1: board_size ** 2 \
                                     - board_size + 1: board_size - 1] [::-1]
    return line_extracted