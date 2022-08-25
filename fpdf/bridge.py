def get_vul(board_num):
    board_num = board_num % 16

    if (board_num == 0):
        board_num = 16

    vul_dict = {

    1  : "None",
    2  : "N-S",
    3  : "E-W",
    4  : "All",
    5  : "N-S",
    6  : "E-W",
    7  : "All",
    8  : "None",
    9  : "E-W",
    10 : "All",
    11 : "None",
    12 : "N-S",
    13 : "All",
    14 : "None",
    15 : "N-S",
    16 : "E-W"

    }

    return vul_dict[board_num]

def get_dealer(board_num):
    board_num = board_num % 4

    if (board_num == 0):
        board_num = 4

    dealer_dict = {

    1  : "N",
    2  : "E",
    3  : "S",
    4  : "W",

    }
    
    return dealer_dict[board_num]

def split(word):
    return [char for char in word]

def hcp_point_count_by_str(list):
    #hcp_point_count_by_str( ["T7", "K542", "KQ42", "Q72"] )
    hcp = 0
    foo = ''.join(map(str, list))
    boo = split(foo)
    
    for i in boo:
        if i == "A":
            hcp = hcp + 4
        if i == "K":
            hcp = hcp + 3
        if i == "Q":
            hcp = hcp + 2
        if i == "J":
            hcp = hcp + 1
    
    return hcp

        





"""
Board	Dealer	Vul.		
1       N	    None	
2	    E	    N-S	
3	    S	    E-W	
4	    W	    All	
5	    N	    N-S	
6	    E	    E-W	
7	    S	    All	
8	    W	    None	
9	    N	    E-W	
10	    E	    All	
11	    S	    None	
12  	W	    N-S	
13  	N	    All
14  	E	    None
15	    S	    N-S
16	    W   	E-W
"""




"""        self.all_board_dir = ["N","E","S","W"]

        
        self.suit = ["s","h","d","c"]

        self.full_suit = "AKQJT98765432"
        self.full_desk = {  "s": self.full_suit ,
                            "h": self.full_suit ,
                            "d": self.full_suit ,
                            "c": self.full_suit
        }

        # Add Dealer,Vul
        self.dict['dealer'] = get_dealer(board_num)
        self.dict['vul'] = get_vul(board_num)
        """

        
def valid_desk(dic):
    # Vaild desk from self.full_desk and add_card
    """
    Document of variable

    name:           type:   example of data:

    init_full_desk  dict    {'s': 'AKQJT98765432', 'h': 'AKQJT98765432', 'd': 'AKQJT98765432', 'c': 'AKQJT98765432'}

    hand            str     N E S W

    hand_card       list    N : ['T7', 'K542', 'KQ42', 'Q72']

    suit_list_index int     0 1 2 3

    suit            str     s h d c

    card_suit       str     KQ42
    """
    
    # Using full desk card
    init_full_desk = self.full_desk
    lost_card = []
    over_card = []
    
    #print(init_full_desk)

    for hand in self.all_board_dir:
    # In all direction hand
        # hand_card is list of string card of suit
        hand_card = self.dict[hand + "_card"]
        
        # Print all card in hand
        # example   N ->  ['T7', 'K542', 'KQ42', 'Q72']
        #print(hand + " ->  " + str(hand_card))

        for suit in self.suit:
        # In each suit of hand
            # card_suit is string of 
            suit_list_index = self.suit.index(suit)
            card_suit = hand_card[ suit_list_index ]
            
            # Print index of card suit for hand_card
            #print(hand + " : " + suit + " : " + str(suit_list_index) + " : " + card_suit)
            #print(hand + " : " + suit + " : " + card_suit)
            
            for card in card_suit :
            # In each card in suit
                #print("hand" + " : " + "suit" + " : " + "suit_list_index" + " : " + "card")
                #print(hand + "\t" + suit + "\t" + str(suit_list_index) + "\t" + card)

                if card in init_full_desk[suit]:
                # if have card in full desk remove it
                    init_full_desk[suit] = init_full_desk[suit].replace(card, '')
                    
                    #print(hand + " : " + suit + " : " + card)
                    #print(init_full_desk)

                else:
                # if not have card in full desk mean it is over card
                # find card that over in every hand and display

                    over_card.append(suit + card)
                    #print(hand + ":" + suit + ":" + ":" + card)
                    
                    #finding_direction who have card
                    finding_dir = []

                    for hand_finding in self.all_board_dir:
                    # Find in every hand
                        # get hand_card ,every card on one hand
                        hand_card_hand_finding = self.dict[hand_finding + "_card"]
                        
                        # Find index of suit card
                        find_suit = over_card[-1][0]                    # over_card in last element, get first charecter  example. ['h5','s3'] -> get "s"
                        find_number = over_card[-1][1]
                        find_suit_index = self.suit.index(find_suit)    # get suit index from suit


                        # Find suit card on every hand
                        card_suit = hand_card_hand_finding[ find_suit_index ]
                        
                        if find_number in card_suit:
                        # If find number in this dir suit 
                        # Add direction
                            finding_dir.append(hand_finding)
                            #print(hand_finding)
                    
                    # Convert finding_dir to string
                    finding_dir_str_version = ''.join(finding_dir)

                    # Add direction to overcard
                    over_card[-1] = finding_dir_str_version + ":" +over_card[-1]

                    #print(over_card[-1])
                    #print(finding_dir_str_version)
                    

    # Check if init_full_desk is not empty -> Still have card
    for suit in self.suit:
        if init_full_desk[suit] == '' :
            init_full_desk_check = False
        else:
            init_full_desk_check = True
            break
    
    # for find lost_card
    if init_full_desk_check:
        #print("list is not empty")
        # If init_full_desk is not empty mean card is lost
        for suit in self.suit:
            for card in init_full_desk[suit]:
                # Add remain card to lost_card
                lost_card.append(suit + card)
                #print(suit + card)

    # Check nuumber of card 
    for hand in self.all_board_dir:
        card = self.dict[hand + "_card"]

        count = 0

        for i in range(0,4):
            count = count + len(card[i])
        
        if count == 13:
            pass
            number_card_check = True
        elif count < 13:
            print(hand + " has card less then 13")
            number_card_check = False
        elif count > 13:
            print(hand + " has card more then 13")
            number_card_check = False


    print(init_full_desk)
    print("Over card is ", end='')
    print(over_card)
    print("Lost card is ", end='')
    print(lost_card)
    print(number_card_check)
    
    # Check if desk is vaild
    if over_card == [] and lost_card == []:
        # If vaild
        print("This desk is vaild")
        return 1
    else:
        # If invaild
        print("This desk is invaild")
        return 0

    """# Check if init_full_desk is empty
    if not init_full_desk:
        #print("list is empty")
        # Return True if list is full desk
        print("a")
        return 1
    else:
        #print("list is not empty")
        # Return False if list is not desk
        return 0"""



#for i in range(1 , 23):
#    print(str(i) + " " + send_board_get_vul(i))