import mysql.connector
from datetime import datetime


mysql = mysql.connector.connect(host='eu-cdbr-west-03.cleardb.net',
                                user='b148a915877d9d',
                                password='1176558d',
                                database='heroku_3ccb9a620c4cfd1',)

def db_query(query):
    global mysql
    try:
        cur = mysql.cursor(dictionary=True)
        cur.execute(query)
        try:
            data =  cur.fetchall()
        except:
            data =  mysql.commit()

        return data
    except:
        mysql.reconnect(1,1)
        db_query(query)

def isLoginValid(phone_number, pin):
    userData = db_query(f"SELECT user_id, pin FROM user WHERE user_id={phone_number.strip()} AND pin={pin}")
    if len(userData)>0:
        return True
    else:
        return False


def get_balance(user_id):
    print(user_id)
    userData = db_query(f"SELECT balance FROM user WHERE user_id={user_id.strip()}")
    return userData[0]['balance']


def username_exist(user_id):
    userData = db_query(f"SELECT user_id FROM user WHERE user_id={user_id.strip()}")
    if len(userData)>0:
        return True
    else:
        return False

def create_user(full_name, phone,pin, email_address):
    userData = db_query(f'''INSERT INTO user (name, user_id, pin, email_address, balance, joining_date) 
    VALUES ('{full_name.strip()}', '{phone}', '{pin}', '{email_address}', 0, '{datetime.now().strftime("%Y-%m-%d")}')''')
    print(userData)


def send_txn(user_id, amount, receiver, note):
    db_query(f'UPDATE user SET balance=balance - {amount} where user_id={user_id}')
    db_query(f'''INSERT INTO transaction (user_id, Date, amount, remarks, reciever_id')
                VALUES ('{user_id}', '{datetime.now().strftime("%Y-%m-%d")}', {amount},'{note}','{receiver}')''')

def savings_transfer(user_id, amount):
    pass

def total_savihgs(user_id):
    pass

def transaction_statement(user_id):
    pass

def deposit(user_id, amount,payslip, type="PENDING"):
    pass

def withdraw(user_id, amount, bank, account_number, type="PENDING"):
    #user will withdraw money
    pass

def get_unapproved_deposit_withdraw():
    #Returns all the pending deposit and withdraw from those tables. Admins will approve or reject it
    pass

