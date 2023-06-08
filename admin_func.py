import sqlite3
import trip_db as t



print("print admin")

def loc_profile():
    print("[1]List Location",
          "[2]Enter Location:")
    opt = input()

    if opt == "1":
        print("List Locations")
        print(t.rtrv_data('loc_profile', 'Locations'))
    elif opt == "2":
        conn = sqlite3.connect('SysTA.db')
        print("***open database success***")
        loc_country = input("Enter Country:")
        loc_city = input("Enter City:")
        loc_price = input("Enter Price:")
        print("The trip package available period:")
        loc_start_date = input("Start Date (MM-DD-YYYY):")
        loc_end_date = input("End Date (MM-DD-YYYY):")
        loc_list = [(loc_country, loc_city, loc_price, loc_start_date, loc_end_date)]
        with conn:
            conn = sqlite3.connect('SysTA.db')
            c = conn.cursor()
            c.executemany("INSERT INTO loc_profile (country, city, price, start_date, end_date) VALUES (?,?,?,?,?);", loc_list)
            conn.commit()
            conn.close()
        #print(["country", "city", "price", "start_date", "end_date"])
        #print(loc_list)
        print("Enter successful")
        print(t.rtrv_data('loc_profile', 'Locations'))
    else:
        print("404")
    print("-End-")

def cust_profile():
    print("[1]List Customers",
          "[2]Create Customer Profile")
    opt = input()

    if opt == "1":
        print("List Customers")
        print(t.rtrv_data('cust_profile', 'Customers'))
    elif opt == "2":
        conn = sqlite3.connect('SysTA.db')
        cust_name = input("Enter Customer Name:")
        phone = input("Enter Customer Phone:")
        cust_list = [(cust_name, phone)]
        with conn:
            conn = sqlite3.connect('SysTA.db')
            c = conn.cursor()
            c.executemany("INSERT INTO cust_profile (cust_name, phone) VALUES (?,?);", cust_list)
            conn.commit()
            conn.close()
        #print(["cust_name", "phone"])
        #print(cust_list)
        print("Enter successful")
        print(t.rtrv_data('cust_profile', 'Customers'))
    else:
        print("404")
    print("-End-")

def booking(): #cust-loc-price-date period
    print("[1]List Booking Options",
          "[2]Booking for customer")
    opt = input()

    if opt == "1": #[1]List Booking Options
        print("List Bookings")
        print(t.rtrv_data('booking', 'booking'))
    elif opt == "2": #[2]Booking for customer
        conn = sqlite3.connect('SysTA.db')
        #booking_id += 1
        fk_cust_id = eval(input("Enter Customer ID:"))
        fk_loc_id = eval(input("Enter Location ID:"))
        trvl_date = input("Enter Travel Date (MM-DD-YYYY):")
        paid = bool(eval(input("Customer Paid? ('1' if Paid, '0' if not Paid):")))
        booking_list = ([trvl_date, paid, fk_loc_id, fk_cust_id])
        with conn:
            conn = sqlite3.connect('SysTA.db')
            c = conn.cursor()
            c.execute("INSERT INTO booking (trvl_date, paid, fk_loc_id, fk_cust_id) \
                      VALUES (?,?,?,?)", booking_list)
            conn.commit()
            conn.close()
        print("booking_id", "cust_id", "trvl_date", "paid")
        print(booking_list)
        print(t.rtrv_data('booking', 'booking'))
    else:
        print("404")
    print("-End-")

def rep_out():
    t.orders_city()
    return

def audit_out(): #data storage
    print(t.audit_out())
    return
