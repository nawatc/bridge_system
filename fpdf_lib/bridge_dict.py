from bridge import get_dealer ,get_vul ,hcp_point_count_by_str

class bridge_dict():
    def __init__(self):
        self.bridge_dict = {}   # Emtry Dictionary
        self.last_board = {}    # Emtry Dictionary
        self.last_board_num = len(self.bridge_dict) # init last_board_num = 0
        
        
        self.all_board_dir = ["N","E","S","W"]


    def add_new_board(self):

        # Add new dict key
        self.last_board_num = len(self.bridge_dict) + 1
        self.bridge_dict = {self.last_board_num : {} }    # Set to emtry dict

        # Reset Last Board
        self.last_board = {}
    
    def end_new_board(self):

        # Set Value to last_board
        self.bridge_dict = {self.last_board_num : self.last_board }








    def get_last_board_num(self):
        return self.last_board_num

    def get_full_board(self):
        return self.bridge_dict








    def add_card(self,direction ,s_suit ,h_suit ,d_suit ,c_suit):
        # Add Card to dict by key [direction]_HCP     example. -> self.last_board["N_hand"] = ["s_suit" ,"h_suit" ,"d_suit" ,"c_suit"]
        if direction in self.all_board_dir:
            self.last_board[direction+"_card"] = [s_suit ,h_suit ,d_suit ,c_suit]
        else:
            print("Input Dirction invaild : " + direction)

    



    def set_info(self):
        self.set_hcp_by_card()
        self.set_dealer_by_board()
        self.set_vul_by_board()

    def set_hcp_by_card(self):
        # Add HCP to dict, calcuate by added card

        for i in self.all_board_dir:
            # Add by each Hand

            # Display Add data
            #print(hcp_point_count_by_str_list(self.last_board[i+"_card"]))

            # Add in dict by key [direction]_HCP     example. -> dict["N_HCP"] = 12
            self.last_board[i + "_HCP"] = hcp_point_count_by_str(self.last_board[i+"_card"])
    
    def set_dealer_by_board(self):
        board_num = self.last_board_num

        self.last_board["dealer"] = get_dealer( board_num )
        

    def set_vul_by_board(self):
        board_num = self.last_board_num

        self.last_board["vul"] = get_vul( board_num )
        












    def add_key(self ,key ,value):
        self.dict[key] = value



tournament_board = bridge_dict()
tournament_board.add_new_board()
tournament_board.add_card(direction = "N"
    ,s_suit = "T"
    ,h_suit = "K542"
    ,d_suit = "KQ42"
    ,c_suit = "Q72"
    )
tournament_board.add_card(direction = "E"
    ,s_suit = "Q64"
    ,h_suit = "QJT7"
    ,d_suit = "AJ9"
    ,c_suit = "T43"
    )
tournament_board.add_card(direction = "S"
    ,s_suit = "A82"
    ,h_suit = "963"
    ,d_suit = "76"
    ,c_suit = "AK986"
    )
tournament_board.add_card(direction = "W"
    ,s_suit = "KJ953"
    ,h_suit = "A8"
    ,d_suit = "T853"
    ,c_suit = "J5"
    )

tournament_board.set_info()

tournament_board.end_new_board()

print(tournament_board.get_full_board())



#board_1.valid_desk()




















