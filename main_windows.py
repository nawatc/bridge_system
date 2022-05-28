import sys
from PyQt5 import QtWidgets ,QtGui #, QtCore
from PyQt5.QtWidgets import QMainWindow ,QLabel ,QWidget ,QVBoxLayout ,QPushButton ,QTabWidget ,QLineEdit ,QHBoxLayout ,QShortcut #,QSizePolicy ,QFileDialog ,QGridLayout 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence ,QPixmap

#import ddstable
#from ddstable import ddstable
import ddstable_standalone

from PIL_picture_program import make_pic_4hand

import re

from porter_bridges.porter_bridges import pbn_to_dict

class BridgeWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        width , height = 1200,600
        
        #self.setMinimumSize(QSize(width, height))      # Set Windows Size
        self.setFixedSize(width, height)                # Set Windows Size That cannot resize
        self.setWindowTitle("Bridge system") 
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        

        self.show()

class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        #self.tabs.resize(300,200)

        # Create Tab
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        #self.tab3 = QWidget()
        
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Input Desk")
        self.tabs.addTab(self.tab2,"Display Selected Desk")
        #self.tabs.addTab(self.tab3,"Select Desk")

        # Add Tab to Main Windows
        self.layout_tab = QVBoxLayout(self)
        self.layout_tab.addWidget(self.tabs)










        #self.tabs.setCurrentIndex(1)        # Go to Tab 2 

        #########################################################################################################################################################################################

        # Add Shortcut key

        # Ctrl + W to Exit
        self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut.activated.connect(self.exit)

        #########################################################################################################################################################################################

        # Create first tab


        # Create Label

        #self.tab1_text1 = QLabel("Desk Code : N:Space.Heart.Diamond.Club E:Space.Heart.Diamond.Club S:Space.Heart.Diamond.Club W:Space.Heart.Diamond.Club")
        """self.tab1_text1 = QLabel('Desk Code : N:<font color="blue">♠</font>.<font color="red">♥</font>.<font color="orange">♦</font>.<font color="green">♣</font> ' +
        'E:<font color="blue">♠</font>.<font color="red">♥</font>.<font color="orange">♦</font>.<font color="green">♣</font> ' +
        'S:<font color="blue">♠</font>.<font color="red">♥</font>.<font color="orange">♦</font>.<font color="green">♣</font> ' +
        'W:<font color="blue">♠</font>.<font color="red">♥</font>.<font color="orange">♦</font>.<font color="green">♣</font> ')"""

        #self.tab1_text2 = QLabel("Example Input : N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63")    # Default Text
        self.tab1_text2 = QLabel('Example Input : N:<font color="blue">QJT5432</font>.<font color="red">T</font>.<font color="orange">6</font>.<font color="green">QJ82</font>' +
                                                ' E:<font color="blue"></font>.<font color="red">J97543</font>.<font color="orange">K7532</font>.<font color="green">94</font>' +
                                                ' S:<font color="blue">87</font>.<font color="red">A62</font>.<font color="orange">QJT4</font>.<font color="green">AT75</font>' +
                                                ' W:<font color="blue">AK96</font>.<font color="red">KQ8</font>.<font color="orange">A98</font>.<font color="green">K63</font>')

        self.line_input_desk = QLineEdit()
        #self.line_input_desk.setFixedWidth(750)
        self.line_input_desk.setMaximumWidth(750)                   # Set Width
        self.line_input_desk.setText("N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63") # Set Default Text
        self.line_input_desk.setStyleSheet('font-size: 14pt;')      # Set stylesheet for LineEdit

        self.line_input_desk_generate = QPushButton("Generate")
        self.line_input_desk_generate.clicked.connect(self.clicked_generate)
        self.line_input_desk_generate.setAutoDefault(1)             # Make button to click with Enter key
        self.line_input_desk_generate.setStyleSheet('font-size: 14pt;')

        # Create Layout and Add label
    
        self.tab1.layout_tab1_V = QVBoxLayout(self)
        #self.tab1.layout_tab1_V.addWidget(self.tab1_text1)
        self.tab1.layout_tab1_V.addWidget(self.tab1_text2)

        

        self.tab1.layout_tab1_H = QHBoxLayout()
        self.tab1.layout_tab1_H.addWidget(self.line_input_desk)
        self.tab1.layout_tab1_H.addWidget(self.line_input_desk_generate)

        self.tab1.layout_tab1_V.addLayout(self.tab1.layout_tab1_H)
    
        

        # End of first tab
        self.tab1.layout_tab1_V.addStretch()
        self.tab1.setLayout(self.tab1.layout_tab1_V)



        #########################################################################################################################################################################################
    
        # Create Secend tab

        # Create Label
        self.tab2_text1 = QLabel("Board : 1")
        self.tab2_text2 = QLabel("Dealer : N")
        self.tab2_text3 = QLabel("Vul : N-S")
        self.tab2_text4 = QLabel("Desk Code")
        self.tab2_text5 = QLabel("Sol.")

        # loading image
        self.pixmap = QPixmap('picture_resource/result_default.png')

        # creating label and adding image to label
        self.label_pic = QLabel(self)
        self.label_pic.setPixmap(self.pixmap)



        # Create Layout and Add label
        self.tab2.layout_tab2_H = QHBoxLayout(self)
        self.tab2.layout_tab2_V = QVBoxLayout(self)
        
        self.tab2.layout_tab2_V.addWidget(self.tab2_text1)
        self.tab2.layout_tab2_V.addWidget(self.tab2_text2)
        self.tab2.layout_tab2_V.addWidget(self.tab2_text3)
        self.tab2.layout_tab2_V.addWidget(self.tab2_text4)
        self.tab2.layout_tab2_V.addWidget(self.tab2_text5)

        self.tab2.layout_tab2_V.addLayout(self.tab2.layout_tab2_V)
        self.tab2.layout_tab2_V.addLayout(self.tab2.layout_tab2_V)


        self.tab2.layout_tab2_H.addLayout(self.tab2.layout_tab2_V)
        self.tab2.layout_tab2_H.addWidget(self.label_pic)


        




        





        # End of Secend tab
        self.tab2.layout_tab2_V.addStretch()
        self.tab2.setLayout(self.tab2.layout_tab2_H)


    
        #########################################################################################################################################################################################
    
        # Create Third tab

        # Create Label

        # Create Layout and Add label


        # End of Third tab
        #self.tab2.layout_tab2_V.addStretch()
        #self.tab2.setLayout(self.tab2.layout_tab2_V)








    @pyqtSlot()
    def clicked_generate(self):

        # Get line_input_desk string

        #print(self.line_input_desk.text())

        # Switch to 2nd Tab
        self.tabs.setCurrentIndex(1)

        self.tab2_text4.setText(self.line_input_desk.text())

        # to PBN
        text_PBN = self.line_input_desk.text()
        
        text_PBN = text_PBN.replace("E:", "")
        text_PBN = text_PBN.replace("S:", "")
        text_PBN = text_PBN.replace("W:", "")

        b = text_PBN.encode()
        
        all = ddstable_standalone.get_ddstable(b)
        #print(all)


        all_2 = ""

        all_2 = all_2 + "{:>5}\t{:>5} \t{:>5} \t{:>5} \t{:>5} \t{:>5}".format("", "S", "H", "D", "C", "NT")
        all_2 = all_2 + "\n"
        # may use  card_suit=["C", "D", "H", "S", "NT"]
        for each in all.keys():
            all_2 = all_2 + "{:>5}".format(each)
            for suit in ddstable_standalone.dcardSuit:
                trick=all[each][suit]
                if trick>7:
                    all_2 = all_2 + "\t{:5}".format(trick - 6)
                else:
                    all_2 = all_2 + "\t{:>5}".format("-")
            all_2 = all_2 + "\n"


        #print(all_2)
        self.tab2_text5.setText(all_2)


        # make pic
        input_text = self.line_input_desk.text()
        input_text = pbn_to_dict(input_text)
        make_pic_4hand(input_text)      # create pic of 4 hand of desk

        # loading image
        self.pixmap = QPixmap('picture_resource/result.png')
        self.label_pic.setPixmap(self.pixmap)


    

    def exit():
        sys.exit( app.exec_() )

        
    
















        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QLabel{font-size: 14pt;}")              # Set Default Font

    main_windows = BridgeWindow()
    main_windows.show()


    sys.exit( app.exec_() )


    