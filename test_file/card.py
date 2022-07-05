import re

def text_to_pbn_check(input_text):
    #input_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" with on sort
    #
    #output is 
    # No Error : ["No Error"]
    # Error    : ["Error"   ,"N not found","E not found","S not found","W not found"]

    output = []

    N_text = re.findall('N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    E_text = re.findall('E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    S_text = re.findall('S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    W_text = re.findall('W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)

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


    return output


def text_to_pbn(input_text):
    #input_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" with on sort
    #output_text is "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63" sort by N E S W
    N_text = re.findall('N:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    print(N_text)
    E_text = re.findall('E:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    S_text = re.findall('S:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)
    W_text = re.findall('W:[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}\.[AKQJT98765432]{0,13}', input_text)

    output_text = N_text[0] + " " \
                + E_text[0] + " " \
                + S_text[0] + " " \
                + W_text[0]

    return output_text

print(text_to_pbn_check("N:QJT5432.T.6. E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"))
print(text_to_pbn("N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"))