from fpdf import FPDF
from bridge import get_dealer ,get_vul



#Add Text To Images With Pillow - Python Tkinter GUI Tutorial 203
#https://www.youtube.com/watch?v=bmzDUQRPEdE

title = 'Open Pairs - Mon.5.10.20'
author = 'Project-Bridge-system'
output_filename = title + ".pdf"


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
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_fill_color(255, 255, 255)
        self.set_text_color( 4, 5, 211)
        # Title
        self.cell(w, 7, title, 0, 1, 'C', 1)
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


    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)


    def print_board(self, Board_num, dealer, vul):
        if ( (Board_num % 12) == 1):
            self.add_page()
            
        self.draw_box(Board_num)
        self.board_information(Board_num, dealer, vul)
        pass

    
    def board_information(self ,position ,dealer ,vul):
        # Set text
        self.set_font('Times', '', 12)
        self.set_text_color( 4, 5, 211)

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


    def draw_box(self ,position):
        # position in range 1 to 12
        y_long = 47  # mm , height of box
        x_long = 104 # mm , wide of box

        # y_header = 10 # mm point from header
        # x_header = 0  # mm point from header


        x_start , y_start = self.start_point_from_position(position)

        self.rect(x_start, y_start, x_long, y_long, style = '')

    def start_point_from_position(self ,position):
        # position in range 1 to 12
        y_long = 47  # mm , height of box
        x_long = 104 # mm , wide of box

        y_header = 10 # mm point from header
        x_header = 0  # mm point from header

        if position < 1 :
            position = 1
        elif position > 0 :
            position = position % 12
        else :
            position = int(position) 

        if position == 0:
            position = 12

        position = position - 1 # First position start with 0
        
        if position % 2 == 0:
            # start point left box
            x = 1
        else:
            # start point right box
            x = 1 + x_long
        
        x_start = x + x_header
        y_start = ( ( position // 2 ) * y_long ) + y_header # plus 10 mm for header (y_header)

        return x_start ,y_start


# Setting to pdf
pdf = PDF()

pdf.set_title(title)
pdf.set_author(author)
pdf.set_margins(0.1 , 1.5, -0.1)


for Board_num in range(1,200):
    pdf.print_board(Board_num, get_dealer(Board_num) ,get_vul(Board_num) )



#pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
#pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
# to
#pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
#pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')

pdf.output(output_filename, 'F')




# docs
# https://github.com/reingart/pyfpdf/tree/master/docs