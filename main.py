from utils import *

# def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
#     target_number = None
#     return target_number


def transform  ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
        bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base)

def from_bin_to_bin (number):
     return number

def from_dec_to_dec (number):
     return number

def from_hex_to_hex (number):
     return number

def from_hex_to_bin (number):
      number = from_hex_to_dec (number)
      number = from_dec_to_bin (number)
      return number

def from_bin_to_hex (number) :
        init_number = from_bin_to_dec (init_number)
        init_number = from_dec_to_hex (init_number)
        return init_number  # en attente des fonctions bin_to_dec de cassandre et dec_to_hex de Salomé !!

def from_bin_to_dec (number) :
       pass




















def from_dec_to_bin (number) :
       pass









def from_hex_to_dec (number) :
    decimal = 0
    puissance = 0
    # On parcourt le nombre hexadécimal de droite à gauche
    for chiffre in reversed(number):
        if '0' <= chiffre <= '9':
            valeur = ord(chiffre) - ord('0')  # Convertir caractère '0'-'9' à valeur 0-9
        elif 'A' <= chiffre <= 'F':
            valeur = ord(chiffre) - ord('A') + 10  # Convertir 'A'-'F' à valeur 10-15
        elif 'a' <= chiffre <= 'f':
            valeur = ord(chiffre) - ord('a') + 10  # Convertir 'a'-'f' à valeur 10-15
        else:
            raise ValueError("Caractère hexadécimal invalide")
        
        # Calculer la valeur décimale
        decimal += valeur * (16 ** puissance)
        puissance += 1
    
    return decimal

# on print
hexadecimal_input = input("Entrez un nombre hexadécimal : ")
decimal_output = from_hex_to_dec(hexadecimal_input)
print(f"Le nombre en décimal est : {decimal_output}")









def from_dec_to_hex (number) :
       pass


















def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    if init_base == 2 and target_base == 2:
            return from_bin_to_bin (init_number)

    if init_base == 2 and target_base == 10:
            return from_bin_to_dec (init_number)

    if init_base == 2 and target_base == 16:
            return from_bin_to_hex (init_number)

    if init_base == 10 and target_base == 2:
            return from_dec_to_bin (init_number)
    
    if init_base == 10 and target_base == 10:
            return from_dec_to_dec (init_number)            
    
    if init_base == 10 and target_base == 16:
            return from_dec_to_hex (init_number)

    if init_base == 16 and target_base == 2:
            return from_hex_to_bin (init_number)

    if init_base == 16 and target_base == 10:
            return from_hex_to_dec (init_number)  

    if init_base == 16 and target_base == 16:
            return from_hex_to_hex (init_number)           
    
    

        











# assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

# ask_for_the_init_number 144