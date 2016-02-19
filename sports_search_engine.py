#Connect to the 'clemson_google' database with user 'tiger_twitty'

import psycopg2
conn = psycopg2.connect(user="tiger_twitty", database="clemson_google")
cur = conn.cursor()

print("\nThis is the Clemson Google database for 2015 Offensive Football Stats.\n")
search = True
while search:
    player_search = input("Which offensive player would you like to search for? ")
    cur.execute("select * from offensive_stats_2015 where player_name = (%s);",(player_search,))
    player_search_row = cur.fetchone()
    if player_search_row == None:
        print("\nSorry, That player was not found")
        print("=" * 20)
    else:
        print("\nPlayer Name: " + "\t","\t","\t","\t","\t","\t","\t",player_search_row[0])
        print("Position: " + "\t","\t","\t","\t","\t","\t","\t","\t",player_search_row[1])
        print("Jersey number: " + "\t","\t","\t","\t","\t","\t","\t",str(player_search_row[2]))
        print("Total Plays from Scrimmage: " + "\t","\t","\t",str(player_search_row[3]))
        print("Total Yards from Scrimmage: " + "\t","\t","\t",str(player_search_row[4]))
        print("Average Yards per play from Scrimmage: " + "\t",str(player_search_row[5]))
        print("Total TDs from Scrimmage: " + "\t","\t","\t","\t",str(player_search_row[6]))
        print("=" * 20)
        
    position_check = "y"
    while position_check == "y":
        position_check = input("\nWould you like to search by position? (Type 'y' or 'n') ")
        print('-' * 20)

        if position_check == "y":
            position_search = input("Which positions would you like to search for? (Type 'qb', 'rb', or 'wr') ")
            cur.execute("SELECT * FROM offensive_stats_2015 WHERE player_position = (%s);", (position_search,))
            position_search_row = cur.fetchall()
            print('=' * 20)
            print("Data for %s position group:" % (position_search.upper()))
            print('=' * 20)
            for player in position_search_row:
                print("Player Name: " + "\t","\t","\t","\t","\t","\t","\t",player[0])
                print("Position: " + "\t","\t","\t","\t","\t","\t","\t","\t",player[1])
                print("Jersey number: " + "\t","\t","\t","\t","\t","\t","\t",str(player[2]))
                print("Total Plays from Scrimmage: " + "\t","\t","\t",str(player[3]))
                print("Total Yards from Scrimmage: " + "\t","\t","\t",str(player[4]))
                print("Average Yards per play from Scrimmage: " + "\t",str(player[5]))
                print("Total TDs from Scrimmage: " + "\t","\t","\t","\t",str(player[6]))
                print("-" * 20)
        else:
            continue

    insert_player = "y"
    while insert_player == "y":
        insert_player = input("Would you like to insert new player data? (Type 'y' or 'n')")
        if insert_player == "y":
            insert_player_string = """player_name,
            player_position,
            jersey_number,
            plays_from_scrimmage,
            yards_from_scrimmage,
            ave_yrds_per_play_from_scrimmage,
            tds_from_scrimmage"""
            name = input("\nWhat is the player's name? ")
            position = input("\nWhat is the {}'s position? ".format(name))
            jersey = input("\nWhat is the {}'s jersey number? ".format(name))
            plays = input("\nHow many plays from scrimmage did {} have in 2015? ".format(name))
            yards = input("\nHow many yards from scrimmage did {} have in 2015? ".format(name))
            ave = input("\nWhat was the average yards per play for {} in 2015? ".format(name))
            tds = input("\nHow many Touchdowns did {} score in 2015? ".format(name))
            cur.execute("INSERT INTO offensive_stats_2015 VALUES (%s, %s, %s, %s, %s, %s, %s);",(name,position,jersey,plays,yards,ave,tds))
            conn.commit()
        else:
            print("-" * 20)
            continue
    keep_going = input("Would you like to search again? (Type 'y' or 'n')" )
    if keep_going == "y":
        continue

    else:
        break

cur.close()
conn.close()