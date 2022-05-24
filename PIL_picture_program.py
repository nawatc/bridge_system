import PIL
from PIL import Image ,ImageFont ,ImageDraw
 
 






def make_pic_4hand(input_dict_desk) :

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
    }"""

    dict_desk = input_dict_desk


    # Load picture
    #pic_4hand = Image.open('picture_resource/pic_4hand_default.png')
    pic_4hand = Image.new('RGB',(440, 440) ,"white")
    pic_4direction = Image.open('picture_resource/pic_nsew_2.png')
    pic_space   = Image.open('picture_resource/space_2.png')
    pic_heart   = Image.open('picture_resource/heart_2.png')
    pic_diamond = Image.open('picture_resource/diamond_2.png')
    pic_club    = Image.open('picture_resource/club_2.png')

    # Add pic_4direction to pic_4hand
    pic_4hand.paste(pic_4direction, (int(440/2) - int(80/2) ,int(440/2) - int(80/2)) )

    # Add Fonts
    #title_font = PIL.ImageFont.load_path("C:\Windows\Fonts\timesbd.ttf")
    title_font = ImageFont.truetype("arial.ttf", size = 18, encoding="unic")
    #title_font = ImageFont.truetype("C:\Windows\Fonts\times.ttf", size = 28, encoding="unic")
    #title_font = ImageFont.load_default()
    
    # Add Text
    #text_fulldesk = "    AKQJT98765432\n    AKQJT98765432\n    AKQJT98765432\n    AKQJT98765432"

    text_fulldesk_N = "    " + dict_desk["North"]["S"] + "\n    " + dict_desk["North"]["H"] + "\n    " + dict_desk["North"]["D"] + "\n    " + dict_desk["North"]["C"]
    text_fulldesk_W = "    " + dict_desk["West"]["S"] + "\n    " + dict_desk["West"]["H"] + "\n    " + dict_desk["West"]["D"] + "\n    " + dict_desk["West"]["C"]
    text_fulldesk_E = "    " + dict_desk["East"]["S"] + "\n    " + dict_desk["East"]["H"] + "\n    " + dict_desk["East"]["D"] + "\n    " + dict_desk["East"]["C"]
    text_fulldesk_S = "    " + dict_desk["South"]["S"] + "\n    " + dict_desk["South"]["H"] + "\n    " + dict_desk["South"]["D"] + "\n    " + dict_desk["South"]["C"]
    #text_fulldesk_S = "    AKQJT98765432\n    AKQJT98765432\n    AKQJT98765432\n    AKQJT98765432"
    #print(text_fulldesk_W)
    
    image_editable = ImageDraw.Draw(pic_4hand)

    # N
    image_editable.text(xy = (int(220 - (152/2)),20), text = text_fulldesk_N,font = title_font ,fill = (0, 0, 0))

    pic_4hand.paste(pic_space   , (140,20+(21*0)) )
    pic_4hand.paste(pic_heart   , (140,20+(21*1)) )
    pic_4hand.paste(pic_diamond , (140,20+(21*2)) )
    pic_4hand.paste(pic_club    , (140,20+(21*3)) )

    # W
    image_editable.text(xy = (20,178), text = text_fulldesk_W,font = title_font ,fill = (0, 0, 0))

    pic_4hand.paste(pic_space   , (20,178+(21*0)) )
    pic_4hand.paste(pic_heart   , (20,178+(21*1)) )
    pic_4hand.paste(pic_diamond , (20,178+(21*2)) )
    pic_4hand.paste(pic_club    , (20,178+(21*3)) )

    # E
    image_editable.text(xy = (260,178), text = text_fulldesk_E,font = title_font ,fill = (0, 0, 0))

    pic_4hand.paste(pic_space   , (260,178+(21*0)) )
    pic_4hand.paste(pic_heart   , (260,178+(21*1)) )
    pic_4hand.paste(pic_diamond , (260,178+(21*2)) )
    pic_4hand.paste(pic_club    , (260,178+(21*3)) )


    # S
    image_editable.text(xy = (int(220 - (152/2)),340), text = text_fulldesk_S,font = title_font ,fill = (0, 0, 0))

    pic_4hand.paste(pic_space   , (140,340+(21*0)) )
    pic_4hand.paste(pic_heart   , (140,340+(21*1)) )
    pic_4hand.paste(pic_diamond , (140,340+(21*2)) )
    pic_4hand.paste(pic_club    , (140,340+(21*3)) )


    pic_4hand.save("result.png")



    #title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)
    #title_text = "The Beauty of Nature"
    #image_editable = ImageDraw.Draw(pic_4hand)
    #image_editable.text((15,15), title_text, (237, 230, 211))
    #pic_4hand.save("result.jpg")

    





#make_pic_4hand()



"""
# Location of the image
img = Image.open("picture_resource/pic_nsew.png")
 
img.show()

"""

"""
    dict_desk = {
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