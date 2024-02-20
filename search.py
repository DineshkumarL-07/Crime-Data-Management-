from conn import Conn
from tabulate import tabulate

class Search:
    def __init__(self):
        print("SPECIFY THE DATA THAT YOU WANT TO SEARCH")
        print("1) SEARCH CRIME DATA\n2) SEARCH CRIMINAL DATA\n3) SEARCH VICTIM DATA\n4) EXIT")
        opt = int(input("\nEnter Your Choice: "))
        while opt != 4:
            temp = self.search_crime() if opt == 1 else self.search_criminal() if opt == 2 else self.search_victim() if opt == 3 else print("Invalid Choice")
            opt = int(input("\nEnter Your Choice: "))

    def search_crime(self):
        col = input("Enter The Column Name:  ")
        val = input("Enter The Column Value: ")
        query = f"SELECT * FROM CRIME WHERE {col} LIKE '%{val}%'"
        Conn.cursor.execute(query)
        rows = Conn.cursor.fetchall()
        header = ["CRIME_ID", "CRIME_DATE", "POLICE_STATION_NAME", "CRIME_DETAILS", "CRIME_STATUS", "CRIME_PLACE",
                  "CRIME_WITNESS", "CRIME_EVIDENCE"]
        print(tabulate(rows, header, tablefmt="rounded_grid"))
    def search_criminal(self):
        col = input("Enter The Column Name:  ")
        val = input("Enter The Column Value: ")
        query = f"SELECT * FROM CRIMINAL WHERE {col} LIKE '%{val}%'"
        Conn.cursor.execute(query)
        rows = Conn.cursor.fetchall()
        header = ["CRIMINAL_ID", "CRIMINAL_NAME", "CRIMINAL_AADHAAR", "CRIMINAL_AGE", "CRIMINAL_GENDER",
                  "CRIMINAL_ADDRESS", "POLICE_STATION_NAME", "CRIMINAL_IDENTIFICATION_MARK"]
        print(tabulate(rows, header, tablefmt="rounded_grid"))


    def search_victim(self):
        col = input("Enter The Column Name:  ")
        val = input("Enter The Column Value: ")
        query = f"SELECT * FROM VICTIM WHERE {col} LIKE '%{val}%'"
        Conn.cursor.execute(query)
        rows = Conn.cursor.fetchall()
        header = ["VICTIM_ID", "VICTIM_NAME","VICTIM_AGE", "VICTIM_GENDER", "VICTIM_ADDRESS","VICTIM_AADHAAR"
                  "VICTIM_DESCRIPTION"]
        print(tabulate(rows, header, tablefmt="rounded_grid"))