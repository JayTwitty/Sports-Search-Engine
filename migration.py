# writing a front-loaded migration. putting a lot of data into our database.

# create a table.

# insert data using the cursor.execute method

import psycopg2

conn = psycopg2.connect(user="tiger_twitty", database="clemson_google")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS offensive_stats_2015;")

create_table_string = """
        CREATE TABLE offensive_stats_2015 (
        player_name varchar(40),
        player_position varchar(10),
        jersey_number numeric(2),
        plays_from_scrimmage numeric(3),
        yards_from_scrimmage numeric(4),
        ave_yrds_per_play_from_scrimmage real,
        TDs_from_scrimmage numeric(2)
        )
        """
cur.execute(create_table_string)
conn.commit()

insert_template = "INSERT INTO offensive_stats_2015 VALUES (%s, %s, %s, %s, %s, %s, %s)"

roster = [['wayne gallman','rb',9,304,1740,5.7,14],
          ['deshaun watson','qb',4,207,1105,5.3,12],
          ['zac brooks','rb',24,50,347,6.9,5],
          ['c.j. fuller','rb',27,46,215,4.7,1],
          ['kelly bryant','qb',2,23,156,6.8,2],
          ['tyshon dye','rb',23,23,91,4.0,2],
          ['c.j. davidson','rb',21,22,60,2.7,0],
          ['ray-ray mccloud','wr',34,36,299,8.3,1],
          ['artavis scott','wr',3,99,921,9.3,7],
          ['nick schuessler','qb',12,6,-23,-3.8,0],
          ['deon cain','wr',8,35,577,16.5,5],
          ['charone peake','wr',19,50,716,14.3,5],
          ['jordan leggett','te',16,40,525,13.1,8],
          ['hunter renfrow','wr',13,33,492,14.9,5],
          ['germone hopper','wr',5,21,317,15.1,1],
          ['mike williams','wr',7,2,20,10,1]
          ]

for player in roster:
    cur.execute(insert_template, player)
    conn.commit()

cur.close()
conn.close()