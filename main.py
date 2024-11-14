from utils import *  # Assurez-vous que utils.py contient les bonnes fonctions

def bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base):
    
    '''
      Cette fonction prend en compte le nombre d'entrée, 
      la base de départ et la base souhaitée. Elle va donc lancée la 
      fontion ci-dessous correspondante.
    '''

    init_base = int(init_base)
    target_base = int(target_base)

    if init_base == 2 and target_base == 2:
        return bin_to_bin(init_number)

    if init_base == 2 and target_base == 10:
        return bin_to_dec(init_number)

    if init_base == 2 and target_base == 16:
        return bin_to_hex(init_number)

    if init_base == 10 and target_base == 2:
        return dec_to_bin(init_number)

    if init_base == 10 and target_base == 10:
        return dec_to_dec(init_number)

    if init_base == 10 and target_base == 16:
        return dec_to_hex(init_number)

    if init_base == 16 and target_base == 2:
        return hex_to_bin(init_number)

    if init_base == 16 and target_base == 10:
        return hex_to_dec(init_number)

    if init_base == 16 and target_base == 16:
        return hex_to_hex(init_number)
    
    return None

def bin_to_bin(init_number):
    return init_number

def dec_to_dec(init_number):
    return init_number

def hex_to_hex(init_number):
    return init_number

def hex_to_bin(init_number):
    init_number = hex_to_dec(init_number)
    return dec_to_bin(init_number)

def bin_to_hex(init_number):
    init_number = bin_to_dec(init_number)
    return dec_to_hex(init_number)

def bin_to_dec(init_number):
    result = 0
    exposant = len(init_number) - 1
    for char in init_number:
        if char == '1':
            result += 2 ** exposant
        exposant -= 1
    return result

def hex_to_dec(init_number):
    decimal_value = 0                                                        # Initialiser la valeur décimale à 0
    hex_liste = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }                                                                       # Liste qui associe chaque caractère hexadécimal
#                                                                             à sa valeur en base 10

    for caracter in init_number:                                            # Parcourir chaque caractère du nombre initial en base 16
        if caracter not in hex_liste:
            print("Erreur : Le nombre entré n'est pas valide en base 16.")  # Vérifier si le caractère est valide en vérifiant 
#                                                                             qu'il est bien présent dans la liste hex_liste

        decimal_value = decimal_value * 16 + hex_liste[caracter]            # Mettre à jour la valeur décimale initialisée à 0 
#                                                                             en multipliant par 16 et en ajoutant la valeur en base 10 
#                                                                             du nombre initial trouvé la liste hex_liste

    return decimal_value                                                    # Retourner la valeur décimale actualisée


def dec_to_bin(init_number):
    init_number = int(init_number)              # pour convertir init_number en entier.
    if init_number == 0:                        # car 0 en base 10 est aussi 0 en base 2.
        return "0"
    restes = ""                                 # chaîne vide qui accumule les chiffres binaires formant le résultat final.
    while init_number > 0:                      # à chaque itération :
        restes = str(init_number % 2) + restes  # on calcule le reste de la division de init_number par 2, qui donne le chiffre binaire le plus à droite.
#                                                 Le reste est converti en chaîne (str) et ajouté au début de la chaîne restes (pour avoir les chiffres dans le bon ordre).
        init_number //= 2                       # init_number est ensuite mis à jour en le divisant par 2.
    return restes                               # la fonction retourne la chaîne restes, qui contient le nombre en base 2.

def dec_to_hex(init_number):
    init_number = int(init_number)          # pour convertir init_number en entier.
    if init_number == 0:                    # car 0 en base 10 est aussi 0 en base 16.
        return "0"
    hex_digits = "0123456789ABCDEF"         # hex_digits contient des caractères hexadécimaux (valeurs de 0 à 15),
#                                           # => permet la conversion des restes en leurs représentations hexadécimales.
    restes = ""                             # chaîne vide qui accumule les chiffres hexadécimaux formant le résultat final.
    quotient = init_number                  # quotient est initialisé avec la valeur de init_number car il sera modifié dans la boucle.
    while quotient > 0:                     # à chaque itération :
        reste = quotient % 16               # on calcule le reste de la division de quotient par 16
        restes = hex_digits[reste] + restes # reste: utilisé comme indice pour obtenir le caractère héxadécimal correspondant dans hex_digits
#                                             et ce caractère est ajouté au début de la chaine restes (pour avoir les chiffres dans le bon ordre)
        quotient //= 16                     # pour mettre le quotient à jour en le divisant par 16 pour préparer l'itération suivante.
    return restes                           # la fonction retourne la chaîne restes, qui contient le nombre en base 16.

# def check_compatibility_number_base (init_number, init_base):
#     if init_base == "2":
#         for n in init_number:
#             if n not in bin_number_valid_chars:
#                 print (error_in_init_base)
#     elif init_base == "10":
#         for n in init_number:
#             if n not in dec_number_valid_chars:
#                 print (error_in_init_base)
#     elif init_base == "16":
#         for n in init_number:
#             if n not in hex_number_valid_chars:
#                 print (error_in_init_base)

def check_compatibility_number_base(init_number, init_base):
    while True:
        if init_base == "2":
            if all(char in bin_number_valid_chars for char in init_number):
                break
            else:
                print(error_in_init_base)
                init_number = ask_for_init_number()
        elif init_base == "10":
            if all(char in dec_number_valid_chars for char in init_number):
                break
            else:
                print(error_in_init_base)
                init_number = ask_for_init_number()
        elif init_base == "16":
            if all(char in hex_number_valid_chars for char in init_number):
                break
            else:
                print(error_in_init_base)
                init_number = ask_for_init_number()

def transform():
    
    '''
    Cette fonction demande les valeurs de base, de nombre et de base cible à l'utilisateur
    puis effectue la conversion et affiche le résultat.
    '''
    init_number = ask_for_init_number()
    init_base = ask_for_init_base()
    check_compatibility_number_base (init_number, init_base)
    init_number = int(init_number)
    target_base = ask_for_target_base()
   
    
    final_number = bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base)
    print (f"Le nombre converti est : {final_number}")

if __name__ == "__main__":
    transform() 