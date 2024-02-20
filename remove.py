from conn import Conn

class Remove:
    def __init__(self):
        print("SPECIFY THE DATA THAT YOU WANT TO REMOVE")
        print("1) REMOVE CRIME DATA\n2) REMOVE CRIMINAL DATA\n3) REMOVE VICTIM DATA\n4) EXIT")
        opt = int(input("\nEnter Your Choice: "))
        while opt!=4:
            temp = self.remove_crime() if opt == 1 else self.remove_criminal() if opt == 2 else self.remove_victim() if opt == 3 else print("Invalid Choice")
            opt = int(input("\nEnter Your Choice: "))

    def remove_crime(self):
        id = int(input("Enter Crime ID to Remove The Crime Data : "))
        query = """DELETE FROM CRIME WHERE CRIMEID = ?"""
        Conn.cursor.execute(query, id)
        Conn.connection.commit()
        print("The Crime Detail Was Removed Successfully")

    def remove_criminal(self):
        id = int(input("Enter Criminal ID or Criminal Name to Remove The Data: "))
        query = """DELETE FROM CRIMINAL WHERE CRIMINALID = ? OR CRIMINALNAME = ?"""
        Conn.cursor.execute(query, id,id)
        Conn.connection.commit()
        print("The Criminal Detail Was Removed Successfully")

    def remove_victim(self):
        id = int(input("Enter Victim ID or Victim Name to Remove The Data: "))
        query = """DELETE FROM VICTIM WHERE VICTIMID = ? OR VICTIMNAME = ?"""
        Conn.cursor.execute(query,id,id)
        Conn.connection.commit()
        print("The Victim Detail Was Removed Successfully")
