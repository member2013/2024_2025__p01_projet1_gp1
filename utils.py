from data import *
from main import *

def check_char_number_validity (char):
    return char in hex_number_valid_chars

def is_a_valid_number (number):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def ask_for_the_init_number ():
    init_number = input (ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_the_init_number_text)
    return init_number

def is_a_valid_base (base):
    return base in valid_base_strings

def ask_for_the_init_base ():
    init_base = input (ask_for_the_init_base_text)
    while not (is_a_valid_base (init_base)) == True:
        init_base = input (ask_again_for_the_init_base_text)
    return init_base

def ask_for_the_target_base ():
    target_base = input (ask_for_the_target_base_text)
    while not (is_a_valid_base (target_base)) == True:
        target_base = input (ask_again_for_the_target_base_text)
    return target_base