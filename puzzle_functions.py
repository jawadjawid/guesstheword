""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
  
    if player_one_turn:
        return P1
    else:
        return P2


def get_winner(player_one_score: int, player_two_score: int) -> str:
    """ Return the winner of the game, based on who is higher, player_one_score
    or player_two_score"
    
    Precondition: player_one_score <= Maximum possible points in the game
                  player_two_score <= Maximum possible points in the game
                  0 < player_one_score + player_two_score      
    
    >>> get_winner(14, 16)
    "P2_WINS"
    >>> get_winner(8, 8)
    "TIE"
    """
    
    if player_one_score > player_two_score:
        return P1_WINS
    elif player_one_score < player_two_score:
        return P2_WINS
    else:
        return TIE
    

def reverse(string: str) -> str:
    """Return the reverse of a string
    
    >>>reverse("Anya")
    "aynA"
    >>>reverse("Kaveh")
    "hevaK"
    """
    
    return string[-1::-1]


def get_row(puzzle: str, row_num: int) -> str:
    """Return the row in a specific puzzle by providing the row_num
    
    Precondition: Puzzle must have the same number of charecters in each row.
                  0 <= row_num <= Total number of rows in the puzzle
    
    >>>get_row('abcd\nefgh\nijkl\n', 1)
    'efgh'
    >>>get_row('abcd\nefgh\nijkl\n', 2)
    'ijkl'
    """
    # This return statment adds 1 to the row_length to get rid of spaces
    # between lines. And it ends with the row_length only because Python dosent
    # include the closing charecter in an index.
    
    return puzzle[(get_row_length(puzzle) + 1) * row_num : row_num * \
                     (get_row_length(puzzle) + 1) + get_row_length(puzzle)]
     

def get_factor(direction: str) -> int:
    """Return the facotr based on the direction
    
    Precondition: Direction must be one of thesse posibilities
                  UP, DOWN, FORWARD, BACKWARD.
    
    >>>get_factor(UP)
    4
    >>>get_factor(DOWN)
    2
    """
    
    if direction == FORWARD:
        return FORWARD_FACTOR
    elif direction == DOWN:
        return DOWN_FACTOR
    elif direction == BACKWARD:
        return BACKWARD_FACTOR
    else:
        return UP_FACTOR
    

def get_points(direction: str, words_left: int) -> int:
    """ Return points earned in a specific direction when
    a certian amount of words_left
    
    Precondition: Direction must be one of thesse posibilities
                  UP, DOWN, FORWARD, BACKWARD.
                  0  < words_left <= Total number of words (THRESHOLD)
    
    >>> get_points(BACKWARD, 5)
    15
    >>> get_points(BACKWARD, 2)
    24
    """
    
    # The conditional statments below explain how the score earned depending on
    # word_left. For example guessing a word at the beginning is easier so you
    # earn less points. While guessing the last word can give you a BOUNS.
    
    if words_left >= THRESHOLD:
        return THRESHOLD * get_factor(direction)
    elif words_left == 1:
        return (2 * THRESHOLD - words_left) * get_factor(direction) + BONUS
    else: 
        return (2 * THRESHOLD - words_left) * get_factor(direction)

    
def check_guess(puzzle: str, direction: str, word: str, row_or_column: int,
                words_left: int) -> int:
    """Return number of points earned based on the direction, word,
    row_or_column and words_left.
    
    Precondition: Puzzle must have the same number of charecters in each row.
                  Direction must be one of thesse posibilities
                  UP, DOWN, FORWARD, BACKWARD.
                  0 <= row_or_column <= Total number of rows in the puzzle
                  0  < words_left <= Total number of words (THRESHOLD)
    
    >>>check_guess('abcd\nefgh\nijkl\n', FORWARD, 'abcd', 0, 5)
    5
    >>>check_guess('abcd\nefgh\nijkl\n', BACKWARD, 'hgfe', 1, 2)
     24
    """
    
   # This code below describes how points are earned based on the direction 
   # of the guess. For example a DOWN guess in found directly in a specfic 
   # column, while an UP guess is found in the reverse of a column.
    if word in get_column(puzzle, row_or_column) and direction == DOWN:
        return get_points(direction, words_left)
    elif word in reverse(get_column(puzzle, row_or_column)) and direction\
             == UP:
        return get_points(direction, words_left)
    elif word in get_row(puzzle, row_or_column) and direction == FORWARD:
        return get_points(direction, words_left)
    elif word in reverse(get_row(puzzle, row_or_column)) and direction\
             == BACKWARD:
        return get_points(direction, words_left)
    else:
        return 0