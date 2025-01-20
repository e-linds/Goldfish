import requests
from models import add_new
import datetime
import pprint

from dotenv import load_dotenv

load_dotenv()


import sqlite3

con = sqlite3.connect("app.db")
cur = con.cursor()

month = datetime.datetime.now().month
date = datetime.datetime.now().day

weekday_int = datetime.datetime.now().weekday()
weekday = None

def get_weekday():
    if weekday_int == 0:
        return("Monday")
    elif weekday_int == 1:
        return("Tuesday")
    elif weekday_int == 2:
        return("Wednesday")
    elif weekday_int == 3:
        return("Thursday")
    elif weekday_int == 4:
        return("Friday")
    elif weekday_int == 5:
        return("Saturday")
    elif weekday_int == 6:
        return("Sunday")
    else:
        raise Exception("something's wrong with the get_weekday function dude")
    
weekday = get_weekday()

def add_new(month, date, weekday, location):
    cur.execute(f"INSERT INTO attendance (month, date, weekday, ip_location) VALUES({month}, {date}, '{weekday}', '{location}')")
    con.commit()


def check_ip():
    url="https://ifconfig.me"
    response=requests.get(url)
    full_address = list(response.text)
    
    #pulling first four values of ip address
    full_address = full_address[slice(4)]

    #And turning back into a string
    address_to_check =  ''.join(full_address)

    return(address_to_check)


def get_location():
    if check_ip() == "2601":
        print("home")
        return("home")
    elif check_ip() == "testestestestes":
        print("I'm at the office")
        return("office")
    elif check_ip() == "204.":
        print("The Wild")
        return("The Wild")
    else:
        print("I'm somewhere else")
        return("somewhere else")


def add_to_db():
    location = get_location()

    if weekday != "Sunday" and weekday != "Saturday":
        add_new(month, date, weekday, location)
    elif weekday == "Sunday" or weekday == "Saturday":
        print("It's the weekend!")
    else: 
        raise Exception("it's not the weekend but also not not the weekend...hmmm")


def check_monthly_numbers(location):
    result1 = cur.execute(f"SELECT * FROM attendance WHERE ip_location='{location}'")
    results1 = result1.fetchall()

    location_days = len(results1)

    percentage = int(100 * (location_days / date))

    print(f"{location_days} days at {location} = {percentage}% of the month so far.")


def print_attendance():
    pprint.pp(list(cur.execute("SELECT * FROM attendance")))
