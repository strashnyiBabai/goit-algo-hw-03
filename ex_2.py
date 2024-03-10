import random

"""Returns lottery ticket with unique number from range of given numbers: from 'min' to 'max' (both included).
    Amount of random picked numbers is equal to 'quantity'"""
def get_numbers_ticket(min: int, max: int, quantity: int):
    
    "List of given numbers"
    loterry_range = list(range(min, max+1))
    lotrry_numbers = ()

    """First of all ckeck if 'min' and 'max' are in allowed range.
        Then try to pick random unique numbers for lottery 
        excpet if there is error, give a message to user"""
    if min >= 1 and max <= 1000:    
        try:
            lotrry_numbers = random.sample(loterry_range, quantity)
            return sorted(lotrry_numbers)
        except (TypeError, ValueError):
            return "Wrong input info. 'min' should be less than 'max'. 'quantity' cannot be bigger than ('max' - 'min' + 1) "
        
    else:
        return "'min' must be >= 1 and 'max' must be <= 1000"

print(get_numbers_ticket(1, 10,3))