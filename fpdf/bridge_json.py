# Do not named this file "json.py"

from pickle import NONE
from bridge import get_dealer ,get_vul ,hcp_point_count_by_str
import json


class bridge_json():
    def __init__(self ,board_num):
        # Add board number
        self.dict = {'board': board_num}
        self.all_board_dir = ["N","E","S","W"]
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

    def add_card(self,direction ,s_suit ,h_suit ,d_suit ,c_suit):
        # Add Card to dict by key [direction]_HCP     example. -> dict["N_hand"] = ["s_suit" ,"h_suit" ,"d_suit" ,"c_suit"]
        if direction in self.all_board_dir:
            self.dict[direction+"_card"] = [s_suit ,h_suit ,d_suit ,c_suit]
        else:
            print("Input Dirction invaild")
            
    def set_hcp_by_card(self):
        # Add HCP to dict, calcuate by added card

        for i in self.all_board_dir:
            # Add by each Hand

            # Display Add data
            #print(hcp_point_count_by_str_list(self.dict[i+"_card"]))

            # Add in dict by key [direction]_HCP     example. -> dict["N_HCP"] = 12
            self.dict[i + "_HCP"] = hcp_point_count_by_str(self.dict[i+"_card"])













    def add_key(self,key ,value):
        self.dict['mynewkey'] = 'mynewvalue'

    def dump(self,):
        with open("data_file.json", "w") as write_file:
            json.dump(self.dict, write_file)



board_1 = bridge_json(board_num = 1)
board_1.add_card(direction = "N"
    ,s_suit = "T"
    ,h_suit = "K542"
    ,d_suit = "KQ42"
    ,c_suit = "Q72"
    )
board_1.add_card(direction = "E"
    ,s_suit = "Q64"
    ,h_suit = "QJT7"
    ,d_suit = "AJ9"
    ,c_suit = "T43"
    )
board_1.add_card(direction = "S"
    ,s_suit = "A82"
    ,h_suit = "963"
    ,d_suit = "76"
    ,c_suit = "AK986"
    )
board_1.add_card(direction = "W"
    ,s_suit = "KJ953"
    ,h_suit = "A8"
    ,d_suit = "T853"
    ,c_suit = "J5"
    )

board_1.set_hcp_by_card()



#board_1.valid_desk()



board_1.dump()



















