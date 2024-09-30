bin_number_valid_chars = ["0", "1"]

dec_number_valid_chars = \
    bin_number_valid_chars \
  + ["2", "3", "4", "5", "6", "7", "8", "9"]

hex_number_valid_chars = \
    dec_number_valid_chars \
  + ["A", "B", "C", "D", "E", "F"] \
  + ["a", "b", "c", "d", "e", "f"]


def check_char_number_validity (char):
    return char in hex_number_valid_chars
 
def is_a_valid_number (number):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i<= len(number) - 1 :
        is_a_valid_char = check_char_number_validity (number[i])
        i = i+1
    return is_a_valid_char


def ask_for_the_init_number ():
    init_number = input ("Veuillez entrer un nombre : ")
    while not (is_a_valid_number (init_number)) == True:
        init_number = input ("Veuillez entrer un nombre entier valide !")
    return init_number



def check_char_base_validity (char):
    return char in hex_base_valid_chars
 
def is_a_valid_base (base):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i<= len(base) - 1 :
        is_a_valid_char = check_char_base_validity (base[i])
        i = i+1
    return is_a_valid_char


def ask_for_the_init_base ():
    init_base = input ("Entrez la base de départ: 2, 10 ou 16: ")
    while not (is_a_valid_base (init_base)) == True:
        init_base = input ("Veuillez entrer une base valide !")
    return init_base


ask_for_the_target_base = input ("Entrez la base d'arrivée: ")