from tabulate import tabulate
from conn import Conn

class View:
    def __init__(self):
        print("SPECIFY THE DATA THAT YOU WANT TO VIEW")
        print("1) VIEW CRIME DATA\n2) VIEW CRIMINAL DATA\n3) VIEW VICTIM DATA\n4) EXIT")
        opt = int(input("\nEnter Your Choice: "))
        while opt != 4:
            temp = self.view_crime() if opt == 1 else self.view_criminal() if opt == 2 else self.view_victim() if opt == 3 else print("Enter An Valid Choice!")
            opt = int(input("\nEnter Your Choice: "))

    def view_crime(self):
        print("Select the which format you want to view crime data")
        print("1) In Table Format\n2) In Normal Format")
        temp = int(input("\nEnter Your Format choice:"))
        query = 'SELECT * FROM CRIME'
        Conn.cursor.execute(query)
        rows = Conn.cursor.fetchall()
        if temp == 1:
            header = ["CRIME_ID","CRIME_DATE","POLICE_STATION_NAME","CRIME_DETAILS","CRIME_STATUS","CRIME_PLACE","CRIME_WITNESS","CRIME_EVIDENCE"]
            print(tabulate(rows,header,tablefmt="rounded_grid"))
        elif temp == 2:
            for row in rows:
                print(f'CRIME_ID: {row.CRIMEID}\nCRIME_DATE: {row.DATEOFCRIME}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIME_DETAILS: {row.DISCRIPTION}\nCRIME_STATUS: {row.STATUSOFCRIME}\nCRIME_PLACE: {row.PLACEOFCRIME}\nCRIME_WITNESS: {row.WITNESS}\nCRIME_EVIDENCE: {row.EVIDENCE}\n')
        else:
            print("Invalid Choice")
    def view_criminal(self):
        print("Select the which format you want to view criminal data")
        print("1) In Table Format\n2) In Normal Format")
        temp = int(input("\nEnter Your Format choice:"))
        query = 'SELECT * FROM CRIMINAL'
        Conn.cursor.execute(query)
        rows = Conn.cursor.fetchall()
        if temp == 1:
            header = ["CRIMINAL_ID","CRIMINAL_NAME","CRIMINAL_AADHAAR","CRIMINAL_AGE","CRIMINAL_GENDER","CRIMINAL_ADDRESS","POLICE_STATION_NAME","CRIMINAL_IDENTIFICATION_MARK"]
            print(tabulate(rows,header,tablefmt="rounded_grid"))
        elif temp == 2:
            for row in rows:
                print(f'CRIMINAL_ID: {row.CRIMINALID}\nCRIMINAL_NAME: {row.CRIMINALNAME}\nCRIMINAL_AADHAAR: {row.CRIMINALAADHAAR}\nCRIMINAL_AGE: {row.CRIMINALAGE}\nCRIMINAL_GENDER: {row.CRIMINALGENDER}\nCRIMINAL_ADDRESS: {row.CRIMINALADDRESS}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIMINAL_IDENTIFICATION_MARK: {row.BIRTHMARK}\n')
        else:
            print("Invalid Choice")
    def view_victim(self):
        print("Select the which format you want to view criminal data")
        print("1) In Table Format\n2) In Normal Format")
        temp = int(input("\nEnter Your Format choice:"))
        query = 'SELECT * FROM VICTIM'
        Conn.cursor.execute(query)
        rows = Conn.cursor.fetchall()
        if temp == 1:
            header = ["VICTIM_ID","VICTIM_NAME","VICTIM_AGE","VICTIM_GENDER","VICTIM_ADDRESS","VICTIM_AADHAAR","VICTIM_DESCRIPTION"]
            print(tabulate(rows, header, tablefmt="rounded_grid"))
        elif temp == 2:
            for row in rows:
                print(f'VICTIM_ID: {row.VICTIMID}\nVICTIM_NAME: {row.V_NAME}\nVICTIM_AADHAAR: {row.V_AADHAAR}\nVICTIM_AGE: {row.V_AGE}\nVICTIM_GENDER: {row.V_GENDER}\nVICTIM_ADDRESS: {row.V_ADDRESS}\nVICTIM_DESCRIPTION: {row.V_DISCRIPTION}\n')
        else:
            print("Invalid Choice")
