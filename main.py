from conn import Conn
from search import Search
from signup import signUp
from view import View
from validate import Validate
from add import Add
from remove import Remove
from overall import Overall

class CrimeDatabase():
    def options(self):
        print("1) VIEW DATA\n2) ADD DATA\n3) REPORT\n4) ADD USER\n5) SEARCH DATA\n6) UPDATE CRIME STATUS\n7) REMOVE DATA\n8) VIEW OVERALL CRIME DETAIL\n9) EXIT")
        opt = int(input("Enter Your Choice: "))
        obj = Overall()
        while opt != 9:
            temp = View() if opt == 1 else Add() if opt == 2 else self.report() if opt == 3 else signUp() if opt == 4 else Search() if opt == 5 else self.update_status() if opt == 6 else Remove() if opt == 7 else obj.overall() if opt == 8 else print("Enter valid choice")
            opt = int(input("Enter Your Choice: "))

    def report(self):
        print("Here, You can made an final report of the crime")
        id = int(input("Enter The Crime ID: "))
        criminal = input("Enter the Criminal ID or Criminal Name: ")
        victim = input("Enter the Victim ID or Victim Name: ")
        if criminal.isnumeric():
            criminal_id = criminal
        else:
            query = """SELECT CRIMINALID FROM CRIMINAL WHERE CRIMINALNAME = ?"""
            Conn.cursor.execute(query,criminal)
            c_id = Conn.cursor.fetchone()
            criminal_id = c_id[0]
        if victim.isnumeric():
            victim_id = victim
        else:
            query = """SELECT VICTIMID FROM VICTIM WHERE VICTIMNAME = ?"""
            Conn.cursor.execute(query,victim)
            v_id = Conn.cursor.fetchone()
            victim_id = v_id[0]
        query1 = """INSERT INTO CC VALUES (?,?)"""
        Conn.cursor.execute(query1,id,criminal_id)
        Conn.connection.commit()
        query2 = """INSERT INTO CV VALUES (?,?)"""
        Conn.cursor.execute(query2,id,victim_id)
        Conn.connection.commit()
        print(f"The Crime Report for Crime ID {id} is added successfully")

    def update_status(self):
        id = int(input("Enter The Crime ID : "))
        val = input("Enter The Status Of The Crime : ")
        query = f'UPDATE CRIME SET STATUSOFCRIME = ? WHERE CRIMEID = ?'
        Conn.cursor.execute(query, val, id)
        Conn.connection.commit()
        print(f"The Crime Status of the Crime ID {id} was Updated Successfully")

print("*******************************************  WELCOME TO THE CRIME DATA MANAGEMENT  ************************************")
print(f"1) SIGN UP \n2) LOG IN\n")
initial = int(input("Enter Your Choice: "))
ans = 0
if initial == 1:
    ans = signUp()
elif ans == True or initial == 2:
    print()
    emailid = input("Enter Your Email ID or Username: ")
    password = input("Enter Your Password: ")
    check = Validate(emailid,password)
    temp = check.vaild()
    if temp == True:
        cri = CrimeDatabase()
        cri.options()
    else:
        print('Enter valid input or Sign Up\n')
else:
    print("Enter an valid choice")
