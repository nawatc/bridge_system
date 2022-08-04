import re


def text_to_pbn_check(input_text):
    #input_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" with on sort
    #
    #output is 
    # No Error : ["No Error"]
    # Error    : ["Error"   ,"N not found","E not found","S not found","W not found"]   # Many not found
    # Error    : ["Error"   ,"N not found"]    # One not found

    output = []

    N_text = re.findall('N:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)
    E_text = re.findall('E:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)
    S_text = re.findall('S:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)
    W_text = re.findall('W:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)

    if N_text == "": # Not found North
        output.append("N : Not found")
    if E_text == "": # Not found East
        output.append("E : Not found")
    if S_text == "": # Not found South
        output.append("S : Not found")
    if W_text == "": # Not found West
        output.append("W : Not found")

    if output == []:    # No Error
        output.insert( 0 ,"No Error")
    else:               # Error
        output.insert( 0 ,"Error")


    return output

def list_to_text(input_list_N ,input_list_E ,input_list_S ,input_list_W):
    # input
    """
    ['Ks', 'Js', 'Ts', '9s', 'Ah', '8h', 'Td', '8d', '7d', '6d', '3d', 'Ac', 'Tc']
    ['As', 'Qs', 'Qh', '7h', '5h', 'Kd', 'Qd', '4d', 'Kc', 'Qc', '6c', '5c', '3c']
    ['7s', '2s', 'Kh', 'Jh', 'Th', '9h', '6h', '3h', 'Ad', 'Jd', '2d', '7c', '4c']
    ['8s', '6s', '5s', '4s', '3s', '4h', '2h', '9d', '5d', 'Jc', '9c', '8c', '2c']
    """
    # output_text
    """
    N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63
    """
    input_list = [input_list_N ,input_list_E ,input_list_S ,input_list_W]
    output_text = ""
    dir = ["N","E","S","W"]
    suit = ["s","h","d","c"]
    

    for i in range(0,4):
        # Dir
        output_text = output_text + dir[i] + ":"
        hand = input_list[i]

        count_suit = 0

        for j in hand:
            
            while(j[-1] != suit[count_suit]):
                output_text = output_text + "."
                count_suit = count_suit + 1

            if j[-1] == suit[count_suit]:
                output_text = output_text + j[0]

        while(count_suit != 3):
                output_text = output_text + "."
                count_suit = count_suit + 1

        output_text = output_text + " "

    #print(output_text)
    return output_text
        
#list_to_text(['As', 'Ks', 'Qs', 'Js', 'Ts', '9s', 'Ah', '8h', 'Td', '8d', '7d', '6d', '3d'],['Qh', '7h', '5h', 'Kd', 'Qd', '4d', 'Kc', 'Ac', 'Tc', 'Qc', '6c', '5c', '3c'],['7s', '2s', 'Kh', 'Jh', 'Th', '9h', '6h', '3h', 'Ad', 'Jd', '2d', '7c', '4c'],['8s', '6s', '5s', '4s', '3s', '4h', '2h', '9d', '5d', 'Jc', '9c', '8c', '2c'])

def text_to_list(input_text):
    #input_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" with on don't need to sort
    #output_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" sort by N E S W
    N_text = re.findall('N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    E_text = re.findall('E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    S_text = re.findall('S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    W_text = re.findall('W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)

    output_text = [ N_text[0] ,
                    E_text[0] ,
                    S_text[0] ,
                    W_text[0] ]

    return output_text

def text_to_pbn(input_text):
    #input_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" with on don't need to sort
    #output_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" sort by N E S W
    N_text = re.findall('N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    E_text = re.findall('E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    S_text = re.findall('S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    W_text = re.findall('W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)

    output_text = N_text[0] + " " \
                + E_text[0] + " " \
                + S_text[0] + " " \
                + W_text[0]

    return output_text


def pbn_to_dict(text):
    # Input text [String]
    #txt = "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"

    # Output dict_desk [dict][NSEW][card(list)]
    #dict_desk

    txt = text

    #   North

    #North = re.findall("N:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*", txt)    # Old
    North = re.findall("N:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*", txt)
    North = str(North)
    North = North[2:-2]
    North = North[2:]
    North_split = North.split(".")

    North_S = North_split[0]
    North_H = North_split[1]
    North_D = North_split[2]
    North_C = North_split[3]

    #   East
    
    #
    East = re.findall("E:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*", txt)
    East = str(East)
    East = East[2:-2]
    East = East[2:]

    East_split = East.split(".")

    East_S = East_split[0]
    East_H = East_split[1]
    East_D = East_split[2]
    East_C = East_split[3]

    #   South

    South = re.findall("S:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*", txt)
    South = str(South)
    South = South[2:-2]
    South = South[2:]

    South_split = South.split(".")

    South_S = South_split[0]
    South_H = South_split[1]
    South_D = South_split[2]
    South_C = South_split[3]

    #   West

    West = re.findall("W:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*", txt)
    West = str(West)
    West = West[2:-2]
    West = West[2:]

    West_split = West.split(".")

    West_S = West_split[0]
    West_H = West_split[1]
    West_D = West_split[2]
    West_C = West_split[3]

    dict_desk = {
        "North" : {
            "S" : North_S ,
            "H" : North_H ,
            "D" : North_D ,
            "C" : North_C
        } ,
        "East" : {
            "S" : East_S ,
            "H" : East_H ,
            "D" : East_D ,
            "C" : East_C
        } ,
        "South" : {
            "S" : South_S ,
            "H" : South_H ,
            "D" : South_D ,
            "C" : South_C
        } ,
        "West" : {
            "S" : West_S ,
            "H" : West_H ,
            "D" : West_D ,
            "C" : West_C
        }
        }

    return dict_desk

def get_num_from_txt():
    # Get number from txt file
    # Number range is 1 to 53644737765488792839237440000
    f = open("rng_number.txt", "r")
    #print(f.read())
    
    return int(f.read())

def set_num_from_txt(num):
    # Replace number to txt file
    # Number range is 1 to 53644737765488792839237440000
    f = open("rng_number.txt", "w")
    f.write(str(num))

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
    seed = 17           #seed_input
    sample_size = 7 #10    #53644737765488792839237440000      # 53 644 , 737 765 , 488 792 , 839 237 , 440 000
    increment = 3 #13      #

    # Print all the numbers
    print(list(cycle(seed, sample_size, increment)))

    # Verify that all numbers were generated correctly
    assert set(cycle(seed, sample_size, increment)) == set(range(sample_size))

def generate_desk():
    num = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    suit = ["s","h","d","c"]
    desk = []

    for i in suit:
        for j in num:
            desk.append(j+i)
    
    return desk

def deck_list_checker(input_desk):
    # Intitial variable
    input_desk = input_desk
    full_desk = generate_desk()
    lost_card = []
    over_card = []
    
    # Checking by Looping full_desk
    for i in full_desk:
        if i in input_desk:
            input_desk.remove(i)
        else:
            lost_card.append(i)
    
    over_card = input_desk

    #print(over_card)
    #print(lost_card)

    if over_card == [] and lost_card == []:
        return True
    else:
        return False


desk = ['As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', 'Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', 'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', 'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']

deck_list_checker(desk)









#FC_random_number()

# get 1 step

"""while(1):
    a = cycle_one_step(seed = get_num_from_txt() ,sample_size = 53644737765488792839237440000 ,increment = 11)
    #print(a)
    set_num_from_txt(a)"""







        
