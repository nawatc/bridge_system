import sys ,os
from PyQt5 import QtWidgets ,QtGui #,QtCore 
from PyQt5.QtWidgets import QMainWindow ,QLabel ,QWidget ,QVBoxLayout ,QPushButton ,QTabWidget ,QLineEdit ,QHBoxLayout ,QMessageBox ,QShortcut ,QSizePolicy#,QTextEdit  #,QSizePolicy ,QFileDialog ,QGridLayout 
from PyQt5.QtCore    import pyqtSlot
from PyQt5.QtGui     import QKeySequence ,QPixmap  #,QColor


import ddstable_standalone as ddstable_standalone


from picture_program.picture_program import make_pic_4hand

from porter_bridges.random_number import random_card

from porter_bridges.porter_bridges import pbn_to_dict ,text_to_pbn_check ,text_to_pbn ,dict_to_desk ,deck_list_result  ,text_to_list_desk
from porter_bridges.board_info import get_dealer_from_board_number ,get_vul_from_board_number



class BridgeWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        width , height = 1200,600
        
        #self.setMinimumSize(QSize(width, height))      # Set Windows Size
        self.setFixedSize(width, height)                # Set Windows Size That cannot resize
        self.setWindowTitle("Bridge system") 
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.table_widget = MyTabsWidget(self)
        self.setCentralWidget(self.table_widget)
        
        

class MyTabsWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        #self.tabs.resize(300,200)

        # Create Tab
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        
        
        # Add Tabs
        self.tabs.addTab(self.tab1,"Main Menu")
        self.tabs.addTab(self.tab2,"Edit Board")
        self.tabs.addTab(self.tab3,"Display Board")
        self.tabs.addTab(self.tab4,"Choose from Database")
        self.tabs.addTab(self.tab5,"Export as PDF")
        
        self.tabs.setCurrentIndex(2)    # Go to tab 2

        # Add Tab to Main Windows
        self.layout_tab = QVBoxLayout(self)
        self.layout_tab.addWidget(self.tabs)

        #########################################################################################################################################################################################

        # Add Shortcut key

        # Ctrl + W to Exit
        #self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        #self.shortcut.activated.connect(self.exit)

        #########################################################################################################################################################################################

        # Create First tab
        
        # Create Main Layout and Add label
        self.tab1.layout_tab1_V_main = QVBoxLayout()
        self.tab1.setLayout(self.tab1.layout_tab1_V_main)


            # 1st Horizon Layout
        self.tab1.layout_tab1_H = QHBoxLayout()

                # Autogen Lable
        self.line_autogen = QLabel("Auto generate new Desk number : ")
        self.tab1.layout_tab1_H.addWidget(self.line_autogen)

                # Autogen Line Edit
        self.line_edit_autogen = QLineEdit()
        self.line_edit_autogen.setText("0") # Set Default Text
        self.line_edit_autogen.setStyleSheet('font-size: 14pt;')
        self.line_edit_autogen.setFixedWidth(100)
        #self.line_edit_autogen.setMaximumWidth(100)                   # Set Width
        self.tab1.layout_tab1_H.addWidget(self.line_edit_autogen)

                # Autogen Button
        self.button_autogen = QPushButton("Generate Desk")
        #self.button_autogen.clicked.connect(self.clicked_input_clear)
        self.button_autogen.setAutoDefault(1)                             # Make button to click with Enter key
        self.button_autogen.setStyleSheet('font-size: 14pt;')
        self.tab1.layout_tab1_H.addWidget(self.button_autogen)
        

        self.tab1.layout_tab1_H.addStretch()

            # Add 1st Horizon Layout into main Layout
        self.tab1.layout_tab1_V_main.addLayout(self.tab1.layout_tab1_H)


        


        # End of first tab
        
        # Add Stretch
        self.tab1.layout_tab1_V_main.addStretch()


        #########################################################################################################################################################################################
    
        # Create Second tab

        # Create Main Layout and Add label
        self.tab2.layout_tab2_V_main = QVBoxLayout()
        self.tab2.setLayout(self.tab2.layout_tab2_V_main)

        """
            # Vertical

            # 0st Horizon Layout
        self.tab2.layout_tab2_H_zero = QHBoxLayout()
        self.tab2.layout_tab2_V_main.addLayout(self.tab2.layout_tab2_H_zero)

                # Table Layout
        self.tab2.layout_tab2_Table_V = QVBoxLayout()
        self.tab2.layout_tab2_Table_V_right = QVBoxLayout()
        self.tab2.layout_tab2_H_zero.addLayout(self.tab2.layout_tab2_Table_V)
        self.tab2.layout_tab2_H_zero.addLayout(self.tab2.layout_tab2_Table_V_right)

                # Table 1 2 3
        self.tab2.layout_tab2_Table_H1 = QHBoxLayout()
        self.tab2.layout_tab2_Table_H2 = QHBoxLayout()
        self.tab2.layout_tab2_Table_H3 = QHBoxLayout()
        self.tab2.layout_tab2_Table_V.addLayout(self.tab2.layout_tab2_Table_H1)
        self.tab2.layout_tab2_Table_V.addLayout(self.tab2.layout_tab2_Table_H2)
        self.tab2.layout_tab2_Table_V.addLayout(self.tab2.layout_tab2_Table_H3)


                # Table 1-1         North Input
        self.tab2.layout_tab2_Table_V1_1 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H1.addLayout(self.tab2.layout_tab2_Table_V1_1)
                    # Add Lable
        self.lable_V1_1_lable_N = QLabel("North")
        self.tab2.layout_tab2_Table_V1_1.addWidget(self.lable_V1_1_lable_N)
                    # Add 13 button
        self.tab2.layout_tab2_Table_V1_1_H1 = QHBoxLayout()
        self.tab2.layout_tab2_Table_V1_1.addLayout(self.tab2.layout_tab2_Table_V1_1_H1)

        button_list = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
        for i in button_list:
            button = QPushButton(i.format(i), self)
            button.setMaximumWidth(20)
            #button.clicked.connect(lambda ch, i=i: self.function(i))      # < ---
            self.tab2.layout_tab2_Table_V1_1_H1.addWidget(button)

        #self.tab2.layout_tab2_Table_V1_1.addStretch()

                # Table 1-2         North Output
        self.tab2.layout_tab2_Table_V1_2 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H1.addLayout(self.tab2.layout_tab2_Table_V1_2)
                    # Add Lable
        self.lable_V1_2_lable_N = QLabel("North")
        self.tab2.layout_tab2_Table_V1_2.addWidget(self.lable_V1_2_lable_N)
        self.lable_V1_2_lable_N_s = QLabel("S : AKQJT98765432")
        self.lable_V1_2_lable_N_h = QLabel("H : ")
        self.lable_V1_2_lable_N_d = QLabel("D : ")
        self.lable_V1_2_lable_N_c = QLabel("C : ")

        self.tab2.layout_tab2_Table_V1_2.addWidget(self.lable_V1_2_lable_N_s)
        self.tab2.layout_tab2_Table_V1_2.addWidget(self.lable_V1_2_lable_N_h)
        self.tab2.layout_tab2_Table_V1_2.addWidget(self.lable_V1_2_lable_N_d)
        self.tab2.layout_tab2_Table_V1_2.addWidget(self.lable_V1_2_lable_N_c)


                # Table 1-3         East Input
        self.tab2.layout_tab2_Table_V1_3 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H1.addLayout(self.tab2.layout_tab2_Table_V1_3)
                    # Add Lable
        self.lable_V1_3_lable_E = QLabel("East")
        self.tab2.layout_tab2_Table_V1_3.addWidget(self.lable_V1_3_lable_E)
                    # Add 13 button
        self.tab2.layout_tab2_Table_V1_3_H1 = QHBoxLayout()
        self.tab2.layout_tab2_Table_V1_3.addLayout(self.tab2.layout_tab2_Table_V1_3_H1)

        button_list = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
        for i in button_list:
            button = QPushButton(i.format(i), self)
            button.setMaximumWidth(20)
            #button.clicked.connect(lambda ch, i=i: self.function(i))      # < ---
            self.tab2.layout_tab2_Table_V1_3_H1.addWidget(button)


        self.tab2.layout_tab2_Table_H1.addStretch()


                # Table 2-1         West Output
        self.tab2.layout_tab2_Table_V2_1 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H2.addLayout(self.tab2.layout_tab2_Table_V2_1)
                    # Add Lable
        self.lable_V2_1_lable_W = QLabel("West")
        self.tab2.layout_tab2_Table_V2_1.addWidget(self.lable_V2_1_lable_W)
        self.lable_V2_1_lable_W_s = QLabel("S : AKQJT98765432")
        self.lable_V2_1_lable_W_h = QLabel("H : ")
        self.lable_V2_1_lable_W_d = QLabel("D : ")
        self.lable_V2_1_lable_W_c = QLabel("C : ")

        self.tab2.layout_tab2_Table_V2_1.addWidget(self.lable_V2_1_lable_W_s)
        self.tab2.layout_tab2_Table_V2_1.addWidget(self.lable_V2_1_lable_W_h)
        self.tab2.layout_tab2_Table_V2_1.addWidget(self.lable_V2_1_lable_W_d)
        self.tab2.layout_tab2_Table_V2_1.addWidget(self.lable_V2_1_lable_W_c)


                # Table 2-2         Middle Checker
        self.tab2.layout_tab2_Table_V2_2 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H2.addLayout(self.tab2.layout_tab2_Table_V2_2)


                # Table 2-3         East Output
        self.tab2.layout_tab2_Table_V2_3 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H2.addLayout(self.tab2.layout_tab2_Table_V2_3)
                    # Add Lable
        self.lable_V2_3_lable_E = QLabel("West")
        self.tab2.layout_tab2_Table_V2_3.addWidget(self.lable_V2_3_lable_E)
        self.lable_V2_3_lable_E_s = QLabel("S : AKQJT98765432")
        self.lable_V2_3_lable_E_h = QLabel("H : ")
        self.lable_V2_3_lable_E_d = QLabel("D : ")
        self.lable_V2_3_lable_E_c = QLabel("C : ")

        self.tab2.layout_tab2_Table_V2_3.addWidget(self.lable_V2_3_lable_E_s)
        self.tab2.layout_tab2_Table_V2_3.addWidget(self.lable_V2_3_lable_E_h)
        self.tab2.layout_tab2_Table_V2_3.addWidget(self.lable_V2_3_lable_E_d)
        self.tab2.layout_tab2_Table_V2_3.addWidget(self.lable_V2_3_lable_E_c)


        self.tab2.layout_tab2_Table_H2.addStretch()


                # Table 3-1         South Input
        self.tab2.layout_tab2_Table_V3_1 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H3.addLayout(self.tab2.layout_tab2_Table_V3_1)
                    # Add Lable
        self.lable_V3_1_lable_S = QLabel("South")
        self.tab2.layout_tab2_Table_V3_1.addWidget(self.lable_V3_1_lable_S)
                    # Add 13 button
        self.tab2.layout_tab2_Table_V3_1_H1 = QHBoxLayout()
        self.tab2.layout_tab2_Table_V3_1.addLayout(self.tab2.layout_tab2_Table_V3_1_H1)

        button_list = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
        for i in button_list:
            button = QPushButton(i.format(i), self)
            button.setMaximumWidth(20)
            #button.clicked.connect(lambda ch, i=i: self.function(i))      # < ---
            self.tab2.layout_tab2_Table_V3_1_H1.addWidget(button)


                # Table 3-2         South Output
        self.tab2.layout_tab2_Table_V3_2 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H3.addLayout(self.tab2.layout_tab2_Table_V3_2)
                    # Add Lable
        self.lable_V3_2_lable_S = QLabel("West")
        self.tab2.layout_tab2_Table_V3_2.addWidget(self.lable_V3_2_lable_S)
        self.lable_V3_2_lable_S_s = QLabel("S : AKQJT98765432")
        self.lable_V3_2_lable_S_h = QLabel("H : ")
        self.lable_V3_2_lable_S_d = QLabel("D : ")
        self.lable_V3_2_lable_S_c = QLabel("C : ")

        self.tab2.layout_tab2_Table_V3_2.addWidget(self.lable_V3_2_lable_S_s)
        self.tab2.layout_tab2_Table_V3_2.addWidget(self.lable_V3_2_lable_S_h)
        self.tab2.layout_tab2_Table_V3_2.addWidget(self.lable_V3_2_lable_S_d)
        self.tab2.layout_tab2_Table_V3_2.addWidget(self.lable_V3_2_lable_S_c)


                # Table 3-3         West Input
        self.tab2.layout_tab2_Table_V3_3 = QVBoxLayout()
        self.tab2.layout_tab2_Table_H3.addLayout(self.tab2.layout_tab2_Table_V3_3)
                    # Add Lable
        self.lable_V3_3_lable_W = QLabel("West")
        self.tab2.layout_tab2_Table_V3_3.addWidget(self.lable_V3_3_lable_W)
                    # Add 13 button
        self.tab2.layout_tab2_Table_V3_3_H1 = QHBoxLayout()
        self.tab2.layout_tab2_Table_V3_3.addLayout(self.tab2.layout_tab2_Table_V3_3_H1)

        button_list = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
        for i in button_list:
            button = QPushButton(i.format(i), self)
            button.setMaximumWidth(20)
            #button.clicked.connect(lambda ch, i=i: self.function(i))      # < ---
            self.tab2.layout_tab2_Table_V3_3_H1.addWidget(button)


        self.tab2.layout_tab2_Table_H3.addStretch()


        # Button Right
        self.Hzero_right_lable1 = QLabel("Menu :")
        self.tab2.layout_tab2_Table_V_right.addWidget(self.Hzero_right_lable1)

        self.Hzero_right_button_1 = QPushButton("Right")
        self.tab2.layout_tab2_Table_V_right.addWidget(self.Hzero_right_button_1)

        self.tab2.layout_tab2_Table_V_right.addStretch()

        """


            # 1st Lable_Example Widget

                # Example Lable
        self.tab2_lable_example = QLabel('Example Input : N:<font color="blue">QJT5432</font>.<font color="red">T</font>.<font color="orange">6</font>.<font color="green">QJ82</font>' +
                                                ' E:<font color="blue"></font>.<font color="red">J97543</font>.<font color="orange">K7532</font>.<font color="green">94</font>' +
                                                ' S:<font color="blue">87</font>.<font color="red">A62</font>.<font color="orange">QJT4</font>.<font color="green">AT75</font>' +
                                                ' W:<font color="blue">AK96</font>.<font color="red">KQ8</font>.<font color="orange">A98</font>.<font color="green">K63</font>')
        self.tab2.layout_tab2_V_main.addWidget(self.tab2_lable_example)

            # 2st Horizon Layout
        self.tab2.layout_tab2_H = QHBoxLayout()

                # line_input_desk
        self.line_input_desk = QLineEdit()
        self.line_input_desk.setMaximumWidth(750)                   # Set Width
        self.line_input_desk.setText("N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 W:AK96.KQ8.A98.K63 S:87.A62.QJT4.AT75") # Set Default Text
        #N:Q54.A74.AJ942.Q9 E:A2.J86.T8KT843 W:K63.KQT953.Q6.A6 S:JT987.2.K753.J75
        self.line_input_desk.setStyleSheet('font-size: 14pt;')      # Set stylesheet for LineEdit
        self.line_input_desk.textChanged.connect(self.checker_card)
        #self.line_input_desk.textChanged.connect(self.upper_card)
        self.line_input_desk.textChanged.connect(self.after_input_text)
        self.tab2.layout_tab2_H.addWidget(self.line_input_desk)

                # line_input_desk_generate
        self.line_input_desk_generate = QPushButton("Generate")
        self.line_input_desk_generate.clicked.connect(self.clicked_generate)
        self.line_input_desk_generate.setAutoDefault(1)                     # Make button to click with Enter key
        self.line_input_desk_generate.setStyleSheet('font-size: 14pt;')
        self.tab2.layout_tab2_H.addWidget(self.line_input_desk_generate)

                # line_input_desk_generate_random
        self.line_input_desk_generate_random = QPushButton("Random Generate")
        self.line_input_desk_generate_random.clicked.connect(self.clicked_generate_random)
        self.line_input_desk_generate_random.setAutoDefault(1)              # Make button to click with Enter key
        self.line_input_desk_generate_random.setStyleSheet('font-size: 14pt;')
        self.tab2.layout_tab2_H.addWidget(self.line_input_desk_generate_random)

                # line_input_clear
        self.line_input_clear = QPushButton("Clear Input")
        self.line_input_clear.clicked.connect(self.clicked_input_clear)
        self.line_input_clear.setAutoDefault(1)                             # Make button to click with Enter key
        self.line_input_clear.setStyleSheet('font-size: 14pt;')
        self.tab2.layout_tab2_H.addWidget(self.line_input_clear)


            # Add 2st Horizon Layout into main Layout
        self.tab2.layout_tab2_V_main.addLayout(self.tab2.layout_tab2_H)

            # 3st text_checker
                # text_checker
        self.text_checker = QLabel("Checker Card : -")
        self.text_checker.setStyleSheet('font-size: 14pt;')
        self.tab2.layout_tab2_V_main.addWidget(self.text_checker)





        # End of Second tab

        # Add Stretch
        self.tab2.layout_tab2_V_main.addStretch()



        #########################################################################################################################################################################################
    
        # Create Third tab


        self.tab3.layout_tab3_H_main = QHBoxLayout(self)

        self.tab3.layout_tab3_V = QVBoxLayout(self)
        self.tab3.layout_tab3_H_main.addLayout(self.tab3.layout_tab3_V)


        # Create Label
        self.tab3_text1 = QLabel("Board : 1")
        self.tab3_text2 = QLabel("Dealer : N")
        self.tab3_text3 = QLabel("Vul : N-S")
        self.tab3_text4 = QLabel("Desk Code")
        self.tab3_text5 = QLabel("Sol.")

        self.tab3.layout_tab3_V.addWidget(self.tab3_text1)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text2)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text3)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text4)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text5)

        # Loading image
        make_pic_4hand({})
        self.pixmap = QPixmap('picture_resource/result.png')
        os.remove("picture_resource/result.png")

        # Creating label and adding image to label
        self.label_pic = QLabel(self)
        self.label_pic.setPixmap(self.pixmap)
        self.tab3.layout_tab3_H_main.addWidget(self.label_pic)

        


        





        # End of Third tab
        self.tab3.layout_tab3_V.addStretch()
        self.tab3.setLayout(self.tab3.layout_tab3_H_main)


    
        #########################################################################################################################################################################################
    
        # Create Third tab

        # Create Label

        # Create Layout and Add label


        # End of Third tab
        #self.tab2.layout_tab2_V.addStretch()
        #self.tab2.setLayout(self.tab2.layout_tab_V)








    @pyqtSlot()
    def clicked_generate(self):

        # Check if Desk code is valid

        if ( text_to_pbn_check(self.line_input_desk.text()) == False):
            """
            If pbn is Invaild
            """
            # Error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            #msg.setText("Error")
            #msg.setInformativeText('More information')
            msg.setInformativeText('Desk is Invalid')
            msg.setWindowTitle("Error")
            msg.exec_()

            return # Exit function

        else:
            """
            Else (If pbn is vaild)
            -> Check lost_card ,over_card == []
            """
            list_desk = self.line_input_desk.text()
            list_desk = text_to_list_desk(list_desk)
            lost_card ,over_card = deck_list_result(list_desk)          # get checker result

            if ((lost_card == []) == False) or ((over_card == []) == False):
                # Error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error : Desk is not complete")
                #msg.setInformativeText('More information')
                msg.setWindowTitle("Error")
                msg.exec_()

                return # Exit function




        
        # Switch to Tab 3
        self.tabs.setCurrentIndex(2)

        # Set text in Tab 2
        self.tab3_text4.setText(self.line_input_desk.text())
        
        # to PBN
        text_PBN = self.line_input_desk.text()      # get text
        #print(self.line_input_desk.toPlainText()) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! get text from qtextedit

        text_PBN = text_to_pbn(text_PBN)            # set text to right position

        text_PBN_encode = text_PBN.encode()
        
        all = ddstable_standalone.get_ddstable(text_PBN_encode)
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
        self.tab3_text5.setText(all_2)


        # Create image
        input_text = self.line_input_desk.text()
        input_text = pbn_to_dict(input_text)
        make_pic_4hand(input_text)                  # Create image of 4 hand desk

        # Loading image
        self.pixmap = QPixmap('picture_resource/result.png')
        self.label_pic.setPixmap(self.pixmap)
        os.remove("picture_resource/result.png")

    def clicked_generate_random(self):
        # Signal to change text in line_input_desk to random card
        random_desk = random_card()                         # get random card
        self.line_input_desk.setText(random_desk)           # set text to display

    def clicked_input_clear(self):
        # Signal to clear text in line_input_desk
        self.line_input_desk.setText("N:... E:... S:... W:...")
    
    def checker_card(self):
        # Signal to Display Checker Lost card and Over card on 
        dict_desk = pbn_to_dict(self.line_input_desk.text())        # get text and change to dict type
        list_desk = dict_to_desk(dict_desk)                         # change dict type to list of desk

        lost_card ,over_card = deck_list_result(list_desk)          # get checker result
        
        # Display result on text_checker
        self.text_checker.setText(  "Checker Card : "                           + "\n" +
                                    "Lost_card \t" + str(lost_card)             + "\n" +
                                    "Over_card \t" + str(over_card)
        )
    
    def after_input_text(self):
        # Signal to change text in line_input_desk 
        self.upper_card()            # to change text to upper character
        #self.remove_input_text()     # to check input
        
        

    def remove_input_text(self):
        # Signal to change text in line_input_desk to right text "AKQJT98765432 NEWS :"
        line = self.line_input_desk.text()                    # get text and change to upper character

        value = line
        whitelist = set('AKQJT998765432NEWS: .')

        output = ''.join([c for c in value if c in whitelist])


        cursorPos = self.line_input_desk.cursorPosition()     # get cursorPosition of line_input_desk
        
        self.line_input_desk.setText(output)                  # set text as upper text
        self.line_input_desk.setCursorPosition(cursorPos)     # set cursorPosition same as before

    def upper_card(self):
        # Signal to change text in line_input_desk to upper character

        line = self.line_input_desk.text().upper()          # get text and change to upper character
        cursorPos = self.line_input_desk.cursorPosition()   # get cursorPosition of line_input_desk
        
        self.line_input_desk.setText(line)                  # set text as upper text
        self.line_input_desk.setCursorPosition(cursorPos)   # set cursorPosition same as before
        

    def exit():
        # Exit function to Close progream
        sys.exit( app.exec_() )


    
















        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QLabel{font-size: 14pt;}")              # Set Default Font

    main_windows = BridgeWindow()
    main_windows.show()


    sys.exit( app.exec_() )


    