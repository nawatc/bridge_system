# -*- coding: utf-8 -*-
# import sys
# from io import TextIOWrapper
# sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='UTF-8', errors='replace')

from fpdf import FPDF

from porter_bridges.board_info import get_dealer_from_board_number ,get_vul_from_board_number ,hcp_point_count_by_str
from porter_bridges.porter_bridges import pbn_to_dict

import ddstable_standalone as ddstable_standalone


# Add Text To Images With Pillow - Python Tkinter GUI Tutorial 203
# https://www.youtube.com/watch?v=bmzDUQRPEdE

# Ref.
# https://github.com/reingart/pyfpdf/blob/master/docs/ReferenceManual.md

# Docs
# https://github.com/reingart/pyfpdf/tree/master/docs


class PDF(FPDF):
    def __init__(self):
        super().__init__()      # Inheritance all Method and Property

        self.header_title = ""                          # Header Name

        self.set_margins(0.1 , 1.5, -0.1)               # Set Margins for all page
        self.set_auto_page_break(False, margin = 0.0)   # Disables Auto page breaking mode

        
    def set_header_title(self ,header_title):
        self.header_title = header_title
    
    def get_header_title(self):
        return self.header_title


    # Set Header & Footer 

    def header(self):
        # Set Font to Times Bold Size = 20
        self.set_font('Times', 'B', 20)
        # Draw 3 Headline
        self.set_line_width( 0.1 )
        self.line(1 , 0.5, 209, 0.5)
        self.line(1 , 1, 209, 1)
        self.line(1 , 9.5, 209, 9.5)
        # Calculate width of title and position
        w = self.get_string_width(self.header_title)# + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_fill_color(255, 255, 255)
        self.set_text_color( 4, 5, 211)
        # Title
        self.cell(w, 7, self.header_title, 0, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 0.7 cm from bottom
        self.set_y(-7)
        # Set Fonts to Arial italic Size = 8
        self.set_font('Arial', 'I', 8)
        # Set Text Color
        #self.set_text_color(231 ,231 ,231)     # Text color to Gray
        self.set_text_color( 4, 5, 211)         # Text color to Blue
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    
    

    # Main function to make pdf

    def print_board(self, Board_num, dealer, vul, desk):
        # Function to write 1 Board to Body of PDF
        
        # Add New Pages Every 12 Board passed (1 page can collect 12 Board)
        if ( (Board_num % 12) == 1):
            self.add_page()
            
        # Add Property of Board
        self.draw_box(Board_num)                            # Draw Box
        self.board_information(Board_num, dealer, vul)      # Draw Board Info
        self.draw_dds(Board_num ,desk)                      # Draw DDS Info
        self.draw_card(Board_num ,desk)                     # Draw Card in Board
        self.draw_hcp(Board_num ,desk)                      # Draw HCP of card in Board
        self.draw_gametype(Board_num ,desk)                 # Draw Gametype Info





    # Sub function to make pdf
    def draw_gametype(self, position ,desk):
        # Set text
        self.set_font('Arial', '', 10)      # Set Fonts and Size
        self.set_text_color( 4, 2, 3)        # Text color To Black.

        # Get Position
        x_start , y_start = self.start_point_from_position(position)

        # Draw Text
        line = desk[1]    # "Grand Slam"
        
        self.set_xy(x_start + 10, y_start + 20)
        self.cell(w = 2, h = 1, txt = line ,align = 'C')



    def draw_hcp(self, position ,desk):
        # Set text
        self.set_font('Arial', '', 10)      # Set Fonts and Size
        self.set_text_color( 4, 2, 3)        # Text color To Black.

        # Get Position
        x_start , y_start = self.start_point_from_position(position)

        # Draw Image to Center of Board
        self.image(name = """picture_resource\pic_hcp_2.png""", x = x_start + 90, y = y_start + 37, w = 8, h = 5, type = 'PNG')

        # Draw Text
        # PBN to Dict
        # 'N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.'
        # {'North': {'S': 'J72', 'H': 'QT', 'D': 'JT4', 'C': 'T9843'}, 'East': {'S': 'Q983', 'H': 'J872', 'D': 'A7', 'C': 'AK7'}, 'South': {'S': 'AKT54', 'H': 'AK5', 'D': 'K6532', 'C': ''}, 'West': {'S': '6', 'H': '9643', 'D': 'Q98', 'C': 'QJ652'}}
        desk_dict = pbn_to_dict(desk[0])

        count_list = []

        # Calulate HCP and Draw Text
        for i in ['North','East','South','West']:
            for j in ['S', 'H', 'D', 'C']:

                count_list.append(desk_dict[i][j])      # Add Text to list  -> ['J72','QT','JT4','T9843']

            hcp = hcp_point_count_by_str(count_list)    # Get HCP

            count_list = []     # Reset list
        
            # Setting x ,y For Direction
                # Setting x ,y For Direction
            if i == 'West':
                x_dir ,y_dir =  86   , 39

            elif i == 'North':
                x_dir ,y_dir =  93   , 34

            elif i == 'South':
                x_dir ,y_dir =  93   , 44

            elif i == 'East':
                x_dir ,y_dir =  100   , 39


            # Draw Text
            line = str(hcp)     
                    
            self.set_xy(x_start + x_dir , y_start + y_dir)
            self.cell(w = 2, h = 1, txt = line ,align = 'C')








    def draw_card(self ,position ,desk):
        # Set text
        self.set_font('Arial', '', 10)      # Set Fonts and Size
        self.set_text_color( 4, 2, 3)        # Text color To Black.

        # Get Position
        x_start , y_start = self.start_point_from_position(position)
        x_dir , y_dir   = 0 , 0
        x_suit , y_suit = 0 , 0

        # Draw Image to Center of Board
        self.image(name = """picture_resource\pic_nsew_2.png""", x = x_start + 55, y = y_start + 18, w = 12, h = 12, type = 'PNG')

        # Draw Text
        # PBN to Dict
        # 'N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.'
        # {'North': {'S': 'J72', 'H': 'QT', 'D': 'JT4', 'C': 'T9843'}, 'East': {'S': 'Q983', 'H': 'J872', 'D': 'A7', 'C': 'AK7'}, 'South': {'S': 'AKT54', 'H': 'AK5', 'D': 'K6532', 'C': ''}, 'West': {'S': '6', 'H': '9643', 'D': 'Q98', 'C': 'QJ652'}}
        desk_dict = pbn_to_dict(desk[0])

        #print(desk_dict["North"]["S"]) 

        
        for i in ['North','East','South','West']:
            # Draw Text By Direction
                # Setting x ,y For Direction
            if i == 'West':
                x_dir ,y_dir =  22   , 19

            elif i == 'North':
                x_dir ,y_dir =  53.5 , 3

            elif i == 'South':
                x_dir ,y_dir =  53.5 , 34

            elif i == 'East':
                x_dir ,y_dir =  68   , 19


            for j in ['S', 'H', 'D', 'C']:
            # Draw Text By Suit
                # Setting x ,y , color ,picture For Suit
                if j == 'S':
                    x_suit , y_suit = 0 , 0
                    self.set_text_color( 4, 2, 3)        # Text color To Black
                    name = """picture_resource\space_2.png"""

                elif j == 'H':
                    x_suit , y_suit = 0 , 3.5
                    self.set_text_color(233, 47, 32)     # Text color To Red
                    name = """picture_resource\heart_2.png"""

                elif j == 'D':
                    x_suit , y_suit = 0 , 7
                    self.set_text_color(233, 47, 32)     # Text color To Red
                    name = """picture_resource\diamond_2.png"""

                elif j == 'C':
                    x_suit , y_suit = 0 , 10.5
                    self.set_text_color( 4, 2, 3)        # Text color To Black
                    name = """picture_resource\club_2.png"""


                # Draw Text

                #line = j + ":" + desk_dict[i][j]
                line = desk_dict[i][j]
                    
                self.set_xy(x_start + x_dir + x_suit  + 2.5, y_start + y_dir + y_suit)
                self.cell(w = 2, h = 1, txt = line ,align = 'L')


                # Draw Suit Picture
                self.image(name = name, x = x_start + x_dir + x_suit, y = y_start + y_dir + y_suit - 1.3, w = 3, h = 3, type = 'PNG')
                    








        
        
    def draw_box(self ,position):
        # position in range 1 to 12
        y_long = 47  # mm , height of box
        x_long = 104 # mm , wide of box

        # y_header = 10 # mm point from header
        # x_header = 0  # mm point from header

        # Set color of box
        self.set_draw_color(0 ,0 ,0)  # to Black

        # Get Position
        x_start , y_start = self.start_point_from_position(position)

        self.rect(x_start, y_start, x_long, y_long, style = '')


    def board_information(self ,position ,dealer ,vul):
        # Function to write Board Info (on Top left Corner)   

        # Set Fonts and Color
        self.set_font('Times', '', 12)
        self.set_text_color( 4, 5, 211)     # Text color is Blue.

        # Get Position
        x_start , y_start = self.start_point_from_position(position)

        # Line 1    Board Number
        line_1 = "Board: " + str(position)

        self.set_xy(x_start + 1, y_start + 4)
        self.cell(w = 10, h = 0, txt = line_1)

        # Line 2    Dealer's Hand
        line_2 = "Dealer: " + dealer

        self.set_xy(x_start + 1, y_start + 8)
        self.cell(w = 10, h = 0, txt = line_2)
        
        # Line 3    Board's Value
        line_3 = "Vul: " + vul

        self.set_xy(x_start + 1, y_start + 12)
        self.cell(w = 10, h = 0, txt = line_3)


    def draw_dds(self ,position ,desk):
        # Function to write DDS Solution (on Bottom Left Corner)
        
        # Get Position
        x_start , y_start = self.start_point_from_position(position)

        # Draw Gray Background
            # Set color of box
        self.set_draw_color(231 ,231 ,231)  # Set to Gray
        self.set_fill_color(231 ,231 ,231)  # Set to Gray

            # Set Height & Width
        y_long = 16.5 # mm , height of box
        x_long = 20 # mm , wide of box

            # Draw Gray
        self.rect(x_start + 2, y_start + 28, x_long, y_long, style = 'DF')

        # Draw Text
            # Set text
        self.set_font('Arial', '', 10)
        self.set_text_color( 4, 5, 211)

            # Get DDS Info
        text_PBN = desk[0]
        text_PBN_encode = text_PBN.encode()
        all = ddstable_standalone.get_ddstable(text_PBN_encode)
        #print(all)

            # Draw Text
                # Adjust Info
                    # Default Info Example
        """
        all = {     'N': {'S': 4, 'H': 7, 'D': 4, 'C': 3, 'NT': 3}, 
                    'S': {'S': 4, 'H': 7, 'D': 4, 'C': 3, 'NT': 3}, 
                    'E': {'S': 6, 'H': 6, 'D': 8, 'C': 9, 'NT': 8}, 
                    'W': {'S': 6, 'H': 6, 'D': 8, 'C': 9, 'NT': 10} }
        """
                    # Change All play   to Level play
        for i in ["N","E","W","S"]:
            for j in ['S', 'H', 'D', 'C', 'NT']:

                if all[i][j] >= 7:
                    all[i][j] = all[i][j] -6
                else:
                    all[i][j] = 0


                    # Add Head table        #       " " NT S H D C

        all[' '] = {'S': "S", 'H': "H", 'D': "D", 'C': "C", 'NT': "NT"}
        line_key  = [ " ","N","S","E","W"]

                    # Add Left table        #       " " N E W S

        for i in list(all.keys()): # ['N', 'S', 'E', 'W', ' ']
            #print(all[i])
            all[i][" "] = i
        all_key   = [ " ","NT","S","H","D","C"]


                # Draw Text to PDF
        for i in range(0 ,len(line_key)):
            #print(line_key[i])
            
            for j in range(0 ,len(all_key)):
                #print(all_key[j])
                #print(all[line_key[i]][all_key[j]])


                    # Set Color     #       " " NT S H D C

                if all_key[j] == " " or all_key[j] == "S" or all_key[j] == "C" :
                    self.set_text_color( 4, 2, 3)       # Text color To Black

                elif all_key[j] == "NT" :
                    self.set_text_color( 4, 5, 211)     # Text color To Blue

                elif all_key[j] == "H" or all_key[j] == "D" :
                    self.set_text_color(233, 47, 32)    # Text color To Red

                else:
                    self.set_text_color( 4, 2, 3)       # Text color To Black


                    # Adjust Text
                        # Blank  If Level = 0
                if all[line_key[i]][all_key[j]] == 0:
                    txt = " "
                        # if NT make it N
                elif all[line_key[i]][all_key[j]] == "NT":
                    txt = "N"
                else:
                    txt = str(all[line_key[i]][all_key[j]])
                
                    # Draw Text
                
                #txt = str(all[line_key[i]][all_key[j]])
                self.set_xy(x_start + (3.2) + (j*3.2), y_start + 30 + (i*3.2))
                self.cell(w = 1, h = 0, txt = txt ,align = 'C')
        

    def start_point_from_position(self ,position):
        # position in range 1 to 12
        y_long = 47  # mm , height of box
        x_long = 104 # mm , wide of box

        y_header = 10 # mm point from header
        x_header = 0  # mm point from header

        if position < 1 :   # for zero error
            position = 1
        elif position > 0 : # for 1-12 board
            position = position % 12
        else :              # for accidently get string number
            position = int(position) 

        if position == 0:   # board 12 mod 12 will be 0, so make zero to 12.
            position = 12

        position = position - 1 # First position start with 0 to 11 in 1 page
        
        if position % 2 == 0:
            # start point left box
            x = 1
        else:
            # start point right box
            x = 1 + x_long
        
        x_start = x + x_header
        y_start = ( ( position // 2 ) * y_long ) + y_header # plus 10 mm for header (y_header)

        return x_start ,y_start



# Example

    # Example Info
#title_pdf = 'Open Pairs - Mon.5.10.20'
title_pdf = 'Bridge System - PDF'
author = 'Project-Bridge-system'

output_filename = title_pdf + ".pdf"


    # Setting to pdf
pdf = PDF()                 
pdf.set_header_title(title_pdf)     # Set Header Title
pdf.set_title(title_pdf)            # Set Document Title
pdf.set_author(author)              # Set Document Author


    # Example Desk
desk = [['N:A842.QT3.K8.J652 E:75.AJ6542.92.KQ4 W:KT3.97.AQT64.T87 S:QJ96.K8.J753.A93', 'Part score']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:AKQJT98765432... E:.AKQJT98765432.. W:..AKQJT98765432. S:...AKQJT98765432', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']   # #12

      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']   # #24

      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']]  # #33

    # Create Board from Desk
for Board_num in range(1 ,len(desk) + 1):
    pdf.print_board(Board_num, get_dealer_from_board_number(Board_num) ,get_vul_from_board_number(Board_num) ,desk[Board_num - 1])


    #print(desk[Board_num - 1])

    

    # Save file
pdf.output(output_filename, 'F')    # Save to a local file




