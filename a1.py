"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{user.name}} ({{user.id}})"
__email__ = ""
__date__ = ""


# Write your code here (i.e. functions)
def select_word_at_random(word_select)-> str:
    if word_select in ("FIXED", "ARBITRARY"):
        words = load_words(word_select)
        word = random_index(words)
        return word
    else:
        return None



def create_guess_line(guess_no, word_length)-> str:
    wall_length = ["| - "] * word_length
    for i in range(len(GUESS_INDEX_TUPLE)):
        if len(GUESS_INDEX_TUPLE[i]) == word_length:
            guess_index = GUESS_INDEX_TUPLE[i]
    start, end = guess_index[guess_no-1]
    for i in range(start, end):
        wall_length[i] = "| * "
    guess_line = "guess {} ".format(guess_no) + wall_length + "|"

def display_guess_matrix(guess_no, word_length, scores)-> None:
    pass


def compute_value_for_guess(word, start_index, end_index, guess)-> int:
    pass

def main():
    """
    Handles top-level interaction with user.
    """
    # Write the code for your main function here
    print(WELCOME)
    action = input(INPUT_ACTION)
    if action == 's':
        word_select = input('Do you want a "FIXED" or "ARBITRARY" length word?: ')
        select_word_at_random(word_select)
        # while 循环
        while True:

    elif action == 'h':
        print(HELP)
    elif action == 'q':
        return
    elif action not in ('s', 'h', 'q'):
        print(INVALID)


if __name__ == "__main__":
    main()
