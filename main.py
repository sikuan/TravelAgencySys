import admin_func as a
from trip_db import *
print('main')

####### README ##############
##--Group Members
##--1. Taneja, Chandan (8748475)
##--2. Kuan, Sao I (8777987)
#############################
##--SyS Default password: 123
####### README ##############

def option(opt):

    if opt == "1":
        a.loc_profile()
    elif opt == "2":
         a.cust_profile()
    elif opt == "3":
         a.booking()
    elif opt == "4":
         a.rep_out()
    elif opt == "5":
         a.audit_out()
    else:
         print("404")

def login(): #pw: 123
    pw = input("admin password:")
    if pw == "123":

        print("login Successful")
        print("[1]Location",
              "[2]Customer",
              "[3]Booking",
              "[4]Report",
              "[5]Audit")
        option(input("action:"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dbPath = input("Sqlite3 Path:")
    create_connection(r"{}".format(dbPath))
    print("**** Hello Travel Agency ****")
    login()
