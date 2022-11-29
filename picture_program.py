from re import X
#import PIL
from PIL import Image ,ImageFont ,ImageDraw

import ddstable_standalone as ddstable_standalone

import copy     # for copy dict
import ddstable


# Get function
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









def get_textwidth(text, selected_font='arial.ttf', font_size=18):
    # parameters
    text = text
    selected_font = selected_font
    font_size = font_size

    # get the size of the text
    img = Image.new('RGBA', (0,0), (255, 255, 255, 0))
    font = ImageFont.truetype(selected_font, font_size)
    draw = ImageDraw.Draw(img)
    text_size = draw.textsize(text, font)

    # resize and draw
    img = img.resize(text_size)
    draw.text((0,0), text, (0,0,0), font)

    #img.save('signature.png')
    
    return img.width





def make_pic_4hand(input_dict_desk) :
    # Make picture of 4hand card from desk

    # Full input_dict_desk format
    """
    dict_desk = {
        "North" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        } ,
        "East" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        } ,
        "South" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        } ,
        "West" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        }
    }

    
    """
    ############ Set input to variable ############
    dict_desk = input_dict_desk
    dict_desk_for_calculate = copy.deepcopy(input_dict_desk)    # Copy Data not refer data to dict_desk

    if input_dict_desk == {}:
        # If input_dict_desk is blank 
        dict_desk = {
        "North" : {
            "S" : "      -      " ,
            "H" : "      -      " ,
            "D" : "      -      " ,
            "C" : "      -      "
        } ,
        "East" : {
            "S" : "      -      " ,
            "H" : "      -      " ,
            "D" : "      -      " ,
            "C" : "      -      "
        } ,
        "South" : {
            "S" : "      -      " ,
            "H" : "      -      " ,
            "D" : "      -      " ,
            "C" : "      -      "
        } ,
        "West" : {
            "S" : "      -      " ,
            "H" : "      -      " ,
            "D" : "      -      " ,
            "C" : "      -      "
        }
        }
    else :
        # Else Set as Input
        dict_desk = input_dict_desk

    # Change Blank Suit ("") to "      -      "
    for i in ["North","East","South","West"]:
        for j in ["S","H","D","C"]:
            if dict_desk[i][j] == "":
                dict_desk[i][j] = "  - "

    
    ############ Load Picture ############

    #pic_4hand = Image.open('picture_resource/pic_4hand_default.png')
    #pic_4hand       = Image.new('RGB',(440, 440) ,"white")
    pic_4hand       = Image.new('RGB',(440, 440) ,"green")
    pic_4direction  = Image.open('picture_resource/pic_nsew_2.png')

    pic_space       = Image.open('picture_resource/space_2.png')
    pic_heart       = Image.open('picture_resource/heart_2.png')
    pic_diamond     = Image.open('picture_resource/diamond_2.png')
    pic_club        = Image.open('picture_resource/club_2.png')

    # Add Fonts
    title_font = ImageFont.truetype("arial.ttf", size = 18, encoding="unic")

    # Add Text
    #text_fulldesk = "AKQJT98765432\nAKQJT98765432\nAKQJT98765432\nAKQJT98765432"   # Full format
    #text_fulldesk = "      -      \n      -      \n      -      \n      -      "   # Blank format

    text_fulldesk_N = dict_desk["North"]["S"]  + "\n" + dict_desk["North"]["H"]    + "\n" + dict_desk["North"]["D"]    + "\n" + dict_desk["North"]["C"]
    text_fulldesk_W = dict_desk["West"]["S"]   + "\n" + dict_desk["West"]["H"]     + "\n" + dict_desk["West"]["D"]     + "\n" + dict_desk["West"]["C"]
    text_fulldesk_E = dict_desk["East"]["S"]   + "\n" + dict_desk["East"]["H"]     + "\n" + dict_desk["East"]["D"]     + "\n" + dict_desk["East"]["C"]
    text_fulldesk_S = dict_desk["South"]["S"]  + "\n" + dict_desk["South"]["H"]    + "\n" + dict_desk["South"]["D"]    + "\n" + dict_desk["South"]["C"]
    

    ############ Edit pic_4hand ############
    
    # Add pic_4direction    to      Middle of pic_4hand
    pic_4hand.paste(pic_4direction, (int(pic_4hand.width/2) - int(pic_4direction.width/2) ,int(pic_4hand.height/2) - int(pic_4direction.height/2) ) )

    # Add text and suit pic
    image_editable = ImageDraw.Draw(pic_4hand)

    # Edit Text to make North ,South Index equal
    text_length_N = get_textwidth(text_fulldesk_N, selected_font="arial.ttf", font_size=18)   # get text length
    text_length_S = get_textwidth(text_fulldesk_S, selected_font="arial.ttf", font_size=18)   # get text length
    
    if text_length_N > text_length_S:
        # If N more than S ,make S high as N
        text_length_S = text_length_N
    elif text_length_S > text_length_N:
        # If S more than N ,make N high as S
        text_length_N = text_length_S
    else:
        # Else (Equal) make it equal (forget it)
        pass
    

        # N
    #text_length = get_textwidth(text_fulldesk_N, selected_font="arial.ttf", font_size=18)   # get text length
    
    x_point = ( int(pic_4hand.width/2) - int((text_length_N + pic_space.width )/2) )          # text start x point (include suit pic)
    
    image_editable.text(xy = (x_point + pic_space.width,20), text = text_fulldesk_N,font = title_font ,fill = (0, 0, 0))
    
    pic_4hand.paste(pic_space   , (x_point,20+(21*0)) )
    pic_4hand.paste(pic_heart   , (x_point,20+(21*1)) )
    pic_4hand.paste(pic_diamond , (x_point,20+(21*2)) )
    pic_4hand.paste(pic_club    , (x_point,20+(21*3)) )

        # W
    text_length = get_textwidth(text_fulldesk_W, selected_font="arial.ttf", font_size=18)   # get text length
    
    x_point = 20 -10 + ( int((180 - 20)/2) - int((text_length + pic_space.width )/2) )      # text start x point (include suit pic)
    
    image_editable.text(xy = (x_point + pic_space.width,178), text = text_fulldesk_W,font = title_font ,fill = (0, 0, 0))
    
    pic_4hand.paste(pic_space   , (x_point,178+(21*0)) )
    pic_4hand.paste(pic_heart   , (x_point,178+(21*1)) )
    pic_4hand.paste(pic_diamond , (x_point,178+(21*2)) )
    pic_4hand.paste(pic_club    , (x_point,178+(21*3)) )

        # E
    text_length = get_textwidth(text_fulldesk_E, selected_font="arial.ttf", font_size=18)   # get text length
    
    x_point = 280 -10 + ( int((180 - 20)/2) - int((text_length + pic_space.width )/2) )     # text start x point (include suit pic)
    
    image_editable.text(xy = (x_point + pic_space.width,178), text = text_fulldesk_E,font = title_font ,fill = (0, 0, 0))
    
    pic_4hand.paste(pic_space   , (x_point,178+(21*0)) )
    pic_4hand.paste(pic_heart   , (x_point,178+(21*1)) )
    pic_4hand.paste(pic_diamond , (x_point,178+(21*2)) )
    pic_4hand.paste(pic_club    , (x_point,178+(21*3)) )

        # S
    #text_length = get_textwidth(text_fulldesk_S, selected_font="arial.ttf", font_size=18)   # get text length
    
    x_point = ( int(pic_4hand.width/2) - int((text_length_S + pic_space.width )/2) )          # text start x point (include suit pic)
    
    image_editable.text(xy = (x_point + pic_space.width,340), text = text_fulldesk_S,font = title_font ,fill = (0, 0, 0))
    
    pic_4hand.paste(pic_space   , (x_point,340+(21*0)) )
    pic_4hand.paste(pic_heart   , (x_point,340+(21*1)) )
    pic_4hand.paste(pic_diamond , (x_point,340+(21*2)) )
    pic_4hand.paste(pic_club    , (x_point,340+(21*3)) )


    ############################ Add Bo ############################
    draw = ImageDraw.Draw(pic_4hand)
    draw.rectangle(((10, 300), (130, 400)), fill="gray")


    # Get Data

    # Standard blank value
    c1 = [" ","N","S","E","W"]
    c2 = ["N","-","-","-","-"]
    c3 = ["S","-","-","-","-"]
    c4 = ["H","-","-","-","-"]
    c5 = ["D","-","-","-","-"]
    c6 = ["C","-","-","-","-"]
        
    r = [c1,c2,c3,c4,c5,c6]

    
    if dict_desk == {   'North': {'S': '      -      ', 'H': '      -      ', 'D': '      -      ', 'C': '      -      '}
                    ,   'East' : {'S': '      -      ', 'H': '      -      ', 'D': '      -      ', 'C': '      -      '}
                    ,   'South': {'S': '      -      ', 'H': '      -      ', 'D': '      -      ', 'C': '      -      '}
                    ,   'West' : {'S': '      -      ', 'H': '      -      ', 'D': '      -      ', 'C': '      -      '}}:

        pass

    else:

        
        #text_PBN = "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 W:AK96.KQ8.A98.K63 S:87.A62.QJT4.AT75"
        text_PBN = dict_to_text(dict_desk_for_calculate)
        text_PBN_encode = text_PBN.encode()
        #print(text_PBN_encode)
        all = ddstable_standalone.get_ddstable(text_PBN_encode)

        #print(all)

        c1 = [" ","N"                   ,"S"                    ,"E"                    ,"W"]
        c2 = ["N",str(all[c1[1]]["NT"]) ,str(all[c1[2]]["NT"])  ,str(all[c1[3]]["NT"])  ,str(all[c1[4]]["NT"]) ]
        c3 = ["S",str(all[c1[1]]["S"])  ,str(all[c1[2]]["S"])   ,str(all[c1[3]]["S"])   ,str(all[c1[4]]["S"]) ]
        c4 = ["H",str(all[c1[1]]["H"])  ,str(all[c1[2]]["H"])   ,str(all[c1[3]]["H"])   ,str(all[c1[4]]["H"]) ]
        c5 = ["D",str(all[c1[1]]["D"])  ,str(all[c1[2]]["D"])   ,str(all[c1[3]]["D"])   ,str(all[c1[4]]["D"]) ]
        c6 = ["C",str(all[c1[1]]["C"])  ,str(all[c1[2]]["C"])   ,str(all[c1[3]]["C"])   ,str(all[c1[4]]["C"]) ]



        r = [c1,c2,c3,c4,c5,c6]


    # Print Data

    x_start = 20
    y_start = 300
    x_p = 20
    y_p = 20
    
    for i in range(0,6):        # 1 Colume
        for j in range(0,5):    # 1 Row
            #draw.text(((x_start + x_p*i) - (get_textwidth(r[i][j]) / 2) , y_start + y_p*j), r[i][j], font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"),fill = "black")
            if i == 1:
                draw.text(((x_start + x_p*i) - (get_textwidth(r[i][j]) / 2) , y_start + y_p*j), r[i][j], font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"),fill = (0,0,255))
            elif i == 3 or i == 4:
                draw.text(((x_start + x_p*i) - (get_textwidth(r[i][j]) / 2) , y_start + y_p*j), r[i][j], font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"),fill = "red")
            else:
                draw.text(((x_start + x_p*i) - (get_textwidth(r[i][j]) / 2) , y_start + y_p*j), r[i][j], font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"),fill = "black")

    """
    # Draw First Row
    draw.text((55, 300), "N", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((75, 300), "S", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((95, 300), "H", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((115, 300), "D", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((135, 300), "C", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))

    # Draw First Colume
    draw.text((35, 300), " ", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((35, 320), "N", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((35, 340), "S", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((35, 360), "E", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    draw.text((35, 380), "W", font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))
    """


    ############################ Add HCP ############################
    draw = ImageDraw.Draw(pic_4hand)
    draw.rectangle(((310, 300), (430, 400)), fill="gray")

    pic_hcp       = Image.open('picture_resource/pic_hcp.png')
    pic_4hand.paste(pic_hcp   , (310, 300) )


    # Get Data
    #get_hcp_from_text
    hcp = [ 
        get_hcp_from_text(dict_desk["North"]["S"]) + get_hcp_from_text(dict_desk["North"]["H"]) + get_hcp_from_text(dict_desk["North"]["D"]) + get_hcp_from_text(dict_desk["North"]["C"]) ,
        get_hcp_from_text(dict_desk["East"]["S"])  + get_hcp_from_text(dict_desk["East"]["H"])  + get_hcp_from_text(dict_desk["East"]["D"])  + get_hcp_from_text(dict_desk["East"]["C"]) ,
        get_hcp_from_text(dict_desk["West"]["S"])  + get_hcp_from_text(dict_desk["West"]["H"])  + get_hcp_from_text(dict_desk["West"]["D"])  + get_hcp_from_text(dict_desk["West"]["C"]) ,
        get_hcp_from_text(dict_desk["South"]["S"]) + get_hcp_from_text(dict_desk["South"]["H"]) + get_hcp_from_text(dict_desk["South"]["D"]) + get_hcp_from_text(dict_desk["South"]["C"])
    ]
    # Print Data

    # N E W S
    #hcp = [ 10 ,7 ,10 ,10 ]

    # x middle 325 370 415
    # y middle 305 340 370

    text_length_N = get_textwidth(str(hcp[0]), selected_font="arial.ttf", font_size=18)   # get text length N
    text_length_E = get_textwidth(str(hcp[1]), selected_font="arial.ttf", font_size=18)   # get text length E
    text_length_W = get_textwidth(str(hcp[2]), selected_font="arial.ttf", font_size=18)   # get text length W
    text_length_S = get_textwidth(str(hcp[3]), selected_font="arial.ttf", font_size=18)   # get text length S

    draw.text((370 - (text_length_N/2), 305), str(hcp[0]), font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))    # N
    draw.text((415 - (text_length_E/2), 340), str(hcp[1]), font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))    # E
    draw.text((325 - (text_length_W/2), 340), str(hcp[2]), font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))    # W
    draw.text((370 - (text_length_S/2), 370), str(hcp[3]), font=ImageFont.truetype("arial.ttf", size = 18, encoding="unic"))    # S
        


    # Save Pic
    pic_4hand.save("picture_resource/result.png")

#make_pic_4hand({})














# Test function
"""
dict_desk = {
        "North" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        } ,
        "East" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        } ,
        "South" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        } ,
        "West" : {
            "S" : "AKQJT98765432" ,
            "H" : "AKQJT98765432" ,
            "D" : "AKQJT98765432" ,
            "C" : "AKQJT98765432"
        }
    }
"""

dict_desk =  {'North': {'S': 'QJT5432', 'H': 'T', 'D': '6', 'C': 'QJ82'}
     , 'East': {'S': '', 'H': 'J97543', 'D': 'K7532', 'C': '94'}
     , 'South': {'S': '87', 'H': 'A62', 'D': 'QJT4', 'C': 'AT75'}
     , 'West': {'S': 'AK96', 'H': 'KQ8', 'D': 'A98', 'C': 'K63'}}



make_pic_4hand(dict_desk)


