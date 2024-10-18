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
       number = from_bin_to_dec (number)
       number = from_dec_to_hex (number)
       return number

def from_bin_to_dec (number) :
       pass

def from_dec_to_bin (number) :
       pass

def from_hex_to_dec (number) :
       pass

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