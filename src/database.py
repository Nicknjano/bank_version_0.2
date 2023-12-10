'''This file carries all database functions of the project'''
import sqlite3
import os
class Database:
    def __init__(self):
        self.file_path = os.path.dirname(os.path.abspath(__file__))
        self.database_path = os.path.join(self.file_path,'bank_database.db')
        self.create_table_admins()
        self.create_table_customers()

    def create_table_admins(self):
        '''This function creates the admins table of the system'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        mycursor.execute("""CREATE TABLE IF NOT EXISTS admins (
                         staff_number TEXT NOT NULL PRIMARY KEY,
                         password TEXT,
                         first_name TEXT,
                         second_name TEXT,
                         last_name TEXT,
                         position TEXT,
                         status TEXT
        )""")
        connection.commit()
        connection.close()

    def create_table_customers(self):
        '''this function creates the customers table'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        mycursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                         customer_id TEXT NOT NULL PRIMARY KEY,
                         first_name TEXT,
                         second_name TEXT,
                         last_name TEXT,
                         account_type TEXT,
                         account_balance NUMERIC
        )""")
        connection.commit()
        connection.close()

    def add_admin(self,staff_number,password,first_name,second_name,last_name,position,status):
        '''adds admin to the database'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("INSERT INTO admins VALUES (?,?,?,?,?,?,?)",
                                (staff_number,password,first_name,second_name,last_name,position,status,))
        except:
            print('something went wrong')
        connection.commit()
        connection.close()

    def add_customer(self,customer_id,first_name,second_name,last_name,account_type,account_balance):
        '''adds customer details to db'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("INSERT INTO customers VALUES (?,?,?,?,?,?)",
                                (customer_id,first_name,second_name,last_name,account_type,account_balance,))
        except:
            print('something went wrong')
        connection.commit()
        connection.close()

    def get_customer(self,customer_id):
        '''retrieve customer details from db'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("SELECT * FROM customers WHERE customer_id = (?)",
                                (customer_id,))
            data = mycursor.fetchall()
            if data == None:
                print('No records retrieved')
            else: 
                print(data)
        except:
            print('something went wrong')
        connection.close()

    def get_admin(self,staff_number):
        '''retrieves admin info from db'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("SELECT * FROM admins WHERE staff_number = (?)",
                                (staff_number,))
            data = mycursor.fetchall()
            if data == None:
                print('No records retrieved')
            else: 
                print(data)
        except:
            print('something went wrong')
        connection.close()

    def get_balance(self,customer_id):
        '''retrieves customer balance'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("SELECT account_balance FROM customers WHERE customer_id = (?)",
                                (customer_id,))
            data = mycursor.fetchone()[0]
            if data == None:
                print('No records retrieved')
            else: 
                print(data)
        except:
            print('something went wrong')
        connection.close()