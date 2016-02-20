#Connect to the 'clemson_google' database with user 'tiger_twitty'

import psycopg2
conn = psycopg2.connect(user="tiger_twitty", database="clemson_google")
cur = conn.cursor()

print("\nWelcome to the Clemson Google database for 2015 Offensive Football Stats.")
search = True
while search:
    player_check = "y"
    while player_check == "y":
        player_check = input("\nWould you like to search stats by player? (Type 'y' or 'n') ").lower()
        if player_check == "y":
            player_search = input("\nWhich offensive player would you like to search for? ").lower()
            cur.execute("select * from offensive_stats_2015 where player_name = (%s);",(player_search,))
            player_search_row = cur.fetchone()
            if player_search_row == None:
                print("\nSorry, That player was not found")
                print("=" * 20)
            else:
                print("\nPlayer Name: " + "\t","\t","\t","\t","\t","\t","\t",player_search_row[0].upper())
                print("Position: " + "\t","\t","\t","\t","\t","\t","\t","\t",player_search_row[1].upper())
                print("Jersey number: " + "\t","\t","\t","\t","\t","\t","\t",str(player_search_row[2]))
                print("Total Plays from Scrimmage: " + "\t","\t","\t",str(player_search_row[3]))
                print("Total Yards from Scrimmage: " + "\t","\t","\t",str(player_search_row[4]))
                print("Average Yards per play from Scrimmage: " + "\t",str(player_search_row[5]))
                print("Total TDs from Scrimmage: " + "\t","\t","\t","\t",str(player_search_row[6]))
                print("=" * 20)
        else:
            print("=" * 20)
            break
    position_check = "y"
    while position_check == "y":
        position_check = input("\nWould you like to search by position? (Type 'y' or 'n') ").lower()
        if position_check == "y":
            position_search = input("\nWhich positions would you like to search for? (Type 'qb', 'rb', or 'wr') ").lower()
            if position_search in ["rb", "qb", "wr"]:
                cur.execute("SELECT * FROM offensive_stats_2015 WHERE player_position = (%s);", (position_search,))
                position_search_row = cur.fetchall()
                print('=' * 20)
                print("\nData for %s position group:" % (position_search.upper()))
                print('=' * 20)
                for player in position_search_row:
                    print("Player Name: " + "\t","\t","\t","\t","\t","\t","\t",player[0].upper())
                    print("Position: " + "\t","\t","\t","\t","\t","\t","\t","\t",player[1].upper())
                    print("Jersey number: " + "\t","\t","\t","\t","\t","\t","\t",str(player[2]))
                    print("Total Plays from Scrimmage: " + "\t","\t","\t",str(player[3]))
                    print("Total Yards from Scrimmage: " + "\t","\t","\t",str(player[4]))
                    print("Average Yards per play from Scrimmage: " + "\t",str(player[5]))
                    print("Total TDs from Scrimmage: " + "\t","\t","\t","\t",str(player[6]))
                    print("-" * 20)
            else:
                print("Invalid entry")
        else:
            print("=" * 20)
            continue
    insert_player = "y"
    while insert_player == "y":
        insert_player = input("\nWould you like to insert new player data? (Type 'y' or 'n') ").lower()
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
            print("-" * 20)
            try:
                cur.execute("INSERT INTO offensive_stats_2015 VALUES (%s, %s, %s, %s, %s, %s, %s);",(name,position,jersey,plays,yards,ave,tds))
            except Exception:
                print("Invalid entry\n")
                pass
            conn.commit()
        else:
            print("=" * 20)
            continue
    keep_going = input("\nWould you like to search again? (Type 'y' or 'n') " )
    print("\n")
    if keep_going == "y":
        print("=" * 20)
        continue
    else:
        print("=" * 20)
        print("Thank you for using Clemson Google. Goodbye! #GoTigers™ ")
        print("=" * 20)
        search = False

cur.close()
conn.close()