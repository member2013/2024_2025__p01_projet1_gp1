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

def bin_to_bin (init_number):
     return init_number

def dec_to_dec (init_number):
     return init_number

def hex_to_hex (init_number):
     return init_number

def hex_to_bin (init_number):
      init_number = hex_to_dec (init_number)
      init_number = dec_to_bin (init_number)
      return init_number

def bin_to_hex (init_number) :
       init_number = bin_to_dec (init_number)
       init_number = dec_to_hex (init_number)
       return init_number

def bin_to_dec (init_number) :
       pass























def dec_to_bin (init_number) :
    restes = ""
    quotient = init_number // 2
    reste = str (init_number % 2)
    restes = reste + restes
    while quotient != 0 :
        reste = str (quotient % 2)
        quotient = quotient // 2
        restes = reste + restes
    return restes

def hex_to_dec (init_number) :
    decimal = 0
    puissance = 0
    # On parcourt le nombre hexadécimal de droite à gauche
    for chiffre in reversed(init_number):
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
decimal_output = hex_to_dec(hexadecimal_input)
print(f"Le nombre en décimal est : {decimal_output}")

def dec_to_hex (init_number) :
    if init_number == 0 :
        return "0"
    hex_digits = "0123456789ABCDEF"
    restes = ""
    quotient = init_number
    while quotient > 0 :
        reste = quotient % 16
        restes = hex_digits [reste] + restes
        quotient = quotient // 16
    return restes

def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    if init_base == 2 and target_base == 2:
            return bin_to_bin (init_number)

    if init_base == 2 and target_base == 10:
            return bin_to_dec (init_number)

    if init_base == 2 and target_base == 16:
            return bin_to_hex (init_number)

    if init_base == 10 and target_base == 2:
            return dec_to_bin (init_number)
    
    if init_base == 10 and target_base == 10:
            return dec_to_dec (init_number)            
    
    if init_base == 10 and target_base == 16:
            return dec_to_hex (init_number)

    if init_base == 16 and target_base == 2:
            return hex_to_bin (init_number)

    if init_base == 16 and target_base == 10:
            return hex_to_dec (init_number)  

    if init_base == 16 and target_base == 16:
            return hex_to_hex (init_number)           
    
    

        






# assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

# ask_for_the_init_number 144