from data import *

def check_char_number_validity(char):
    return char in hex_number_valid_chars

def is_a_valid_number(number):
    for char in number:
        if not check_char_number_validity(char):
            return False
    return True

def ask_for_init_number():
    init_number = input(ask_for_the_init_number_text)
    while not is_a_valid_number(init_number):
        init_number = input(ask_again_for_the_init_number_text)
    return init_number

def is_a_valid_base(base):
    return base in valid_base_strings

def ask_for_init_base():
    init_base = input(ask_for_the_init_base_text)
    while not is_a_valid_base(init_base):
        init_base = input(ask_again_for_the_init_base_text)
    return init_base

def ask_for_target_base():
    target_base = input(ask_for_the_target_base_text)
    while not is_a_valid_base(target_base):
        target_base = input(ask_again_for_the_target_base_text)
    return target_base 