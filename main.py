from utils import *  # Assurez-vous que utils.py contient les bonnes fonctions

# Fonction principale pour la conversion entre les bases
def bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base):
    '''
    Cette fonction prend en compte le nombre d'entrée, 
    la base de départ et la base souhaitée. Elle va lancer la 
    fonction ci-dessous correspondante.
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

    return None  # Cas d'erreur si les bases ne correspondent pas

# Fonctions spécifiques de conversion entre bases identiques
def bin_to_bin(init_number):
    return init_number

def dec_to_dec(init_number):
    return init_number

def hex_to_hex(init_number):
    return init_number

# Fonctions de conversion entre différentes bases
def hex_to_bin(init_number):
    init_number = hex_to_dec(init_number)
    return dec_to_bin(init_number)

def bin_to_hex(init_number):
    init_number = bin_to_dec(init_number)
    return dec_to_hex(init_number)

def bin_to_dec(init_number):
    result = 0
    exposant = len(init_number) - 1    # Calcule l'exposant initial, correspondant à la position du bit le plus à gauche (plus significatif).
    for char in init_number:           
        if char == '1':                # Vérifie si le bit actuel est '1'.
            result += 2 ** exposant    # Si oui, ajoute la valeur de 2 élevé à `exposant` à `result`
        exposant -= 1                  # Réduit l'exposant de 1 pour passer au bit suivant, vers la droite.
    return result                      # Renvoie la valeur finale de "init_number" 

def hex_to_dec(init_number):
    decimal_value = 0
    hex_liste = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    for caracter in init_number:
        if caracter not in hex_liste:
            print("Erreur : Le nombre entré n'est pas valide en base 16.")
            return None
        decimal_value = decimal_value * 16 + hex_liste[caracter]

    return decimal_value

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

# Vérifie la compatibilité du nombre avec la base initiale
def check_compatibility_number_base(init_number, init_base):
    while True:
        if init_base == "2":
            if all(char in bin_number_valid_chars for char in init_number):
                return init_number
            else:
                print(error_in_init_base)
                init_number = ask_for_init_number()
        elif init_base == "10":
            if all(char in dec_number_valid_chars for char in init_number):
                return init_number
            else:
                print(error_in_init_base)
                init_number = ask_for_init_number()
        elif init_base == "16":
            if all(char in hex_number_valid_chars for char in init_number):
                return init_number
            else:
                print(error_in_init_base)
                init_number = ask_for_init_number()

# Fonction principale qui demande les valeurs à l'utilisateur et effectue la conversion
def transform():
    '''
    Cette fonction demande les valeurs de base, de nombre et de base cible à l'utilisateur
    puis effectue la conversion et affiche le résultat.
    '''
    init_number = ask_for_init_number()
    init_base = ask_for_init_base()
    init_number = check_compatibility_number_base(init_number, init_base)
    target_base = ask_for_target_base()
    
    final_number = bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base)
    print(f"Le nombre converti est : {final_number}")

# Lancer la fonction principale
if __name__ == "__main__":
    transform()
