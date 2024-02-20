from conn import Conn
from tabulate import tabulate

class Overall:

    def overall(self):
        id = int(input("Enter Crime ID To View Overall Crime Details: "))
        query = """SELECT CRIMINAL_ID FROM CC WHERE CRIME_ID = ?"""
        Conn.cursor.execute(query,id)
        c_id = Conn.cursor.fetchone()
        criminal_id = c_id[0]
        query2 = """SELECT V_ID FROM CV WHERE C_ID = ?"""
        Conn.cursor.execute(query2,id)
        v_id = Conn.cursor.fetchone()
        victim_id = v_id[0]
        header = ["CRIME_ID","VICTIM_NAME","CRIMINAL_NAME","DATE_OF_CRIME","POLICESTATION_ID","CRIME_DETAILS","CRIME_STATUS"]
        row = []
        row.append(id)
        query3 = """SELECT VICTIMNAME FROM VICTIM WHERE VICTIMID = ?"""
        Conn.cursor.execute(query3,victim_id)
        v_name = Conn.cursor.fetchone()
        row.append(v_name[0])
        query4 = """SELECT CRIMINALNAME FROM CRIMINAL WHERE CRIMINALID = ?"""
        Conn.cursor.execute(query4, criminal_id)
        c_name = Conn.cursor.fetchone()
        row.append(c_name[0])
        query5 = """SELECT DATEOFCRIME,POLICESTATIONID,CRIMEDESCRIPTION,STATUSOFCRIME FROM CRIME WHERE CRIMEID  = ?"""
        Conn.cursor.execute(query5,id)
        c_temp = Conn.cursor.fetchall()
        for i in range(4):
            row.append(c_temp[0][i])
        rows = []
        rows.append(row)
        print(tabulate(rows,header,tablefmt="rounded_grid"))
