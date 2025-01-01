import sqlite3


class Score:
 def __init__(self):
  self.create_table()


 def create_table(self):
    with sqlite3.connect('scores.db') as conn: #also commits changes
     cur = conn.cursor()
     cur.execute("""CREATE TABLE IF NOT EXISTS scores ( 
          user TEXT, 
          score INTEGER,
          UNIQUE(user)
          )""") #creates table - the unique constraint allows only one entry per user
 
    
 def add_table(self, user_name):
   with sqlite3.connect('scores.db') as conn: 
     cur = conn.cursor()
     cur.execute('SELECT score FROM scores WHERE user=(?)',(user_name,))
     scoring = cur.fetchone() 
     if scoring is None:
      first_values = {'user':user_name,'score':1}
      cur.execute('INSERT INTO scores(user, score) VALUES (:user, :score)', first_values) #adds new row with user and first score 
     else:
      score = scoring[0] + 1
      cur.execute('UPDATE scores SET score = (?) WHERE user = (?)', (score, user_name)) #updates score value in the table for required user
    

 def show_user_score(self, user_name):
   with sqlite3.connect('scores.db') as conn: 
     cur = conn.cursor()
     cur.execute("SELECT score FROM scores WHERE user = (?)", (user_name,)) #selects score from required user
     items = cur.fetchone()
     for item in items:
      return item[0]


 def show_all_scores(self):
   with sqlite3.connect('scores.db') as conn: 
     cur = conn.cursor()
     cur.execute("SELECT * FROM scores") #selects all data in the table scores
     items = cur.fetchall()
     for item in items:
      return str(item[0])+"\t\t\t\t"+str(item[1])


 def delete_all_scores(self):
   with sqlite3.connect('scores.db') as conn: 
     cur = conn.cursor()
     cur.execute("DELETE FROM scores") #deletes all data


 def delete_user_score(self, user_name):
   with sqlite3.connect('scores.db') as conn: 
     cur = conn.cursor()
     cur.execute("DELETE * FROM scores WHERE user = (?)", user_name) #deletes data of selected user 

 


