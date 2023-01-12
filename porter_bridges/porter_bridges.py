import re

def get_hcp_from_text(text = ""):
    """
    
    Input  : "AKQJ864" with no sort
    Output : 10
    HCP for A = 4
            K = 3
            Q = 2
            J = 1
    Else    = 0
    """

    hcp = 0

    for i in text:
        if i == "A":
            hcp = hcp + 4
        if i == "K":
            hcp = hcp + 3
        if i == "Q":
            hcp = hcp + 2
        if i == "J":
            hcp = hcp + 1
        else:
            pass

    return hcp

def dict_to_text(input_dict):
    # Input_dict is
    # {'North': {'S': 'QJT5432', 'H': 'T', 'D': '6', 'C': 'QJ82'}
    # , 'East': {'S': '', 'H': 'J97543', 'D': 'K7532', 'C': '94'}
    # , 'South': {'S': '87', 'H': 'A62', 'D': 'QJT4', 'C': 'AT75'}
    # , 'West': {'S': 'AK96', 'H': 'KQ8', 'D': 'A98', 'C': 'K63'}}

    # Output
    # N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K6
    text = ""
        
    for i in ["North" ,"East" ,"South" ,"West"]:

        text = text + i[0] + ":"

        for j in ["S" ,"H" ,"D" ,"C"]:
            text = text + input_dict[i][j]

            if j != "C":
                text = text + "."
            if j == "C" and i != "West":
                text = text + " "

    return text

def text_to_pbn_check(input_text):
    """
    
    Input  : "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 W:87.A62.QJT4.AT75 S:AK96.KQ8.A98.K63" with on sort
    Output : True    if     found all
             False   if Not found some
    """
    # Output : is 
    # No Error : ["No Error"]
    # Error    : ["Error"   ,"N not found","E not found","S not found","W not found"]   # for Many not found
    # Error    : ["Error"   ,"N not found"]                                             # for One not found

    output = []

    # Regex to get Text
    N_text = re.findall('N:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)
    E_text = re.findall('E:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)
    S_text = re.findall('S:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)
    W_text = re.findall('W:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*', input_text)

    """
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
    """

    """
    print(N_text)
    print(E_text)
    print(W_text)
    print(S_text)
    """
    
    if N_text != [] and E_text != [] and W_text != [] and S_text != []:
        # if found all
        output = True
    else:
        # else not found some
        output = False


    return output

#print(text_to_pbn_check("N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 W:AK96.KQ8.A98.K63 :87.A62.QJT4.AT75"))



def list_to_text(input_list_N ,input_list_E ,input_list_S ,input_list_W):
    # Input
    """
    ['Ks', 'Js', 'Ts', '9s', 'Ah', '8h', 'Td', '8d', '7d', '6d', '3d', 'Ac', 'Tc']
    ['As', 'Qs', 'Qh', '7h', '5h', 'Kd', 'Qd', '4d', 'Kc', 'Qc', '6c', '5c', '3c']
    ['7s', '2s', 'Kh', 'Jh', 'Th', '9h', '6h', '3h', 'Ad', 'Jd', '2d', '7c', '4c']
    ['8s', '6s', '5s', '4s', '3s', '4h', '2h', '9d', '5d', 'Jc', '9c', '8c', '2c']
    """
    # Output_text
    """
    N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63
    """
    input_list = [input_list_N ,input_list_E ,input_list_S ,input_list_W]
    output_text = ""
    dir = ["N","E","W","S"]
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

def text_to_list_hand(input_text):
    # Input_text  is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" with on don't need to sort
    # Output_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" sort by N E S W
    N_text = re.findall('N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    E_text = re.findall('E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    W_text = re.findall('W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    S_text = re.findall('S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)

    output_text = [ N_text[0] ,
                    E_text[0] ,
                    W_text[0] ,
                    S_text[0] ]

    return output_text

def text_to_list_desk(input_text):
    """
    Input  : "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"
    Output : ['Qs', 'Js', 'Ts', '5s', '4s', '3s', '2s', 'Th', '6d', 'Qc', 'Jc', '8c', '2c'
            , 'Jh', '9h', '7h', '5h', '4h', '3h', 'Kd', '7d', '5d', '3d', '2d', '9c', '4c'
            , 'As', 'Ks', '9s', '6s', 'Kh', 'Qh', '8h', 'Ad', '9d', '8d', 'Kc', '6c', '3c'
            , '8s', '7s', 'Ah', '6h', '2h', 'Qd', 'Jd', 'Td', '4d', 'Ac', 'Tc', '7c', '5c']
    """
    # Regex                     ['N:QJT5432.T.6.QJ82']
    N_text = re.findall('N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    E_text = re.findall('E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    W_text = re.findall('W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    S_text = re.findall('S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)

    # Cut head
    N_text = N_text[0][2:]      # ['N:QJT5432.T.6.QJ82'] -> "QJT5432.T.6.QJ82"
    E_text = E_text[0][2:]
    W_text = W_text[0][2:]
    S_text = S_text[0][2:]


    suit = ["s","h","d","c"]
    index = 0
    output = []

    for i in [N_text,E_text,W_text,S_text]:
        index = 0
        for j in i:
            if j == ".":
                index = index + 1
            else:
                output.append(j+suit[index])

    #print(output)
    return output

def text_to_pbn(input_text):
    # Input_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" with on don't need to sort
    # Output_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" sort by N E S W
    N_text = re.findall('N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    E_text = re.findall('E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    S_text = re.findall('S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    W_text = re.findall('W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)

    output_text = N_text[0] + " " \
                + E_text[0] + " " \
                + S_text[0] + " " \
                + W_text[0]

    return output_text




def dict_to_desk(input_dict):
    # Input_dict is
    # {'North': {'S': 'QJT5432', 'H': 'T', 'D': '6', 'C': 'QJ82'}
    # , 'East': {'S': '', 'H': 'J97543', 'D': 'K7532', 'C': '94'}
    # , 'South': {'S': '87', 'H': 'A62', 'D': 'QJT4', 'C': 'AT75'}
    # , 'West': {'S': 'AK96', 'H': 'KQ8', 'D': 'A98', 'C': 'K6'}}

    # Output list is []
    main_dict = input_dict
    output_list = []

    for i in ["North","East","South","West"]:
        for j in ["S","H","D","C"]:
            for k in main_dict[i][j]:
                output_list.append(k+j.lower())

    return output_list

def pbn_to_dict(text):
    # Input text [String]
    #txt = "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"

    # Output dict_desk [dict][NSEW][card(list)]
    #dict_desk

    txt = text

    #   North

    #North = re.findall("N:[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*\.[AKQJT98765432]*", txt)    # Old
    North = re.findall("N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}", txt)
    if North == []:
        North_S = ""
        North_H = ""
        North_D = ""
        North_C = ""
    else:
        North = str(North)
        North = North[2:-2]
        North = North[2:]
        North_split = North.split(".")

        North_S = North_split[0]
        North_H = North_split[1]
        North_D = North_split[2]
        North_C = North_split[3]

    #   East
    
    East = re.findall("E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}", txt)
    if East == []:
        East_S = ""
        East_H = ""
        East_D = ""
        East_C = ""
    else:
        East = str(East)
        East = East[2:-2]
        East = East[2:]

        East_split = East.split(".")

        East_S = East_split[0]
        East_H = East_split[1]
        East_D = East_split[2]
        East_C = East_split[3]

    #   South

    South = re.findall("S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}", txt)
    if South ==[]:
        South_S = ""
        South_H = ""
        South_D = ""
        South_C = ""
    else:
        South = str(South)
        South = South[2:-2]
        South = South[2:]

        South_split = South.split(".")

        South_S = South_split[0]
        South_H = South_split[1]
        South_D = South_split[2]
        South_C = South_split[3]

    #   West

    West = re.findall("W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}", txt)
    if West == []:
        West_S = ""
        West_H = ""
        West_D = ""
        West_C = ""
    else:
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
    #print(dict_desk)
    return dict_desk


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

def deck_list_checker(input_desk):
    # Intitial variable
    input_desk = input_desk
    full_desk = generate_desk_list()
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

def deck_list_result(input_desk):
    """
    Input  : list of desk
            ['Qs', 'Js', 'Ts', '5s', '4s', '3s', '2s', 'Th', '6d', 'Qc', 'Jc', '8c', '2c'
            , 'Jh', '9h', '7h', '5h', '4h', '3h', 'Kd', '7d', '5d', '3d', '2d', '9c', '4c'
            , '8s', '7s', 'Ah', '6h', '2h', 'Qd', 'Jd', 'Td', '4d', 'Ac', 'Tc', '7c', '5c'
            , 'As', 'Ks', '9s', '6s', 'Kh', 'Qh', '8h', 'Ad', '9d', '8d', 'Kc', '6c', '3c']

    Output : [lost_card     -> []   or ['3c'] if have lost card
             ,over_card]    -> []   or ['3c'] if have over card
            
    lost_card ,over_card = deck_list_result(list_desk)
    """
    # Intitial variable
    input_desk = input_desk
    full_desk = generate_desk_list()
    lost_card = []
    over_card = []
    
    # Checking by Looping full_desk
    for i in full_desk:
        if i in input_desk:
            input_desk.remove(i)
        else:
            lost_card.append(i)
    
    over_card = input_desk

    return [lost_card ,over_card]

"""
desk = ['As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s'
      , 'Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h'
      , 'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d'
      , 'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']

deck_list_checker(desk)


"""






#print(pbn_to_dict("N:AKQJT98765432... E:.QJT872.AJT7.AK7 W:.9643.Q984.QJ652 S:.AK5.K6532.T9843"))

        
