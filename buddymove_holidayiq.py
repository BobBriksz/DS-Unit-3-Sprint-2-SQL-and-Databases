import pandas as pd 
import sqlite3

# Load csv into pandas dataframe

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)

# create database and set the cursor
con = sqlite3.connect("buddymove_holidayiq.sqlite")
c = con.cursor()

# Created table with parameters for the columns
c.execute('CREATE TABLE REVIEW (User ID text, Sports number, Religious number, Nature number, Theatre number, Shopping number, Picnic number)')
con.commit()

# send the pandas dataframe to the sql db
df.to_sql('REVIEW', con, if_exists='replace', index = False)

c.execute("""
    SELECT Nature, Shopping
    FROM REVIEW
    WHERE Nature>=100
    INTERSECT
    SELECT Nature, Shopping
    FROM REVIEW
    WHERE Shopping >=100;)
"""
for row in c.fetchall():
    print(row)