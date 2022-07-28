# Importing Packages
import sqlite3
import pandas as pd
# Creating DB using SQLiteJDBC driver
db = sqlite3.connect('../DB/interesting_movies.db')
# DB Cursor
cursor = db.cursor()
# Creating Tables
# cursor.execute('''CREATE TABLE movies(id INTEGER PRIMARY KEY, Movie_Name TEXT, Lead_Actor TEXT, Lead_Actress TEXT, Director_Name TEXT, Year_Of_Release YEAR)''')
# Inserting Data into tables
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(1,"Anjali","Raghuvaran","Revathi","Mani Ratnam",1990)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(2,"Vikram","Kamal Haasan","Shivani Narayanan","Lokesh Kanagaraj",2022)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(3,"Avvai shanmugi","Kamal Haasan","Meena","K. S. Ravikumar",1996)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(4,"Alaipayuthey ","R. Madhavan","Shalini","Mani Ratnam",2000)''')

# SELECT statement to query all rows from the Movies table
sqlite_select_query = """SELECT * from movies"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print(pd.DataFrame(records,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))

# SELECT query with parameter like actor name to select movies based on the actor's name
sqlite_select_query = """SELECT * from movies where Lead_Actor = 'Kamal Haasan'"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print(pd.DataFrame(records,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))
