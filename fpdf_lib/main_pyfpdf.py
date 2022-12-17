from fpdf import FPDF

try:
    from bridge import get_dealer ,get_vul
except:
    from fpdf_lib.bridge import get_dealer ,get_vul



#Add Text To Images With Pillow - Python Tkinter GUI Tutorial 203
#https://www.youtube.com/watch?v=bmzDUQRPEdE

#   Ref.
#   https://github.com/reingart/pyfpdf/blob/master/docs/ReferenceManual.md



class PDF(FPDF):
    def header(self):
        # Times bold 20
        self.set_font('Times', 'B', 20)
        # Headline
        self.set_line_width( 0.1 )
        self.line(1 , 0.5, 209, 0.5)
        self.line(1 , 1, 209, 1)
        self.line(1 , 9.5, 209, 9.5)
        # Calculate width of title and position
        w = self.get_string_width(title_pdf) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_fill_color(255, 255, 255)
        self.set_text_color( 4, 5, 211)
        # Title
        self.cell(w, 7, title_pdf, 0, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 0.7 cm from bottom
        self.set_y(-7)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        #self.set_text_color(128)
        # Text color in blue
        self.set_text_color( 4, 5, 211)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    # Main function to make pdf

    def print_board(self, Board_num, dealer, vul, desk):
        if ( (Board_num % 12) == 1):
            self.add_page()
            
        self.draw_box(Board_num)
        self.board_information(Board_num, dealer, vul)
        pass

        
        # Working on it
        self.draw_dds(Board_num ,desk)    

        #self.draw_card(Board_num)
        #self.draw_hcp(Board_num)
        #self.draw_gametype(Board_num)


    # Sub function to make pdf

    def draw_dds(self ,position ,desk):
        # Set Position
        x_start , y_start = self.start_point_from_position(position)

        # Draw Gray Background
            # Set color of box
        self.set_draw_color(231 ,231 ,231)  # Set to Gray
        self.set_fill_color(231 ,231 ,231)  # Set to Gray

        y_long = 30 # mm , height of box
        x_long = 30 # mm , wide of box

        self.rect(x_start + 1, y_start + 20, x_long, y_long, style = 'DF')

        # Draw Text
            # Set text
        self.set_font('Times', '', 12)
        self.set_text_color( 4, 5, 211)






        #self.set_xy(x_start + 1, y_start + 20)

        #line_1 = "Test " + str(position)

        #self.cell(w = 10, h = 0, txt = line_1)



        
        
    def draw_box(self ,position):
        # position in range 1 to 12
        y_long = 47  # mm , height of box
        x_long = 104 # mm , wide of box

        # y_header = 10 # mm point from header
        # x_header = 0  # mm point from header

        # Set color of box
        self.set_draw_color(0 ,0 ,0)  # to Black


        x_start , y_start = self.start_point_from_position(position)

        self.rect(x_start, y_start, x_long, y_long, style = '')


    def board_information(self ,position ,dealer ,vul):
        # Set text
        self.set_font('Times', '', 12)
        self.set_text_color( 4, 5, 211)     # Text color is Blue.

        # Set Position
        # Line 1
        x_start , y_start = self.start_point_from_position(position)
        self.set_xy(x_start + 1, y_start + 4)

        line_1 = "Board: " + str(position)

        self.cell(w = 10, h = 0, txt = line_1)

        # Line 2
        x_start , y_start = self.start_point_from_position(position)
        self.set_xy(x_start + 1, y_start + 8)

        line_2 = "Dealer: " + dealer

        self.cell(w = 10, h = 0, txt = line_2)
        
        # Line 3

        x_start , y_start = self.start_point_from_position(position)
        self.set_xy(x_start + 1, y_start + 12)

        line_3 = "Vul: " + vul

        self.cell(w = 10, h = 0, txt = line_3)




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


# Info
title_pdf = 'Open Pairs - Mon.5.10.20'
#title_pdf = 'Bridge System - PDF'
author = 'Project-Bridge-system'
output_filename = title_pdf + ".pdf"


# Setting to pdf
pdf = PDF()

#pdf.set_title('Open Pairs - Mon.5.10.20')
#pdf.set_author('Project-Bridge-system')
pdf.set_margins(0.1 , 1.5, -0.1)
#pdf.set_header("kujhgvb")

desk = [['N:A842.QT3.K8.J652 E:75.AJ6542.92.KQ4 W:KT3.97.AQT64.T87 S:QJ96.K8.J753.A93', 'Part score']
      , ['N:J72.QT.JT4.T9843 E:Q983.J872.A7.AK7 W:6.9643.Q98.QJ652 S:AKT54.AK5.K6532.', 'Grand Slam']]


for Board_num in range(1,200):
    pdf.print_board(Board_num, get_dealer(Board_num) ,get_vul(Board_num) ,desk)



#pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
#pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
# to
#pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
#pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')

output_filename = 'Open Pairs - Mon.5.10.20' + ".pdf"
pdf.output(output_filename, 'F')    # save to a local file




# docs
# https://github.com/reingart/pyfpdf/tree/master/docs