#https://math.stackexchange.com/questions/1227409/indexing-all-combinations-without-making-list
from math import comb
from porter_bridges.porter_bridges import list_to_text
import random

def generate_desk():
    num = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    suit = ["s","h","d","c"]
    desk = []

    for i in suit:
        for j in num:
            desk.append(j+i)
    
    return desk

def C(n,k):
    return comb(n,k)
"""
def C(n,k): #computes nCk, the number of combinations n choose k
    result = 1
    for i in range(n):
        result*=(i+1)
    for i in range(k):
        result/=(i+1)
    for i in range(n-k):
        result/=(i+1)
    return result
"""

def cgen(i,n,k):
    """
    returns the i-th combination of k numbers chosen from 1,2,...,n
    """
    c = []
    r = i+0
    j = 0
    for s in range(1,k+1):
        cs = j+1
        while r-C(n-cs,k-s)>0:
            r -= C(n-cs,k-s)
            cs += 1
        c.append(cs)
        j = cs
    return c

def key_to_comb(key):
    h1,h2,h3 = 0,0,0
    h1_list ,h2_list ,h3_list = [],[],[]
    h1_card ,h2_card ,h3_card ,h4_card = [],[],[],[]

    desk = generate_desk()
    num = key

    h1 = num % 635013559600 # combi for h1 
    num = int(num / 635013559600)    # C(52,13)

    h2 = num %   8122425444
    num = int(num / 8122425444)    # C(39,13)

    h3 = num % 10400600
    num = int(num / 10400600)     #C(26,13)

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

    return list_to_text(h1_card ,h2_card ,h3_card ,h4_card)
    


#print(cgen(1,10,2))
#print(cgen(17310309456440,100,10))
#print(cgen(68814103099439929837637702193841,1000,15))
#print(C(52,13)*C(39,13)*C(26,13))

#print(cgen(635013559600,52,13))
#print(cgen(192307254993,52,13))

#key_to_comb(7096896423093986807593535793)



def cycle_one_step(seed: int, sample_size: int, increment: int):
    nb = seed
    nb = (nb + increment) % sample_size
    return nb

def random_card():
    number = random.randint(1, 53644737765488792839237440000)
    # N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63
    #print(key_to_comb(number))
    return key_to_comb(number)

def random_card_with_prng():
    pass








#################### TEST SECTION. ####################



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
#                              26822368884744395102037213184    / 2
#                                    53644737765488792840969    / 1M
#                                         231613336760896829    sqrt 2
"""
seed = 53644737765488792840969
print(key_to_comb(seed))
"""

############### Generate Muti Desk ###############

Seed = 26822368884744395102037213184
for i in range(1,20):
    #print(cycle_one_step(seed = Seed, sample_size = 53644737765488792839237440000, increment = 231613336760896829))
    Seed = cycle_one_step(seed = Seed, sample_size = 53644737765488792839237440000, increment = 231613336760896829)
    print(key_to_comb(Seed))



#random_card()