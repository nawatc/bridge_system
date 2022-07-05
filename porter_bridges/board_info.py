






def get_vul_from_board_number(board_num):
    # Oldname send_board_get_vul

    # Set Board number
    # If Board number more then 16, Vul will repeat value.
    board_num = board_num % 16
    if (board_num == 0):
        board_num = 16

    # Return Board's Vul by dict
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

def get_dealer_from_board_number(board_num):
    # Old name  send_board_get_dealer

    # Set Board number
    # If Board number more then 4, Dealer will repeat value.

    # /Input 
    # /Output
    
    board_num = board_num % 4

    # Return Board's Dealer by dict
    if (board_num == 0):
        board_num = 4

    dealer_dict = {

    1  : "N",
    2  : "E",
    3  : "S",
    4  : "W",

    }
    
    return dealer_dict[board_num]




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



























