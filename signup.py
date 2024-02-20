import re
from conn import Conn

def signUp():

    EMAIL_RE = r'^[a-z0-9\.\_]{1,}@\w+.\w+'
    password = "crimeDATA"
    passcode = input("Enter your passcode to sign Up:")
    if passcode == password:
        name = input("Enter the user name:")
        email = input("Enter an Email id:")
        if re.search(EMAIL_RE,email):
            pwd = input("Enter an New password:")
            renter = input("Re-enter the password to confirm:")
            if pwd == renter:
                print(f"Sign Up successfully completed,{name}")
            else:
                while(pwd != renter):
                    print("Password and Confirm Password doesn't match. Enter correct one")
                    renter = input("Re-enter the password to confirm:")
                print(f"Sign Up successfully completed,{name}")
            query = """INSERT INTO USER(USERNAME,EMAILID,PASS) VALUES (?, ?, ?)"""
            Conn.cursor.execute(query,name,email,pwd)
            Conn.connection.commit()
        else:
            print("Enter an valid EmailID")
        return True

    else:
        print("Invalid Passcode")
    return False