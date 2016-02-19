#Connect to the 'clemson_google' database with user 'tiger_twitty'

import psycopg2
conn = psycopg2.connect(user="tiger_twitty", database="clemson_google")
cur = conn.cursor()

"""def read_file():
   with open("stats_text_file") as infile:
       data = infile.readlines()
   return [line.replace('\n','').split(",") for line in data]"""

cur.execute("select * from offensive_stats_2015")
rows = cur.fetchall()
#print(rows[0])
player_search = input("Which player do you want to search for? ")

for player in rows:
   if player[0] == player_search:
       cur.execute("select * from offensive_stats_2015 where player_name = (%s);",(player_search,))
       row = cur.fetchall()
       print(row)

cur.close()
conn.close()