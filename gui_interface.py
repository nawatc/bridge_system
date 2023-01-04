import sys ,os
from PyQt5 import QtWidgets ,QtGui ,QtCore 
from PyQt5.QtWidgets import QMainWindow ,QLabel ,QWidget ,QVBoxLayout \
    ,QPushButton ,QTabWidget ,QLineEdit ,QHBoxLayout ,QMessageBox ,QTextEdit \
    ,QTableWidget ,QTableView ,QShortcut ,QCheckBox ,QTableWidgetItem \
    ,QSizePolicy ,QComboBox ,QFileDialog #,QSizePolicy  ,QGridLayout 
from PyQt5.QtCore    import pyqtSlot ,QSize
from PyQt5.QtGui     import QKeySequence ,QPixmap #,QColor 


import ddstable_standalone as ddstable_standalone


from picture_program import make_pic_4hand

from sqlite3_lib import Database

from main_pyfpdf import PDF
from fpdf_lib.bridge import get_dealer ,get_vul

from porter_bridges.random_number import random_card ,get_num_from_txt ,set_num_from_txt ,cycle_one_step ,random_card_with_prng

from porter_bridges.porter_bridges import pbn_to_dict ,text_to_pbn_check ,text_to_pbn ,dict_to_desk ,deck_list_result  ,text_to_list_desk
#from porter_bridges.board_info import get_dealer_from_board_number ,get_vul_from_board_number

from time import gmtime, strftime


    
class BridgeWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        width , height = 1820,600
        
        self.setMinimumSize(QSize(width, height))      # Set Windows Size
        #self.setFixedSize(width, height)                # Set Windows Size That cannot resize
        self.setWindowTitle("Bridge system") 
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.table_widget = MyTabsWidget(self)
        self.setCentralWidget(self.table_widget)
        
        

class MyTabsWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet('font-size: 14pt;')
        #self.tabs.resize(300,200)

        self.choose_data = []

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
        #self.tabs.addTab(self.tab5,"Export as PDF")
        
        self.tabs.setCurrentIndex(0)    # Go to tab 4

        # Add Tab to Main Windows
        self.layout_tab = QVBoxLayout(self)
        self.layout_tab.addWidget(self.tabs)

        #############################################################################################################################################################################

        # Add Shortcut key

        # Ctrl + W to Exit
        #self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        #self.shortcut.activated.connect(self.exit)

        #############################################################################################################################################################################

        # Create First tab
        
        # Create Main Layout and Add label
        self.tab1.layout_tab1_V_main = QVBoxLayout()
        self.tab1.setLayout(self.tab1.layout_tab1_V_main)


            # 1st Horizon Layout
        self.tab1.layout_tab1_H1 = QHBoxLayout()

                # Autogen Lable
        self.line_autogen = QLabel("Auto generate new Desk number : ")
        self.tab1.layout_tab1_H1.addWidget(self.line_autogen)

                # Autogen Line Edit
        self.line_edit_autogen = QLineEdit()
        self.line_edit_autogen.setText("0") # Set Default Text
        self.line_edit_autogen.setStyleSheet('font-size: 14pt;')
        self.line_edit_autogen.setFixedWidth(100)
        #self.line_edit_autogen.setMaximumWidth(100)                   # Set Width
        self.tab1.layout_tab1_H1.addWidget(self.line_edit_autogen)

                # Autogen Button
        self.button_autogen = QPushButton("Generate Desk")
        self.button_autogen.setAutoDefault(1)                             # Make button to click with Enter key
        self.button_autogen.setStyleSheet('font-size: 14pt;')
        self.button_autogen.clicked.connect(self.autogen_num)
        self.tab1.layout_tab1_H1.addWidget(self.button_autogen)

                # Add 1st Horizon Layout into main Layout
        self.tab1.layout_tab1_V_main.addLayout(self.tab1.layout_tab1_H1)


            # 2nd Lable
        B_DB = Database()
        row_num = B_DB.get_row_number()
        row_num_percent = row_num / 53644737765488792839237440000
        row_num_percent = f'{row_num_percent:.26f}'
        
        self.line_total = QLabel("Total Record : \t" + str(row_num) + " / " + "53644737765488792839237440000")
        self.tab1.layout_tab1_V_main.addWidget(self.line_total)

        self.line_total_percent = QLabel("\t\t" + str(row_num_percent) + "%")
        self.tab1.layout_tab1_V_main.addWidget(self.line_total_percent)

        self.tab1.layout_tab1_H1.addStretch()




        


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
            # https://stackoverflow.com/questions/57137027/conect-multiple-buttons-to-same-function-with-different-parameters

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
        #self.line_input_desk.setMaximumWidth(750)                   # Set Width
        self.line_input_desk.setMinimumWidth(730)               # Set Width
        #self.line_input_desk.setText("N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 W:AK96.KQ8.A98.K63 S:87.A62.QJT4.AT75") # Set Default Text
        self.clicked_generate_random()  # Random card as start
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

        self.tab2.layout_tab2_H.addStretch()
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

        # V_main Layout
        self.tab3.layout_tab3_V_main = QVBoxLayout(self)
        self.tab3.setLayout(self.tab3.layout_tab3_V_main)

            # 1st H Sub Layout of # V_Main
        self.tab3.layout_tab3_H_1 = QHBoxLayout(self)
        self.tab3.layout_tab3_V_main.addLayout(self.tab3.layout_tab3_H_1)

            # 2nd H Sub Layout of # V_Main
        self.tab3.layout_tab3_H_2 = QHBoxLayout(self)
        self.tab3.layout_tab3_V_main.addLayout(self.tab3.layout_tab3_H_2)

                # 1st V of # 2nd H Sub Layout of # V_Main
        self.tab3.layout_tab3_V = QVBoxLayout(self)
        self.tab3.layout_tab3_H_2.addLayout(self.tab3.layout_tab3_V)


        # Create Button to # 1nd H Sub Layout of # V_Main
            # Create Button
        self.tab3_button_H_1_1 = QPushButton("  <<<  ")
        self.tab3_button_H_1_2 = QPushButton("  >>>  ")

            # Disable Button
        self.tab3_button_H_1_1.setEnabled(False)
        self.tab3_button_H_1_2.setEnabled(False)

            # Add Button to Layout
        self.tab3.layout_tab3_H_1.addWidget(self.tab3_button_H_1_1, alignment=QtCore.Qt.AlignLeft)
        self.tab3.layout_tab3_H_1.addWidget(self.tab3_button_H_1_2, alignment=QtCore.Qt.AlignRight)



        # Create Label to # 2nd H Sub Layout of # V_Main
            # Create Lable
            # Default Value
        self.tab3_text1 = QLabel("Board  : -")
        self.tab3_text2 = QLabel("Dealer : -")
        self.tab3_text3 = QLabel("Vul : -")
        self.tab3_text4 = QLabel("Desk Code :")
        self.tab3_text5 = QTextEdit("Solution : ")

            # Example Value
        """
        self.tab3_text1 = QLabel("Board : 1")
        self.tab3_text2 = QLabel("Dealer : N")
        self.tab3_text3 = QLabel("Vul : N-S")
        self.tab3_text4 = QLabel("Desk Code")
        """
            # Add Lable to Layout
        self.tab3.layout_tab3_V.addWidget(self.tab3_text1)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text2)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text3)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text4)
        self.tab3.layout_tab3_V.addWidget(self.tab3_text5)

            # Loading image to Program
        make_pic_4hand({})                                      # Create image /w No Card # and Save file
        self.pixmap = QPixmap('picture_resource/result.png')    # Loading image file to Program
        os.remove("picture_resource/result.png")                # Delete image file

            # Creating label and adding image to label
        self.label_pic = QLabel(self)
        self.label_pic.setPixmap(self.pixmap)
        self.tab3.layout_tab3_H_2.addWidget(self.label_pic)     # 2st V of # 2nd H Sub Layout of # V_Main

        


        





        # End of Third tab
        self.tab3.layout_tab3_V.addStretch()


    
        #########################################################################################################################################################################################
    
        # Create Forth tab
        self.tab4.layout_tab4_V_main = QVBoxLayout(self)
        self.tab4.setLayout(self.tab4.layout_tab4_V_main)


        # Add H1 Layout 
        self.tab4.layout_tab4_H1 = QHBoxLayout(self)
        self.tab4.layout_tab4_V_main.addLayout(self.tab4.layout_tab4_H1)


        self.sort_by_label = QLabel("Sort By :")
        self.tab4.layout_tab4_H1.addWidget(self.sort_by_label)

        self.combo_box_sort_by = QComboBox()
        self.combo_box_sort_by.setStyleSheet('font-size: 14pt;')
        self.combo_box_sort_by.addItems(["Random","Part score to Grand Slam", "Grand Slam to Part score"])
        self.tab4.layout_tab4_H1.addWidget(self.combo_box_sort_by)

        self.show_only = QLabel("Show : ")
        self.tab4.layout_tab4_H1.addWidget(self.show_only)

        self.part_score = QCheckBox("Part score")
        self.part_score.setChecked(True)
        self.tab4.layout_tab4_H1.addWidget(self.part_score)
        self.game_part  = QCheckBox("Game part")
        self.game_part.setChecked(True)
        self.tab4.layout_tab4_H1.addWidget(self.game_part)
        self.small_slam = QCheckBox("Small Slam")
        self.small_slam.setChecked(True)
        self.tab4.layout_tab4_H1.addWidget(self.small_slam)
        self.grand_slam = QCheckBox("Grand Slam")
        self.grand_slam.setChecked(True)
        self.tab4.layout_tab4_H1.addWidget(self.grand_slam)


        self.number_desk_label = QLabel("Number Desk : ")
        self.tab4.layout_tab4_H1.addWidget(self.number_desk_label)

        #self.combo_box_num_desk = QComboBox()
        #self.combo_box_num_desk.setStyleSheet('font-size: 14pt;')
        #self.combo_box_num_desk.addItems(["20","50","100","200"])
        #self.tab4.layout_tab4_H1.addWidget(self.combo_box_num_desk)

        self.lineedit_num_desk = QLineEdit()
        self.lineedit_num_desk.setStyleSheet('font-size: 14pt;')
        self.lineedit_num_desk.setText("20")
        self.tab4.layout_tab4_H1.addWidget(self.lineedit_num_desk)

        self.random_table_button = QPushButton("Random")
        self.random_table_button.setStyleSheet('font-size: 14pt;')
        self.random_table_button.clicked.connect(self.clicked_random_plot_table)
        self.tab4.layout_tab4_H1.addWidget(self.random_table_button)

        self.display_from_table_button = QPushButton("Display Board")
        self.display_from_table_button.setStyleSheet('font-size: 14pt;')
        self.display_from_table_button.clicked.connect(self.clicked_display_board_table)
        self.tab4.layout_tab4_H1.addWidget(self.display_from_table_button)

        self.clear_choose_table_button = QPushButton("Clear Table")
        self.clear_choose_table_button.setStyleSheet('font-size: 14pt;')
        self.clear_choose_table_button.clicked.connect(self.clicked_clear_choose_table)
        self.tab4.layout_tab4_H1.addWidget(self.clear_choose_table_button)

        self.blank_lable = QLabel(" ")
        self.blank_lable.setStyleSheet('font-size: 14pt;')
        self.tab4.layout_tab4_H1.addWidget(self.blank_lable)

        #self.export_pdf_button = QPushButton("Export Table as PDF")
        #self.export_pdf_button.setStyleSheet('font-size: 14pt;')
        #self.export_pdf_button.clicked.connect(self.clicked_export_pdf)
        #self.tab4.layout_tab4_H1.addWidget(self.export_pdf_button)



        self.tab4.layout_tab4_H1.addStretch()
        # self.export_pdf_button (13th item) will be right side of layout
        self.tab4.layout_tab4_H1.setStretch(12, 4)






        # Add H2 Layout 
        self.tab4.layout_tab4_H2 = QHBoxLayout(self)
        self.tab4.layout_tab4_V_main.addLayout(self.tab4.layout_tab4_H2)

        # Create TableWidget
        self.TableWidget = QTableWidget(self)
        self.tab4.layout_tab4_H2.addWidget(self.TableWidget)



        # Add tab4_V_in_H2 Layout
        self.tab4.layout_tab4_V_in_H2 = QVBoxLayout(self)
        self.tab4.layout_tab4_H2.addLayout(self.tab4.layout_tab4_V_in_H2)

        # Add Choose Button
        self.choose_button = QPushButton(" >> ")
        self.choose_button.setStyleSheet('font-size: 14pt;')
        self.choose_button.clicked.connect(self.clicked_add_from_table)
        self.tab4.layout_tab4_V_in_H2.addWidget(self.choose_button)

        # Add Choose Del Button
        self.choose_del_button = QPushButton(" << ")
        self.choose_del_button.setStyleSheet('font-size: 14pt;')
        self.choose_del_button.clicked.connect(self.clicked_del_from_table)
        self.tab4.layout_tab4_V_in_H2.addWidget(self.choose_del_button)



        # Add Table Choose
        self.TableWidget_choose = QTableWidget(self)
        self.tab4.layout_tab4_H2.addWidget(self.TableWidget_choose)


        # Set Table
            # Set Column
        Column_header = ["Desk Code","Game type"]
        self.TableWidget.setColumnCount(len(Column_header))
        self.TableWidget.setHorizontalHeaderLabels(Column_header)
        self.TableWidget.setColumnWidth(0,680)
        self.TableWidget.setColumnWidth(1,120)

        self.TableWidget_choose.setColumnCount(len(Column_header))
        self.TableWidget_choose.setHorizontalHeaderLabels(Column_header)
        self.TableWidget_choose.setColumnWidth(0,680)
        self.TableWidget_choose.setColumnWidth(1,120)

        
        
        self.plot_table(get_only = ["Part score","Game part","Small Slam","Grand Slam"] ,sort_type = "Random" ,limit = 20 )











        # Create Layout and Add label


        # End of Third tab
        #self.tab2.layout_tab2_V.addStretch()
        #self.tab2.setLayout(self.tab2.layout_tab_V)

        #########################################################################################################################################################################################
    
        # Create Fifth tab

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

        # calulate_and_keep_DB
        self.pbn_calulate_and_keep_DB(self.line_input_desk.text())
    
        
        # Switch to Tab 3
        self.tabs.setCurrentIndex(2)

        # Set text in Tab 2
        self.tab3_text4.setText(self.line_input_desk.text())

        

        self.Display_board(self.line_input_desk.text())
        
    def Display_board(self ,pbn_desk):
        
        text_PBN = pbn_desk
        # to PBN
        #text_PBN = self.line_input_desk.text()      # get text
        #print(self.line_input_desk.toPlainText()) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! get text from qtextedit

        text_PBN = text_to_pbn(text_PBN)            # set text to right position
        #print(text_PBN)
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
        #self.tab3_text5.setText(    text_PBN +
        #                            "\n\n" + all_2)
        self.tab3_text5.setText(    text_PBN +
                                    "\n\n" + all_2)
        
        # Create image
        input_text = text_PBN
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

        #self.pbn_calulate_and_keep_DB(random_desk)

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


    def autogen_num(self):
        # Signal to generate desk ,info and keep it into database

        filename_seed           = "seed"       #filename to collect seed
        filename_original_seed  = "org_seed"   #filename to collect original_seed

        org_seed = int(get_num_from_txt(filename_original_seed))    # original seed
        seed     = int(get_num_from_txt(filename_seed))        # seed

        

            # Get number
        random_time = self.line_edit_autogen.text()
        
        if not(random_time.isdigit()):
            # Check it's integer if not exit
            return
        
        # Check it's integer if it is continue
        random_time = int(self.line_edit_autogen.text())
        #self.line_edit_autogen.setText("0")                # Set Text to 0
        
        # Loop as random_time
        for i in range(0 ,random_time):
            # Process to Generate info
            #print(i) # i is    0 to n-1
                # Get new desk from number
            seed = int(get_num_from_txt(filename_seed))        # get seed

            if seed == org_seed :
                # if seed = ori_seed than full cycle is complete
                print("Full Cycle had Complete")
        
                # Get PBN from seed
            #N:KQJT2.986.Q8.T97 E:765.AKQ.A76.K853 W:983.T75.K932.AJ2 S:A4.J432.JT54.Q64
            pbn_desk = random_card_with_prng(seed)
            
            #print(pbn_desk)
            self.pbn_calulate_and_keep_DB(pbn_desk)





            # set seed to next seed
            set_num_from_txt(filename_seed ,cycle_one_step(seed = seed, sample_size = 53644737765488792839237440000, increment = 31114111519121615131518191719))
            

    def pbn_calulate_and_keep_DB(self ,pbn_desk):
        
            
        # Get Bo
        pbn_desk_encode = pbn_desk.encode()
        #{'N': {'S': 5, 'H': 5, 'D': 4, 'C': 4, 'NT': 4}, 'S': {'S': 5, 'H': 5, 'D': 4, 'C': 4, 'NT': 4}, 'E': {'S': 8, 'H': 8, 'D': 8, 'C': 9, 'NT': 8}, 'W': {'S': 8, 'H': 8, 'D': 8, 'C': 9, 'NT': 8}}
        dds = ddstable_standalone.get_ddstable(pbn_desk_encode)
            
            # Get Max Scoring deals
        max_score_deals = ""
        score_deals     = []
        #score_deals     = ["part score","game part","small slam","grand slam"]
        #score_deals     = [           1,          4,           6,           7]
        #score_deals_lv  = [           7,         10,          12,          13]
        #score_deals_suit= ["s","h","d","c"]
            
        for i in ['N','E','W','S']:
            for j in ['S','H','D','C','NT']:
                if dds[i][j] == 13:
                    score_deals.append("Grand Slam")
                elif dds[i][j] == 12:
                    score_deals.append("Small Slam")
                elif dds[i][j] >= 11 and (j == 'D' or j == 'C'):
                    score_deals.append("Game part")
                elif dds[i][j] >= 10 and (j == 'S' or j == 'H'):
                    score_deals.append("Game part")
                elif dds[i][j] >=  9 and (j == 'NT'):
                    score_deals.append("Game part")
                elif dds[i][j] >=  7:
                    score_deals.append("Part score")
                else:
                    score_deals.append("Below score")
            
        if "Grand Slam" in score_deals:
            max_score_deals = "Grand Slam"
        elif "Small Slam" in score_deals:
            max_score_deals = "Small Slam"
        elif "Game part" in score_deals:
            max_score_deals = "Game part"
        elif "Part score" in score_deals:
            max_score_deals = "Part score"
        elif "Below score" in score_deals:
            max_score_deals = "Below score"
        else:
            max_score_deals = ""
            
            
            # Data

        # pbn_desk  # Desk Info
        #N:KQJT2.986.Q8.T97 E:765.AKQ.A76.K853 W:983.T75.K932.AJ2 S:A4.J432.JT54.Q64
        # dds       # DDS (Bo algorithm)
        #{'N': {'S': 5, 'H': 5, 'D': 4, 'C': 4, 'NT': 4}, 'S': {'S': 5, 'H': 5, 'D': 4, 'C': 4, 'NT': 4}, 'E': {'S': 8, 'H': 8, 'D': 8, 'C': 9, 'NT': 8}, 'W': {'S': 8, 'H': 8, 'D': 8, 'C': 9, 'NT': 8}}
        # max_score_deals # max_score_deals of board
        # "" <- "part score" "game part" "small slam" "grand slam"


            
        # Process to put into database
        B_DB = Database()       # Database Class

        if B_DB.check_if_row_exist(pbn_desk):
            # Check if this desk already into database
            pass

        else:
            # Check if this desk is new to database
            B_DB.add_board(pbn_desk, max_score_deals)


        #B_DB.print_select_board()

        # Set Total Record in Tab 1
        #B_DB = Database()
        row_num = B_DB.get_row_number()
        row_num_percent = row_num / 53644737765488792839237440000
        row_num_percent = f'{row_num_percent:.26f}'

        self.line_total.setText("Total Record : \t" + str(row_num) + " / " + "53644737765488792839237440000")
        self.line_total_percent.setText("\t\t" + str(row_num_percent) + "%")


    def get_database_as_list(self ,get_only = ["Part score","Game part","Small Slam","Grand Slam"] ,sort_type = "Random" ,limit = 10 ):
        # Get desk code and gametype from database
        B_DB = Database()
        
        # Example Input
        # get_only = ["Part score","Game part","Small Slam","Grand Slam"]
        # sort = "Random" , "Grand Slam to Part score" ,"Part score to Grand Slam"
        # limit = 10
        #
        #print(B_DB.get_select_board(get_only = ["Part score","Game part","Small Slam","Grand Slam"] ,sort_type = "Random" ,limit = 10))

        #output_list = []

        return B_DB.get_select_board(get_only = get_only ,sort_type = sort_type ,limit = limit)


    def plot_table(self ,get_only = ["Part score","Game part","Small Slam","Grand Slam"] ,sort_type = "Random" ,limit = 20 ):
        
        # Example Input
        # get_only = ["Part score","Game part","Small Slam","Grand Slam"]
        # sort = "Random" , "Grand Slam to Part score" ,"Part score to Grand Slam"
        # limit = 10
        #self.get_database_as_list(self ,get_only = [] ,sort_type = "Random" ,limit = 10 )

        #a = [["N:Q54.A74.AJ942.Q9 E:A2.J86.T8KT843 W:K63.KQT953.Q6.A6 S:JT987.2.K753.J75","Grand Slam"],["N:Q54.A74.AJ942.Q9 E:A2.J86.T8KT843 W:K63.KQT953.Q6.A6 S:JT987.2.K753.J75","Grand Slam"]]
        a = self.get_database_as_list(get_only ,sort_type ,limit)
        #print(self.get_database_as_list(get_only = [] ,sort_type = "Random" ,limit = 10 ))
        for row_data in a:
            # insert new row at the end of the tableWidget
            row_number = self.TableWidget.rowCount()
            self.TableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.TableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))


    def clicked_random_plot_table(self):
        # Plot table

        self.TableWidget.setRowCount(0)     # Clear Table
        get_only = []
        if self.part_score.isChecked():
            get_only.append("Part score")
        if self.game_part.isChecked():
            get_only.append("Game part")
        if self.small_slam.isChecked():
            get_only.append("Small Slam")
        if self.grand_slam.isChecked():
            get_only.append("Grand Slam")

        #num_desk = int(self.combo_box_num_desk.currentText())
        if self.lineedit_num_desk.text().isdigit():
            num_desk = int(self.lineedit_num_desk.text())
        else:
            num_desk = 0

        if num_desk > 9999:
            num_desk = 9999

        self.plot_table(get_only = get_only ,sort_type = self.combo_box_sort_by.currentText() ,limit = num_desk )


    def clicked_display_board_table(self):
        self.tabs.setCurrentIndex(2)    # Go to tab 3
        
        #pbn_desk = self.get_selected_cell_value()
        if self.get_selected_cell_value_table_choose() == -1:
            # if can't get data from choose table
            # get from left table instand
            pbn_desk = self.get_selected_cell_value()
        else:
            pbn_desk = self.get_selected_cell_value_table_choose()

        #print(pbn_desk)
        self.Display_board(pbn_desk)

    def get_selected_cell_value(self):
        current_row     = self.TableWidget.currentRow()
        current_column  = 0
        #print(current_row)
        if current_row == -1:
            current_row = 0
        #current_column  = self.TableWidget.currentColumn()
        cell_value = self.TableWidget.item(current_row, current_column).text()
        #print(cell_value)
        return cell_value
    
    def get_selected_cell_value_gametype(self):
        current_row     = self.TableWidget.currentRow()
        current_column  = 1
        #print(current_row)
        if current_row == -1:
            current_row = 0
        #current_column  = self.TableWidget.currentColumn()
        cell_value = self.TableWidget.item(current_row, current_column).text()
        #print(cell_value)
        return cell_value

    def get_selected_cell_value_table_choose(self):
        current_row     = self.TableWidget_choose.currentRow()
        current_column  = 0
        #print(current_row)
        if current_row == -1:
            return -1
        #current_column  = self.TableWidget_choose.currentColumn()
        cell_value = self.TableWidget_choose.item(current_row, current_column).text()
        #print(cell_value)
        return cell_value
    
    def get_selected_cell_value_table_choose_gametype(self):
        current_row     = self.TableWidget_choose.currentRow()
        current_column  = 1
        #print(current_row)
        if current_row == -1:
            current_row = 0
        #current_column  = self.TableWidget_choose.currentColumn()
        cell_value = self.TableWidget_choose.item(current_row, current_column).text()
        #print(cell_value)
        return cell_value

    def clicked_add_from_table(self):
        
        # Get Data
        add_row = [self.get_selected_cell_value(),self.get_selected_cell_value_gametype()]
        # Collect Data
        self.choose_data.append(add_row)
        
        
        # plot latest data on choose table
        self.clear_and_plot_choose_table()


    def clicked_del_from_table(self):

        if self.choose_data == []:
            # If choose data is empty ,don't do anything
            pass
        
        else :
            # Get Current row
            # if current_row == -1 # return as no choose row
            # dont del anything
            current_row = self.TableWidget_choose.currentRow()

            
            if current_row == -1:
                #if not choose row
                #del last row

                current_row = -1
                #return

            
            # Del Row Data
            self.choose_data.pop(current_row)

            # plot latest data on choose table
            self.clear_and_plot_choose_table()

            
    def clicked_clear_choose_table(self):
        

        # Set data as empty
        self.choose_data = []

        # Plot latest data on choose table
        self.clear_and_plot_choose_table()
        

    def clear_and_plot_choose_table(self):
        # Clear Table
        self.TableWidget_choose.setRowCount(0)

        # Plot on Choose Table
        for row_data in self.choose_data:
            # insert new row at the end of the tableWidget
            row_number = self.TableWidget_choose.rowCount()
            self.TableWidget_choose.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.TableWidget_choose.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))


    def clicked_export_pdf(self):
        # Export self.choose_data as PDF

        # Get Desk Choose to print
        #[  ['N:T83.J943.753.Q85 E:J64.T62.AK62.732 W:Q975.KQ875.J8.A6 S:AK2.A.QT94.KJT94', 'Game part']
        # , ['N:T9542.K4.JT3.J52 E:A.AQ2.865.KQ9764 W:Q76.J9863.AQ9.A8 S:KJ83.T75.K742.T3', 'Game part']
        # , ['N:42.A942.K98653.8 E:QJT.KT85.A7.AKJ7 W:AK975.J6.J2.Q952 S:863.Q73.QT4.T643', 'Part score']
        # , ['N:T83.J943.753.Q85 E:J64.T62.AK62.732 W:Q975.KQ875.J8.A6 S:AK2.A.QT94.KJT94', 'Game part']
        # , ['N:AK72.76.KT32.T97 E:T54.K432.J965.86 W:QJ86.QJT9.A8.QJ5 S:93.A85.Q74.AK432', 'Part score']]
        #print(self.choose_data)
        desk = self.choose_data

        # Get Time
        current_time = strftime("%a_%d.%b.%Y_%H.%M.%S", gmtime())
        
        # Get Save file location
        filename = QFileDialog.getSaveFileName(self, "Save file", "Bridge_Sport_"+current_time, ".pdf")
        #print(filename)

        Fname = filename[0].split('/')[-1]
        #print(Fname)
        #Lname = filename[1]
        #print(Lname)
        fullpath = filename[0]
        #print(fullpath)
        



        # Set Info
        #title = 'Open Pairs - Mon.5.10.20'
        title = Fname
        author = 'Project-Bridge-system'
        #output_filename = title + ".pdf"
        output_filename = fullpath + ".pdf"

        pdf = PDF()
        pdf.set_title(title)
        pdf.set_author(author)
        pdf.set_margins(0.1 , 1.5, -0.1)

        # Print Info to PDF
        for Board_num in range(1 ,len(desk) + 1):
            pdf.print_board(Board_num, get_dealer(Board_num) ,get_vul(Board_num) ,desk)
        
        
        


        # Working ! ! ! 

        
        pdf.output(output_filename, 'F')    # save to a local file




        
    def exit():
        # Exit function to Close progream
        sys.exit( app.exec_() )


    
















        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QLabel {font-size: 14pt;}")              # Set Default Font

    main_windows = BridgeWindow()
    main_windows.show()


    sys.exit( app.exec_() )


    