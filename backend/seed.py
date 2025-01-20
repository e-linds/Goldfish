from functions import sqlite3, con, cur, month as month_var
import random


cur.execute("DROP TABLE IF EXISTS attendance")

cur.execute('''CREATE TABLE IF NOT EXISTS attendance(
            month INT, 
            date INT, 
            weekday INT,
            ip_location TEXT
            )''')


def seed_db(month, date, weekday, location): 
    cur.execute(f"INSERT INTO attendance (month, date, weekday, ip_location) VALUES({month}, {date}, '{weekday}', '{location}')")
    con.commit()


locations = ["home", "office", "The Wild", "Hello Darling"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


for each in range(1,20):
    
    rand_location = random.choice(locations)
    rand_weekday = random.choice(weekdays)
    seed_db(month_var, each, rand_weekday, rand_location)



    # I would like to rebuild this to create instances for all days of the week including sat and sun
    # and then build the seed function to avoid those
    # but this works for now
