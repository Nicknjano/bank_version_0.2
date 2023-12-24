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
                         status TEXT DEFAULT Active
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
                         account_balance NUMERIC NOT NULL DEFAULT (0) 
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
            print('admin added successfully')
        except:
            connection.close()
            return 1
        connection.commit()
        connection.close()

    def add_customer(self,customer_id,first_name,second_name,last_name,account_type,account_balance):
        '''adds customer details to db'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        existence = self.get_customer(customer_id)
        if existence != None:
            return 'customer exists'
        if customer_id == '':
            return 1
        try:
            mycursor.execute("INSERT INTO customers VALUES (?,?,?,?,?,?)",
                                (customer_id,first_name,second_name,last_name,account_type,account_balance,))
            print('customer added successfully')
        except :
            connection.close()
            return 2
        connection.commit()
        connection.close()

    def get_customer(self,customer_id):
        '''retrieve customer details from db'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("SELECT * FROM customers WHERE customer_id = (?)",
                                (customer_id,))
            data = mycursor.fetchone()
            if data == None:
                return
            else: 
                connection.close()
                return data
        except Exception as e:
            connection.close()

    def get_customers(self):
        '''retrieve all customers'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM customers")
        data = mycursor.fetchall()
        connection.close()
        return data
    
    def update_customer(self,customer_id,first_name,second_name,last_name,account_type,account_balance):
        '''updates the customers details'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        result = self.get_customer(customer_id)
        if result == None:
            return 1
        try:
            mycursor.execute("""UPDATE customers 
                             SET first_name=(?),
                             second_name = (?),
                             last_name =(?),
                             account_type=(?),
                             account_balance= (?)
                             where customer_id=(?) """,(first_name,second_name,last_name,account_type,account_balance,customer_id,))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            return 2

    def delete_customer(self,customer_id):
        '''delete a choosen customer from the DB'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("DELETE FROM customers where customer_id = (?) ",
                                (customer_id,))
        except:
            return 1
        connection.commit()
        connection.close()

    def get_admin(self,staff_number,password):
        '''retrieves admin info from db'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute("SELECT * FROM admins WHERE staff_number = (?) and password = (?)",
                                (staff_number,password,))
            data = mycursor.fetchone()
            if data == None:
                print('No records retrieved')
            else:
                print(len(data)) 
                return data
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
                return
            else: 
                return data
        except:
            print('something went wrong')
        connection.close()

    def deposit(self,customer_id,amount):
        '''handles customer deposits into accounts'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        balance = self.get_balance(customer_id)
        amount = amount + balance
        try:
            mycursor.execute("UPDATE customers SET account_balance = (?) where customer_id = (?)",
                             (amount,customer_id,))
        except:
            print('something went wrong')
        connection.commit()
        connection.close()

    def withdraw(self,customer_id,amount):
        '''handles withdrawal of funds from accounts'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        balance = self.get_balance(customer_id)
        amount = balance - amount
        if amount < 0 :
            print ('Low account balance, can not complete transaction')
            return 0
        try:
            mycursor.execute("UPDATE customers SET account_balance = (?) where customer_id = (?)",
                             (amount,customer_id,))
            
        except:
            print('something went wrong')
        connection.commit()
        connection.close()

    def transfer(self,customer_id,recepient_id,funds_source,amount):
        '''handles transfer of funds from an account to another'''
        connection = sqlite3.connect(self.database_path)
        mycursor = connection.cursor()
        try:
            mycursor.execute('BEGIN')
            sender_balance = self.get_balance(customer_id)
            recepient_balance = self.get_balance(recepient_id)
            if (sender_balance - amount) < 0:
                connection.close()
                return 1
            else:
                mycursor.execute("UPDATE customers SET account_balance = (?) where customer_id = (?)",
                             ((sender_balance-amount),customer_id,))
                mycursor.execute("UPDATE customers SET account_balance = (?) where customer_id = (?)",
                             ((recepient_balance+amount),recepient_id,))
            mycursor.execute('COMMIT')
        except:
            mycursor.execute('ROLLBACK')
            return 2
        finally:
            connection.close()
