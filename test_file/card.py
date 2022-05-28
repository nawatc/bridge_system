import random

def generate_deck():

    desk = []

    num  = ["A" ,"K" ,"Q" ,"J","T" ,"9" ,"8" ,"7" ,"6" ,"5" ,"4" ,"3" ,"2"]
    suit = ["s" ,"h" ,"d" ,"c"]
    
    for suit_i in suit:
        for num_j in num:
            desk.append( num_j + suit_i )
    
    random.shuffle(desk)
    
    return desk

print(generate_deck())