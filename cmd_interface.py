import argparse

from main_windows import *



class Client_simulator(object):
    def generator_main(self):

        # from main_windows.py
        # inline
        #
        # if __name__ == "__main__":
        # 

        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet("QLabel{font-size: 14pt;}")              # Set Default Font

        main_windows = BridgeWindow()
        main_windows.show()


        sys.exit( app.exec_() )


def main():    # you can name this whatever you want, it doesn't need to be main()
    Client_simulator().generator_main()

def play():
    print("play !")
    #print(args.accumulate(args.integers))











description = ""

parser = argparse.ArgumentParser(description=description)

"""
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

"""

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

FUNCTION_MAP = {'run'  : main,
                'play' : play
                }

parser.add_argument('command', choices=FUNCTION_MAP.keys())

args = parser.parse_args()

func = FUNCTION_MAP[args.command]
#func()




















print(args.accumulate(args.integers))