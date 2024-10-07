from utils import *


def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number


def transform  ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
        bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base)

def bin_to_bin (number):
     return number

def dec_to_dec (number):
     return number

def hex_to_hex (number):
     return number

def hex_to_bin (number):
      number = hex_to_dec (number)
      number = dec_to_bin (number)
      return number

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