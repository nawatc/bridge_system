import argparse
import re

from bridge_system_gui import *

def Client_run(filename):
    # /Get code from main_function of file
    # and /Run it !
    
    # /Read Filename as variable data 
    with open(filename, "r") as f:
        data = f.readlines()
        #print(data)

    # /Cut get only main function
    # main function is if __name__ == "__main__":
    data = only_main(data)
    #print(data)

    # Execute code
    exec(data)



def only_main(code):
    # /Input code as list of line code.
    # /Output [string]    # or list

    # /Remove /Newline element ("\n").
    code = remove_newline(code)     

    # /Clear code to only main function
    n_quote = -1        # /Check that /Main function used /Single quote or /Double quote.
    index_line = 0      # /Line to Check Index
    index_str = ""      # /Real index in statement line
    index = 0           # /How many space /Before statement next to /Main function line
    R_code = []         # /Code to return (List)

    main_function_index_first = 0   # /Collect First index 
    main_function_index_last = 0    # /Collect Last index 

    #  !!! Beware main function must correct. else not found. 
    #                                                 if __name__ == "__main__" :
    main_function = ["if __name__ == '__main__':\n" ,'if __name__ == "__main__":\n']  # /Main function in /Single quote and /Double quote.

    if main_function[0] in code:
        # For /Main function that use /Single Quote.
        
        n_quote = 0

    elif main_function[1] in code:
        # For /Main function that use /Double Quote.
        
        n_quote = 1
        
    else:
        # /Not found both /Print Error and /Exit function.
        print("Error : Main function not found in file")
        return None

    
    # /Get Index /Next to /Main function line.
    index_line = code.index(main_function[n_quote]) + 1             # /Check that /Main function on which list index.
    main_function_index_first = code.index(main_function[n_quote])  # /Get first index from code

    # /Get Text /From statement line.
    txt = code[index_line]

    # /Get Text Index /From statement line.
    index_str = re.findall("\s+", txt)[0]

    # /Get Index number from index_str
    index = len(index_str)

    # /Get Index that Last line of statement
    count_line = 0  # count line that has index.

    for line in code[main_function_index_first + 1:]:   # loop every line since main function line untill no index line.
        #print(line)
        if line[:index] == index_str:   # Check if this line has index
            count_line = count_line + 1     # if has index count it.
        else:
            break                           # if not stop it.
    
    # /Get last line index
    main_function_index_last = main_function_index_first + 1 + count_line

    # /Get list to return
    R_code = code[main_function_index_first:main_function_index_last]

    # /Return code only main function
        # Return as list
    #print(R_code)
    #return R_code

        # Return as string
    R_string_code = ''.join(R_code)
    #print(R_string_code)
    return R_string_code
    



def remove_newline(input):
    # /Input list ,Return list
    # /Remove list element that are newline( \n )
    
    output = []

    for line in input:
        if line == '\n':
            pass
        else:
            output.append(line)

    return output





#######################################################################################################################################################
def play():
    print("play !")


def act1():
    print('act1')

def act2():
    print('act2')







if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument("a")

    args = parser.parse_args()  

    parser.add_argument("a", nargs='?', default="check_string_for_empty")

    # Function for Argument
    #
    # No argument
    if args.a == 'check_string_for_empty':
        print ('I can tell that no argument was given and I can deal with that here.')
    
    # Argument list
    elif args.a == 'magic.name':
        print ('You nailed it!')

    elif args.a == 'start_gui':
        #Client_run("main_windows.py")  # Old filename
        Client_run("gui_interface.py")
        
    elif args.a == 'help':
        word_help = """
        help      : Start help manual
        start_gui  : Start Gui for program


        """
        print(word_help)

    # Else Argument
    else:
        #print (args.a)
        print ("No argument try --help")

    #Client_run("test.py")
    #Client_run("main_windows.py")

    args = parser.parse_args()
    









    




    
"""
    if      args.command == 'delete':
        print('Run delete')
    elif    args.command == 'app':
        Client_run("main_windows.py")


        pass

    elif    args.command == 'search':
        print('Run search')
    else:
        print('Run list')
    
"""
    


























