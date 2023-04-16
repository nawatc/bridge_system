"""
Ref. 
Combinatorial number system  for generate 
https://math.stackexchange.com/questions/1227409/indexing-all-combinations-without-making-list
Full_cycle PRNG
https://en.wikipedia.org/wiki/Full_cycle
"""

from math   import comb
from random import randint

# Load Library handler
# To load porter_bridges Library by different location.
try:
    # If can't load.
    # Used for run by gui_interface file.
    from porter_bridges.porter_bridges import list_to_text
except:
    # Then Load from this statement.
    # Used for run by this file.
    # Use to test and debug.
    from porter_bridges import list_to_text



def generate_desk_list():
    """
    Return list of full desk
    """

    """
    # get list by implemented.
    num = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    suit = ["s","h","d","c"]
    desk = []

    for i in suit:
        for j in num:
            desk.append(j+i)
    """
    
    # get list by declear variable
    desk = ['As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s'
          , 'Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h'
          , 'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d'
          , 'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']
    
    return desk

def cgen(i ,n ,k):
    # Combination Generator
    """
    Returns the i-th combination of k numbers chosen from 1,2,...,n
            Order i from nCk

    Input  : i ,n ,k (i index_number   n total size   k total numbers chosen)
    Output : list of k chosen number
        as   [2, 4, 5, 13, 16, 17, 18, 19, 20, 32, 46, 50, 52]

    List of initials name
    c     list of collection index
    r     range
    j     index
    cs    current state
    i index     n total size    k numbers chosen
    """

    c = []
    r = i + 0
    j = 0

    for s in range(1,k+1):
        cs = j+1
        while r-comb(n-cs,k-s)>0:
            r -= comb(n-cs,k-s)
            cs += 1
        c.append(cs)
        j = cs
    
    return c    

def key_to_comb(key_number :int):
    """
    Returns Desk_code from key_number

    Input  : int
    Output : "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"
    """

    h1,h2,h3 = 0,0,0
    h1_list ,h2_list ,h3_list = [],[],[]
    h1_card ,h2_card ,h3_card ,h4_card = [],[],[],[]

    desk = generate_desk_list()
    num = key_number

    h1 = num % 635013559600        # Combination for h1 
    num = int(num / 635013559600)  # comb(52,13)

    h2 = num % 8122425444          # Combination for h2
    num = int(num / 8122425444)    # comb(39,13)

    h3 = num % 10400600            # Combination for h3
    num = int(num / 10400600)      # comb(26,13)

    #h4 = num


    num = 0

    h1_list = cgen(h1,52,13)
    h2_list = cgen(h2,39,13)
    h3_list = cgen(h3,26,13)
    #h4_list = cgen(h4,13,13)

    # Get Card h1
    for i in range(0,len(h1_list)):
        h1_card.append(desk[h1_list[i] - 1])

    # Remove Card h1
    for i in range(0,len(h1_list)):
        desk.remove(h1_card[i])
        
    # Get Card h1
    for i in range(0,len(h2_list)):
        h2_card.append(desk[h2_list[i] - 1])
    
    # Remove Card h2
    for i in range(0,len(h2_list)):
        desk.remove(h2_card[i])

    # Get Card h1
    for i in range(0,len(h3_list)):
        h3_card.append(desk[h3_list[i] - 1])
    
    # Remove Card h3
    for i in range(0,len(h3_list)):
        desk.remove(h3_card[i])

    h4_card = desk
    
    
    #print(h1_card)
    #print(h2_card)
    #print(h3_card)
    #print(h4_card)

    return list_to_text(h1_card ,h2_card ,h3_card ,h4_card)[:-1]    # cut last " " character
    


#print(cgen(1,10,2))
#print(cgen(17310309456440,100,10))
#print(cgen(68814103099439929837637702193841,1000,15))
#print(comb(52,13)*comb(39,13)*comb(26,13))

#print(cgen(635013559600,52,13))
#print(cgen(192307254993,52,13))

#key_to_comb(7096896423093986807593535793)



def cycle_one_step(seed: int, sample_size: int, increment: int):
    """ Return number from full cycle PRNG number """
    prng_number = (seed + increment) % sample_size

    return prng_number

def random_card():
    """ Return desk that generate from random number """
    number = randint(1, 53644737765488792839237440000)      # Random number between 1, 53644737765488792839237440000

    desk = key_to_comb(number)                              # generate desk from number
    
    return desk     #print(key_to_comb(number))     # N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63

def random_card_with_prng(seed_input: int):
    """ Return desk that generate from random number by full cycle PRNG method"""
    seed        = seed_input
    sample_size = 53644737765488792839237440000
    increment   = 31114111519121615131518191719     # 58.000304997 % of sample_size
                                                    # and be prime number that's be coprime of sample_size

    number = cycle_one_step(seed ,sample_size ,increment)     # Random number from seed ,sampl_size and increment

    desk = key_to_comb(number)                              # generate desk from number
    
    return desk     #print(key_to_comb(number))     # N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63


def get_num_from_txt(filename):
    # Get number from txt file
    # Number range is 1 to 53644737765488792839237440000
    f = open(filename, "r")
    #print(f.read())
    
    return int(f.read())

def set_num_from_txt(filename ,num):
    # Replace number to txt file
    # Number range is 1 to 53644737765488792839237440000
    f = open(filename, "w")
    f.write(str(num))

#################### TEST SECTION. ####################

#print(random_card())
#print(random_card_with_prng(1))


############### Generate Number for Desk ###############
#
# Seed is integer between 1 to 53644737765488792839237440000
"""
Seed = 26822368884744395102037213184
for i in range(1,10):
    print(cycle_one_step(seed = Seed, sample_size = 53644737765488792839237440000, increment = 231613336760896829))
    Seed = cycle_one_step(seed = Seed, sample_size = 53644737765488792839237440000, increment = 231613336760896829)
"""

##################### Generate Desk by number #####################
#
# seed is integer between 1 to 53644737765488792839237440000
#                              33644737765488792839237440000    3.3*10^28
#                              31114111519121615131518191719    Prime
#         https://primes.utm.edu/curios/index.php?start=25&stop=36
#
#33822368884744395102037213184
#                              26822368884744395102037213184    / 2
#                                    53644737765488792840969    / 1M
#                                    53644737765488792841241
#                                         231613336760896829    sqrt 2      Need more
"""
seed = 53644737765488792840969
print(key_to_comb(seed))
"""

############### Generate Muti Desk ###############
"""
Seed = 26822368884744395102037213184
Seed = 26222368884724395102237213184
for i in range(1,2):
    #print(cycle_one_step(seed = Seed, sample_size = 53644737765488792839237440000, increment = 231613336760896829))
    Seed = cycle_one_step(seed = Seed, sample_size = 53644737765488792839237440000, increment = 31114111519121615131518191719)
    #Seed = cycle_one_step(seed = Seed, sample_size = 53644737765488792839237440000, increment = 23)
    #print(key_to_comb(Seed))

"""




"""
a = 6

for i in range (1,150):
    a = cycle_one_step(seed = a, sample_size = 100, increment = 81)
    print(a)
"""






################    Old Parts    ################

# Generator that goes through a full cycle
def cycle(seed: int, sample_size: int, increment: int):
    nb = seed
    for i in range(sample_size):
        nb = (nb + increment) % sample_size
        yield nb

def cycle_one_step(seed: int, sample_size: int, increment: int):
    nb = seed
    nb = (nb + increment) % sample_size
    return nb

def FC_random_number():
    # Number range is 1 to 53644737765488792839237440000
    # Full cycle PRNG
    # https://en.wikipedia.org/wiki/Full_cycle
    # Example values
    seed = 0           #seed_input
    sample_size = 10 #10    #53644737765488792839237440000      # 53 644 , 737 765 , 488 792 , 839 237 , 440 000
    increment = 3 #13      #

    # Print all the numbers
    print(list(cycle(seed, sample_size, increment)))

    # Verify that all numbers were generated correctly
    assert set(cycle(seed, sample_size, increment)) == set(range(sample_size))
    
#FC_random_number()

# get 1 step

"""while(1):
    a = cycle_one_step(seed = get_num_from_txt() ,sample_size = 53644737765488792839237440000 ,increment = 11)
    #print(a)
    set_num_from_txt(a)"""
