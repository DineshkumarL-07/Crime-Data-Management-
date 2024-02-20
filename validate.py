from conn import Conn

class Validate:
    def __init__(self, mailid, pwd):
        self.mailid = mailid
        self.pwd = pwd

    def vaild(self):
        query = 'SELECT pass FROM USER WHERE EMAILID=? or USERNAME=?'
        Conn.cursor.execute(query, self.mailid, self.mailid)
        password = Conn.cursor.fetchone()
        if password == None:
            print('\nEmail ID Not Found. Please Enter An Valid Email ID or Sign Up\n')
        else:
            for i in password:
                if i == self.pwd:
                    print("\nWelcome sir!\n")
                    return True
                else:
                    print("Enter The Valid Password\n")