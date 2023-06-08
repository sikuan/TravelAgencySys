import sqlite3
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import openpyxl

############################## CREATE DB ##############################

def create_connection(db_file = '/Users/kuan/PycharmProjects/conestoga/SysProj/SysTA.db'):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print("Connected Database")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

############################## SCHEMA ##############################

def create_table_loc():
    conn = sqlite3.connect('SysTA.db')
    c = conn.cursor()
    print("***open database success***")
    try:
        c.execute('''CREATE TABLE loc_profile
                 (
                 loc_id    INTEGER PRIMARY KEY AUTOINCREMENT,
                 country   CHAR(20) NOT NULL,
                 city      CHAR(20) NOT NULL,
                 price     REAL  NOT NULL,
                 start_date DATE    NOT NULL,
                 end_date   DATE    NOT NULL
                 );''') #available regist travel preiod: "start_date to end_date"
        print("Location table created successfully.")
    except sqlite3.OperationalError as e:
        #pass
        print(e)
        print("***loc_profile table exist***")
    conn.commit()
    conn.close()

def create_table_cust():
    conn = sqlite3.connect('SysTA.db')
    c = conn.cursor()
    print("***open database success***")
    try:
        c.execute('''CREATE TABLE cust_profile
                 (
                 cust_id    INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
                 cust_name  CHAR(20) NOT NULL,
                 phone      NUMERIC  NOT NULL
                 );''')
        print("Customer table created successfully.")
    except sqlite3.OperationalError as e :
        print(e)
        print("***cust_profile table exist***")
    conn.commit()
    conn.close()

def create_table_booking():
    conn = sqlite3.connect('SysTA.db')
    print("***open database success***")
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE booking \
                 ( \
                 booking_id    INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,\
                 trvl_date DATE NOT NULL,\
                 paid      INTEGER NOT NULL,\
                 fk_loc_id  INTEGER NOT NULL,
                 fk_cust_id INTEGER NOT NULL,
                 FOREIGN KEY (fk_loc_id) REFERENCES loc_profile(loc_id),\
                 FOREIGN KEY (fk_cust_id) REFERENCES cust_profile(cust_id)\
                 );''') #one date trip: trvl_date
        print("Booking table created successfully.")
    except sqlite3.OperationalError as e:
        #pass
        print(e)
        print("***booking table exist***")
    conn.commit()
    conn.close()

############################## Pre-insert data ##############################

def pre_insert_data():
    conn = sqlite3.connect('SysTA.db')
    c = conn.cursor()
    print("***open database success***")

    c.execute("INSERT INTO loc_profile (loc_id, country, city, price, start_date, end_date) \
              VALUES (1, 'Canada', 'Waterloo', 2000, '04-10-2022', '04-17-2022' )")

    c.execute("INSERT INTO loc_profile (loc_id, country, city, price, start_date, end_date) \
              VALUES (2, 'Canada', 'Toronto', 2000, '04-11-2022', '04-18-2022' )")

    c.execute("INSERT INTO cust_profile (cust_id, cust_name, phone) \
              VALUES (1, 'Shirley', 26705424  )")

    c.execute("INSERT INTO cust_profile (cust_id, cust_name, phone) \
              VALUES (2, 'Mary', 26671810  )")

    c.execute("INSERT INTO booking (booking_id, trvl_date, paid, fk_loc_id, fk_cust_id) \
              VALUES (101, '04-11-2022', 1, 1, 1  )")

    c.execute("INSERT INTO booking (booking_id, trvl_date, paid, fk_loc_id, fk_cust_id) \
               VALUES (102, '04-11-2022', 1, 2, 2  )")

    conn.commit()
    print("pre-insert success.")
    conn.close()

############################## AUDIT ORDERS ##############################

def audit_out():
    conn = sqlite3.connect('SysTA.db')
    c = conn.cursor()
    print("***open database success***")
    print("List Customer Bookings")
    cursor = c.execute("SELECT * FROM booking \
                        LEFT JOIN loc_profile ON loc_profile.loc_id = fk_loc_id \
                        LEFT JOIN cust_profile ON cust_profile.cust_id = fk_cust_id")
    colnames = cursor.description
    header = []
    for head in colnames:
        header.append(head[0])
    print()
    audit_list = cursor.fetchall()
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(audit_list, columns = header)
    #print(df)
    filename = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    df.to_excel(f'{filename}.xlsx', header=True, index=True)
    print("Download successful")
    conn.close()
    return df

############################## Retrieve Data ##############################

def rtrv_data(tbl, list_name):
    conn = sqlite3.connect('SysTA.db')
    c = conn.cursor()
    print("***open database success***")
    print(f"List {list_name}")
    cursor = c.execute(f"SELECT * FROM {tbl};")
    colnames = cursor.description
    header = []
    for head in colnames:
        header.append(head[0])
    print()
    audit_list = cursor.fetchall()
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(audit_list, columns=header)
    #print(df)
    return df
    conn.close()

############################## PLOT GRAPH ##############################

def orders_city(): #counting how many orders in a city in a dataframe as table
    df = audit_out()
    df_city = df.groupby(['city'])['city'].count().to_frame('count')
    print(df_city)
    plot_bar = df_city.plot.bar()
    plt.show() #show bar chart as graph
    return

############################## TEST AREA ##############################

