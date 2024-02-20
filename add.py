from conn import Conn

class Add:
    def __init__(self):
        print("SPECIFY THE DATA THAT YOU WANT TO ADD")
        print("1) ADD CRIME DATA\n2) ADD CRIMINAL DATA\n3) ADD VICTIM DATA\n4) EXIT")
        opt = int(input("Enter Your Choice"))
        while opt != 4:
            temp = self.add_crime() if opt == 1 else self.add_criminal() if opt == 2 else self.add_victim() if opt == 3 else print("Invalid choice")
            opt = int(input("Enter Your Choice"))

    def add_crime(self):
        print("Enter The Crime Details")
        date = input("Enter The Crime Date: ")
        police = input("Enter The Police Station Name: ")
        details = input("Enter The Crime Details: ")
        status = input("Enter The Crime Status: ")
        place = input("Enter The Crime Place: ")
        witness = input("Enter The Crime Witness Details: ")
        evidence = input("Enter The Crime Evidence: ")
        query = """INSERT INTO CRIME(DATEOFCRIME,POLICESTATIONID,CRIMEDESCRIPTION,STATUSOFCRIME,PLACEOFCRIME,WITNESS,EVIDENCE) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        Conn.cursor.execute(query, date, police, details, status, place, witness, evidence)
        Conn.connection.commit()
        print("Crime Data was Added Successfully")

    def add_criminal(self):
        print("Enter The Criminal Details")
        name = input("Enter The Criminal Name: ")
        aadhaar = input("Enter The Criminal Aadhaar Number: ")
        age = input("Enter The Criminal Age: ")
        gender = input("Enter The Criminal Gender: ")
        Address = input("Enter The Criminal Address: ")
        police = input("Enter The Police Station Name: ")
        birthmark = input("Enter The Birthmark Of The Criminal: ")
        query = """INSERT INTO CRIMINAL(CRIMINALNAME,CRIMINALAADHAAR,CRIMINALAGE,CRIMINALGENDER,CRIMINALADDRESS,POLICESTATIONID,BIRTHMARK) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        Conn.cursor.execute(query, name, aadhaar, age, gender, Address, police, birthmark)
        Conn.connection.commit()
        print("Criminal Data was Added Successfully")

    def add_victim(self):
        print("Enter The Victim Details")
        name = input("Enter The Victim Name: ")
        age = input("Enter The Victime Age: ")
        gender = input("Enter The Victim Gender: ")
        Address = input("Enter The Victim Address: ")
        aadhaar = input("Enter The Victim Aadhaar Number: ")
        description = input("Enter The Victim's Description: ")
        query = """INSERT INTO VICTIM(VICTIMNAME,VICTIMAGE,VICTIMGENDER,VICTIMADDRESS,VICTIMAADHAAR,VICTIMDESCRIPTION) VALUES (?, ?, ?, ?, ?, ?)"""
        Conn.cursor.execute(query, name, age, gender, Address, aadhaar, description)
        Conn.connection.commit()
        print("Victim Data was Added Successfully")
