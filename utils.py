def check_char_number_validity (char):
    return char in hex_valid_chars
 
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




ask_for_the_init_base = input ("Entrez la base de départ: 2, 10 ou 16: ")
ask_for_the_target_base = input ("Entrez la base d'arrivée: ")