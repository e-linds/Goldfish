import sqlite3

con = sqlite3.connect("app.db")
cur = con.cursor()


def add_new(month, date, location):
    cur.execute(f"INSERT INTO attendance VALUES ({month}, {date}, {location})")
    con.commit()

# result = cur.execute("SELECT name FROM sqlite_master")
# print(result.fetchone())


