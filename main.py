from utils import *  # Assurez-vous que utils.py contient les bonnes fonctions

def bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base):

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

def transform():
    init_number = ask_for_init_number()
    init_base = ask_for_init_base()
    target_base = ask_for_target_base()
    
    final_number = bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base)
    
    print(f"Le nombre converti est : {final_number}")

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
    decimal = 0
    puissance = 0
    for i in range(len(init_number) - 1, -1, -1):
        chiffre = init_number[i]
        if '0' <= chiffre <= '9':
            valeur = ord(chiffre) - ord('0')
        elif 'A' <= chiffre <= 'F':
            valeur = ord(chiffre) - ord('A') + 10
        elif 'a' <= chiffre <= 'f':
            valeur = ord(chiffre) - ord('a') + 10
        else:
            print("Erreur")

        decimal += valeur * (16 ** puissance)
        puissance += 1
    return decimal

def dec_to_bin(init_number):
    init_number = int(init_number)
    if init_number == 0:
        return "0"
    restes = ""
    while init_number > 0:
        restes = str(init_number % 2) + restes
        init_number //= 2
    return restes



def dec_to_hex(init_number):
    init_number = int(init_number)
    if init_number == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    restes = ""
    quotient = init_number
    while quotient > 0:
        reste = quotient % 16
        restes = hex_digits[reste] + restes
        quotient //= 16
    return restes        

transform()