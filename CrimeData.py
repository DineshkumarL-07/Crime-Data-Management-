import pyodbc
pyodbc.drivers()
from tabulate import tabulate
# from signup import signUp
conn = pyodbc.connect('DRIVER={MySQL ODBC 8.3 Unicode Driver};'
                            'SERVER=127.0.0.1;'
                            'PORT=3306;'
                            'DATABASE=crime;'
                            'USER=root;'
                            'PASSWORD=dineshsql7;'
                            'TRUSTED_CONNECTION=Yes;')
cursor = conn.cursor()
class Validate:
     
    #  def __init__(self):
    #      self.conn = pyodbc.connect('DRIVER={MySQL ODBC 8.3 Unicode Driver};'
    #                                 'SERVER=127.0.0.1;'
    #                                 'PORT=3306;'
    #                                 'DATABASE=crime;'
    #                                 'USER=root;'
    #                                 'PASSWORD=dineshsql7;'
    #                                 'TRUSTED_CONNECTION=Yes;')
    #      self.cursor = self.conn.cursor()

     def vaild(self,mailid,pwd):
         self.mail = mailid
         self.pwd = pwd
         query = 'SELECT pass FROM USER WHERE EMAILID=? or USERNAME=?'
         cursor.execute(query,self.mail,self.mail)
         password = cursor.fetchone()
         if password == None:
             print('\nEmail ID not found. Please Enter an valid Email ID or Sign Up\n')
         else:       
             for i in password:
                 if i == self.pwd:
                    print("\nWelcome sir!\n")
                    return True
                 else:
                    print("Enter the vaild Password\n")

class CrimeDatabase(Validate):
     
     def __init__(self):
         super().__init__()
    
     def options(self):
         print(f'1) VIEW CRIME DATA\n2) ADD NEW CRIME DATA\n3) ADD CRIMINAL DETAILS\n4) VIEW CRIMINAL DATA\n5) ADD VICTIM DETAILS\n6) VIEW VICTIM DATA\n7) FINAL REPORT\n8) FOR OTHER OPERATIONS\n9) EXIT\n')
         option = int(input("Enter your option: "))
         while option != 9:
            print()
            temp = cri.view() if option == 1 else cri.add_crime() if option == 2 else cri.add_criminal() if option == 3 else cri.view_criminal() if option == 4 else cri.add_victim() if option == 5 else cri.view_victim() if option == 6 else cri.final_report() if option == 7 else Other() if option == 8 else print("Enter an vaild option")
            option = int(input("Enter Your option: "))

     def view(self):
         print("List of the crime and their details are:\n")
         query = 'SELECT * FROM CRIME'
         cursor.execute(query)
         rows = cursor.fetchall()
        #  header = ["CRIME_ID","CRIME_DATE","POLICE_STATION_NAME","CRIME_DETAILS","CRIME_STATUS","CRIME_PLACE","CRIME_WITNESS","CRIME_EVIDENCE"]
        #  print(tabulate(rows,header))
         for row in rows:
             print(f'CRIME_ID: {row.CRIMEID}\nCRIME_DATE: {row.DATEOFCRIME}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIME_DETAILS: {row.DISCRIPTION}\nCRIME_STATUS: {row.STATUSOFCRIME}\nCRIME_PLACE: {row.PLACEOFCRIME}\nCRIME_WITNESS: {row.WITNESS}\nCRIME_EVIDENCE: {row.EVIDENCE}\n')
        
     def add_crime(self):
         print("Enter the crime details in the given order")
         date = input("Enter the crime date: ")
         police = input("Enter the police station name: ")
         details = input("Enter the crime details: ")
         status = input("Enter the crime status: ")
         place = input("Enter the crime place: ")
         witness = input("Enter the crime witness details: ")
         evidence = input("Enter the crime evidence: ")
         query = """INSERT INTO CRIME(DATEOFCRIME,POLICESTATIONID,DISCRIPTION,STATUSOFCRIME,PLACEOFCRIME,WITNESS,EVIDENCE) VALUES (?, ?, ?, ?, ?, ?, ?)"""
         cursor.execute(query,date,police,details,status,place,witness,evidence)
         conn.commit()
         print("Crime Data was Added Successfully")

     def add_criminal(self):
         print("Enter the criminal details in the given order")
         name = input("Enter the criminal name: ")
         aadhaar = input("Enter the criminal Aadhaar Number: ")
         age = input("Enter the criminal Age: ")
         gender = input("Enter the criminal Gender: ")
         Address = input("Enter the criminal address: ")
         police = input("Enter the police station name: ")
         birthmark = input("Enter the birthmark of the criminal: ")
         query = """INSERT INTO CRIMINAL(C_NAME,C_AADHAAR,C_AGE,C_GENDER,C_ADDRESS,POLICESTATIONID,BIRTHMARK) VALUES (?, ?, ?, ?, ?, ?, ?)"""
         cursor.execute(query,name,aadhaar,age,gender,Address,police,birthmark)
         conn.commit()
         print("Criminal Data was Added Successfully")
    
     def view_criminal(self):
         print("The List of the criminal and their details are:\n")
         query = 'SELECT * FROM CRIMINAL'
         cursor.execute(query)
         rows = cursor.fetchall()
         for row in rows:
             print(f'CRIMINAL_ID: {row.CRIMINALID}\nCRIMINAL_NAME: {row.C_NAME}\nCRIMINAL_AADHAAR: {row.C_AADHAAR}\nCRIMINAL_AGE: {row.C_AGE}\nCRIMINAL_GENDER: {row.C_GENDER}\nCRIMINAL_ADDRESS: {row.C_ADDRESS}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIMINAL_IDENTIFICATION_MARK: {row.BIRTHMARK}\n')

     def add_victim(self):
         print("Enter the Victim details in the given order")
         name = input("Enter the victim name: ")
         age = input("Enter the victime Age: ")
         gender = input("Enter the victim Gender: ")
         Address = input("Enter the victim address: ")
         aadhaar = input("Enter the victim Aadhaar Number: ")
         description = input("Enter the victim's description: ")
         query = """INSERT INTO VICTIM(v_NAME,V_AGE,V_GENDER,V_ADDRESS,V_AADHAAR,V_DISCRIPTION) VALUES (?, ?, ?, ?, ?, ?)"""
         cursor.execute(query,name,age,gender,Address,aadhaar,description)
         conn.commit()
         print("Victim Data was Added Successfully")

     def view_victim(self):
         print("The List of the victims and their details are:\n")
         query = 'SELECT * FROM VICTIM'
         cursor.execute(query)
         rows = cursor.fetchall()
         for row in rows:
             print(f'VICTIM_ID: {row.VICTIMID}\nVICTIM_NAME: {row.V_NAME}\nVICTIM_AADHAAR: {row.V_AADHAAR}\nVICTIM_AGE: {row.V_AGE}\nVICTIM_GENDER: {row.V_GENDER}\nVICTIM_ADDRESS: {row.V_ADDRESS}\nVICTIM_DESCRIPTION: {row.V_DISCRIPTION}\n')
    
     def final_report(self):
         print("Report")


class Other(Validate):
    
    def __init__(self):
        super().__init__()
        
        print(f'1) SEARCH SPECIFIC DETAIL IN CRIME DATA\n2) SEARCH SPECIFIC DETAIL IN CRIMINAL DATA\n3) SEARCH SPECIFIC DEATIL IN VICTIM DATA\n4) UPDATE CRIME STATUS\n5) REMOVE THE CRIME DETAILS\n6) REMOVE VICTIM DETAILS\n7) REMOVE CRIMINAL DETAILS')
        op = int(input("Enter the option: "))
        print()
        self.options(op)
    
    def options(self,option):
        temp = self.search_crime() if option == 1 else self.search_criminal() if option == 2 else self.search_victim() if option == 3 else  self.update_status() if option == 4 else self.remove_crime() if option == 5 else print("Please enter an vaild option")
        
    def search_crime(self):
        col = input("Enter the column that you want to search for data: ")
        val = input("Enter the search element: ")
        print()
        query = f"SELECT * FROM CRIME WHERE {col} LIKE '%{val}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
             print(f'CRIME_ID: {row.CRIMEID}\nCRIME_DATE: {row.DATEOFCRIME}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIME_DETAILS: {row.DISCRIPTION}\nCRIME_STATUS: {row.STATUSOFCRIME}\nCRIME_PLACE: {row.PLACEOFCRIME}\nCRIME_WITNESS: {row.WITNESS}\nCRIME_EVIDENCE: {row.EVIDENCE}\n')
           
    def search_criminal(self):
        col = input("Enter the column that you want to search for criminal data: ")
        val = input("Enter the search element: ")
        query = f"SELECT * FROM CRIMINAL WHERE {col} LIKE '%{val}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
             print(f'CRIMINAL_ID: {row.CRIMINALID}\nCRIMINAL_NAME: {row.C_NAME}\nCRIMINAL_AADHAAR: {row.C_AADHAAR}\nCRIMINAL_AGE: {row.C_AGE}\nCRIMINAL_GENDER: {row.C_GENDER}\nCRIMINAL_ADDRESS: {row.C_ADDRESS}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIMINAL_IDENTIFICATION_MARK: {row.BIRTHMARK}\n')

    def search_victim(self):
        col = input("Enter the column that you want to search for criminal data: ")
        val = input("Enter the search element: ")
        query = f"SELECT * FROM CRIMINAL WHERE {col} LIKE '%{val}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
             print(f'VICTIM_ID: {row.VICTIMID}\nVICTIM_NAME: {row.V_NAME}\nVICTIM_AADHAAR: {row.V_AADHAAR}\nVICTIM_AGE: {row.V_AGE}\nVICTIM_GENDER: {row.V_GENDER}\nVICTIM_ADDRESS: {row.V_ADDRESS}\nVICTIM_DESCRIPTION: {row.V_DISCRIPTION}\n')

    def update_status(self):
        id = int(input("Enter the ID where to you want to update: "))
        val = input("Enter the value that you want to update the status of crime: ")
        query = f'UPDATE CRIME SET STATUSOFCRIME = ? WHERE CRIMEID = ?'
        cursor.execute(query,val,id)
        conn.commit()
        print("The details was updated successfully")
    
    def remove_crime(self):
        id = int(input("Enter the ID to remove the crime data: "))
        query = """DELETE FROM CRIME WHERE CRIMEID = ?"""
        cursor.execute(query,id)
        conn.commit()
        print("The crime details was removed successfully")
    
    def remove_victim(self):
        id = int(input("Enter the ID to remove the victim data: "))
        query = """DELETE FROM VICTIM WHERE VICTIMID = ?"""
        cursor.execute(query,id)
        conn.commit()
        print("The victim details was removed successfully")

    def remove_criminal(self):
        id = int(input("Enter the ID to remove the criminal data: "))
        query = """DELETE FROM CRIMINAL WHERE CRIMINAL_ID = ?"""
        cursor.execute(query,id)
        conn.commit()
        print("The criminal details was removed successfully")
        

print("\t\t\tWELCOME TO THE CRIME DATABASE\n")
print(f"1) Sign Up\n2) Sign In\n")
initial = int(input("Enter your choice: "))
ans = 0
if initial == 1:
    ans = signUp()
elif ans == True or initial == 2:
    print()
    emailid = input("Enter your Mail ID or Username: ")
    password = input("Enter your password: ")
    check = Validate()
    a = check.vaild(emailid,password)
    if a == True:
        cri = CrimeDatabase()
        cri.options()
    else:
        print('Enter vaid input or Sign Up\n')
else:
    print("Enter an valid choice")