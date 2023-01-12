import sqlite3
#import os.path

class Database:
  # class to modifiled database ( bridge_board_sample.db file ) by using sqlite3 on python3
  # Database filename
  DB_filename = "bridge_board_sample.db"
  # Connect to database
  conn = None
  cur = None
  

  def __init__(self):
    # Connect to database 
    self.conn = sqlite3.connect(self.DB_filename)
    # Cursor of Connection
    self.cur = self.conn.cursor()
    
    self.check_if_table_exist()


  def connect_db(self):
    # Connect to modifiled DB
    # Set connection and cursor
    self.conn = sqlite3.connect(self.DB_filename)
    self.cur = self.conn.cursor()

  def disconnect_db(self):
    # Disconnect and save data to DB
    self.conn.commit()
    self.conn.close()



  def create_table_bridge_board(self):
    self.connect_db()
    """
    self.cur.execute('''CREATE TABLE bridge_board
               (N_card, E_card, W_card, S_card)''')
    """
    self.cur.execute('''CREATE TABLE bridge_board
               (pbn_desk, max_score_deals)''')

    self.disconnect_db()

  #def add_board(self ,N_card ,E_card ,S_card ,W_card):
  def add_board(self ,pbn_desk, max_score_deals):
    self.connect_db()
    """
    string = "INSERT INTO bridge_board VALUES ('" + \
             N_card + "','" + \
             E_card + "','" + \
             S_card + "','" + \
             W_card + "')"
    """
    
    string = "INSERT INTO bridge_board VALUES ('" + \
             pbn_desk + "','" + \
             max_score_deals + "')"
             
    #print(string)
    self.cur.execute(string)

    #self.cur.execute('''INSERT INTO bridge_board
    #            VALUES ('AK.AK.AKJT.','AK.AK.AKJT.','AK.AK.AKJT.','AK.AK.AKJT.')''')

    self.disconnect_db()

  def get_select_board(self ,get_only = ["Part score","Game part","Small Slam","Grand Slam"] ,sort_type = "Random" ,limit = 20 ):
    # Example Input
    # sort = "Random" , "Grand Slam to Part score" ,"Part score to Grand Slam"
    # get_only = ["Part score","Game part","Small Slam","Grand Slam"]
    #
    self.connect_db()
    
    if get_only == []:
      get_only_exe = ""
    else:
      get_only_str = ""
      for i in get_only:
        get_only_str = get_only_str +'"'+ i + '"' + ","
      get_only_str = get_only_str[:-1]

      get_only_exe = '''WHERE "max_score_deals" IN (''' + get_only_str + ") " 

    #print(get_only)

    sort_exe = ""

    if sort_type == "Random":
      sort_exe = '''ORDER BY RANDOM() '''
    elif sort_type == "Grand Slam to Part score":
      sort_exe = '''ORDER BY CASE "max_score_deals "
      WHEN "Grand Slam" THEN 0
      WHEN "Small Slam" THEN 1
      WHEN "Game part"  THEN 2
      WHEN "Part score" THEN 3
      END '''
    elif sort_type == "Part score to Grand Slam":
      sort_exe = '''ORDER BY CASE "max_score_deals "
      WHEN "Part score" THEN 0
      WHEN "Game part"  THEN 1
      WHEN "Small Slam" THEN 2
      WHEN "Grand Slam" THEN 3
      END '''
    elif sort_type == "Latest":
      sort_exe = '''ORDER BY rowid DESC '''
    else:
      sort_exe = ""

    
    limit_exe = "LIMIT " + str(limit) + " "


    # Example
    #string_exe = '''SELECT * FROM bridge_board WHERE "max_score_deals" IN ("Part score","Game part") ORDER BY RANDOM() LIMIT 20
    string_exe = '''SELECT * FROM bridge_board ''' + get_only_exe + sort_exe + limit_exe

    #print(string_exe)
    self.cur.execute(string_exe)
    #print(self.cur.fetchall())
    output = self.cur.fetchall()

    self.disconnect_db()

    return output
  
  def print_select_board(self):
    self.connect_db()
    #for row in self.cur.execute('SELECT * FROM bridge_board ORDER BY N_card'):
    for row in self.cur.execute('SELECT * FROM bridge_board ORDER BY max_score_deals'):
      print(row)
    self.disconnect_db()

  def check_if_table_exist(self):
    #check if table name "bridge_board" exist
    #SELECT name FROM sqlite_master WHERE type='table' AND name='table_name';
    self.connect_db()
    self.cur.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bridge_board';''')
    
    if self.cur.fetchone()[0]==1 :
      #print('Table exists.')
      self.disconnect_db()
    else :
      #print('Table "bridge_board" does not exist.')
      self.disconnect_db()
      self.create_table_bridge_board()

  #def check_if_row_exist(self ,N_card ,E_card ,W_card ,S_card):
  def check_if_row_exist(self ,pbn_desk):
    self.connect_db()
    
    #string = \
    #""" SELECT 1
    #FROM bridge_board 
    #WHERE N_card = '""" + N_card + """' AND E_card = '""" + E_card + """' AND  W_card = '""" + W_card + """' AND S_card = '""" + S_card + """'
    #"""
    
    #print(pbn_desk)
    #print(max_score_deals)

    string = \
    """SELECT 1 FROM bridge_board WHERE pbn_desk = '""" + pbn_desk + """'"""
    #print(string)

    self.cur.execute(string)

    #a = self.cur.fetchone()

    if self.cur.fetchone() == None :
      #print('Row does not exist.')
      self.disconnect_db()
      return False
    else :
      #print('Row exists.')
      self.disconnect_db()
      return True

    
    """
    if self.cur.fetchone()[0] == 1 :
      #print('Row exists.')
      self.disconnect_db()
      return True
    else :
      #print('Row does not exist.')
      self.disconnect_db()
      return False
    """
  def get_row_number(self):
    self.connect_db()

    self.cur.execute('''SELECT Count(*) FROM bridge_board;''')
    #print(self.cur.fetchone()[0])
    row_num = self.cur.fetchone()[0]

    self.disconnect_db()

    return row_num



  def del_all_from_table(self):
    self.connect_db()
    self.cur.execute('''DELETE FROM bridge_board;''')

    self.disconnect_db()

  def get_row_limit(self ,num):
    self.connect_db()
    
    string = \
    """SELECT * FROM bridge_board ORDER BY RANDOM() LIMIT """ + str(num)

    #print(string)

    self.cur.execute(string)

    list_row = self.cur.fetchall()
    self.disconnect_db()
    #print(self.cur.fetchall())

    return list_row
    


# Testing example zone
  """
  def create_table(self):
    self.connect_db()
    self.cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')
    self.disconnect_db()
  
  def add_data(self):
    self.connect_db()
    self.cur.execute('''INSERT INTO stocks 
        VALUES ('2006-01-05','BUY','RHAT',100,35.14)''')
    self.disconnect_db()

  def print_select(self):
    self.connect_db()
    for row in self.cur.execute('SELECT * FROM stocks ORDER BY price'):
      print(row)
    self.disconnect_db()
  """




  
  def get_row_where(self):
    # NT > 3
    pass



#a = Database()
#a.check_if_row_exist("N:QT.T9543.AK.KT84 E:K9543.Q76.94.A97 W:AJ7.AJ2.JT87652. S:862.K8.Q3.QJ6532")
#a.add_board('N:QT.T9543.AK.KT84 E:K9543.Q76.94.A97 W:AJ7.AJ2.JT87652. S:862.K8.Q3.QJ6532 ','small slam')
#a.print_select_board()
#print(a.get_row_limit(5))
#a.get_row_number()
#a.del_all_from_table()

"""
#a.add_board("JT963.AQ87.A63.7","Q72.J62.K84.AKQ9","A5.T543.JT7.J432","K84.K9.Q952.T865")
#a.add_board                ("AQ.63.AJT4.KJ865","T42.9842.9863.32","K9763.KQT5.Q.AQ9","J85.AJ7.K752.T74")
#a.print_select_board()

#print(a.check_if_row_exist("AQ.63.AJT4.KJ865","T42.9842.9863.32","K9763.KQT5.Q.AQ9","J85.AJ7.K752.T74"))
#print( a.check_if_row_exist("AQ.63.AJT4.KJ865","T42.9842.9863.32","K9763.KQT5.Q.AQ9","J85.AJ7.K752.T74") )

#print(a.get_row_limit(3))

#a.del_all_from_table()
#a.print_select_board()
"""














