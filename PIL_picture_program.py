from re import X
import PIL
from PIL import Image ,ImageFont ,ImageDraw
 
 
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

    # F-ull input_dict_desk format
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


    ############ Load picture ############

    #pic_4hand = Image.open('picture_resource/pic_4hand_default.png')
    pic_4hand       = Image.new('RGB',(440, 440) ,"white")
    #pic_4hand       = Image.new('RGB',(440, 440) ,"green")
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

        # N
    text_length = get_textwidth(text_fulldesk_N, selected_font="arial.ttf", font_size=18)   # get text length
    
    x_point = ( int(pic_4hand.width/2) - int((text_length + pic_space.width )/2) )          # text start x point (include suit pic)
    
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
    text_length = get_textwidth(text_fulldesk_S, selected_font="arial.ttf", font_size=18)   # get text length
    
    x_point = ( int(pic_4hand.width/2) - int((text_length + pic_space.width )/2) )          # text start x point (include suit pic)
    
    image_editable.text(xy = (x_point + pic_space.width,340), text = text_fulldesk_S,font = title_font ,fill = (0, 0, 0))
    
    pic_4hand.paste(pic_space   , (x_point,340+(21*0)) )
    pic_4hand.paste(pic_heart   , (x_point,340+(21*1)) )
    pic_4hand.paste(pic_diamond , (x_point,340+(21*2)) )
    pic_4hand.paste(pic_club    , (x_point,340+(21*3)) )


    # Save Pic
    #pic_4hand.save("result.png")
    pic_4hand.save("picture_resource/result.png")


# use function
"""dict_desk = {
        "North" : {
            "S" : ["AKQJT98765432"] ,
            "H" : ["AKQJT98765432"] ,
            "D" : ["AKQJT98765432"] ,
            "C" : ["AKQJT98765432"]
        } ,
        "East" : {
            "S" : ["AKQJT98765432"] ,
            "H" : ["AKQJT98765432"] ,
            "D" : ["AKQJT98765432"] ,
            "C" : ["AKQJT98765432"]
        } ,
        "South" : {
            "S" : ["AKQJT98765432"] ,
            "H" : ["AKQJT98765432"] ,
            "D" : ["AKQJT98765432"] ,
            "C" : ["AKQJT98765432"]
        } ,
        "West" : {
            "S" : ["AKQJT98765432"] ,
            "H" : ["AKQJT98765432"] ,
            "D" : ["AKQJT98765432"] ,
            "C" : ["AKQJT98765432"]
        }
    }
"""
#make_pic_4hand(dict_desk)


