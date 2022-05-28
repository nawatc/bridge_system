import re

class Desk:
    def __init__(self):
        North_Card = ""
        East_Card = ""
        South_Card = ""
        West_Card = ""

    

    def set_card(self,dir,card):
        if dir == "N":
            North_Card = card
        if dir == "E":
            East_Card = card
        if dir == "S":
            South_Card = card
        if dir == "W":
            West_Card = card

    def get_card_list(self,dir):
        if dir == "N":
            return list(self.North_Card)
        if dir == "E":
            return list(self.East_Card)
        if dir == "S":
            return list(self.South_Card)
        if dir == "W":
            return list(self.West_Card)



asd = Desk()








def pbn_to_dict(text):
    txt = text
    #txt = "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"

    #   North

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























        
