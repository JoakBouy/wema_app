import mysql.connector as mysql

db = mysql.connect(host="localhost",user="root",password="",database="hospital")
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("********************************************************************")
        print("*                        ADMINS ACCOUNT                            *")
        print("********************************************************************")        
        print("*                    1. Register new Patient                       *")
        print("*                    2. Register new Doctor                        *")
        print("*                    3. Delete Existing Patient                    *")
        print("*                    4. Delete Existing Doctor                     *")
        print("*                    5. Logout                                     *")
        print("********************************************************************")
        

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Register New Patient")
            username = input(str("Patient username : "))
            password = input(str("Patient password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users1 (username,password,privilege) VALUES (%s,%s,'patient')",query_vals)
            db.commit()
            print(username + " has been registered as a patient")
        
        elif user_option == "2":
            print("")
            print("Register New Doctor")
            username = input(str("Doctor username : "))
            password = input(str("Doctor password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users1 (username,password,privilege) VALUES (%s,%s,'doctor')",query_vals)
            db.commit()
            print(username + " has been registered as a doctor")
    
        elif user_option == "3":
            print("")
            print("Delete Existing Patient Account")
            username = input(str("Patient username : "))
            query_vals = (username,"patient")
            command_handler.execute("DELETE FROM users1 WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "4":
            print("")
            print("Delete Existing Doctor Account")
            username = input(str("Doctor username : "))
            query_vals = (username,"doctor")
            command_handler.execute("DELETE FROM users1 WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "5":
            break
        else:
            print("No valid option selected")


def auth_admin():
    print("********************************************************************")
    print("*                         ADMINS LOGIN                             *")
    print("********************************************************************")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised") 
        

def auth_patient():
    print("********************************************************************")
    print("*                         PATIENT LOGIN                           *")
    print("********************************************************************")
    username = input(str("Username : "))
    password = input(str("Password : "))
    query_vals = (username, password, "patient")
    command_handler.execute("SELECT username FROM users1 WHERE username = %s AND password = %s AND privilege = %s",query_vals)
    if command_handler.rowcount <= 0:
        print("Login not recognized")
    else:
        patient_session(username)
        
        
def patient_session(username):
    while 1:
        print("********************************************************************")
        print("*                         PATIENTS ACCOUNT                         *")
        print("********************************************************************")        
        print("*                   1. View prescription Status                    *")
        print("*                   2. Logout                                      *")
        print("********************************************************************")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("Displaying prescription status")
            username = (str(username),)
            command_handler.execute("SELECT date, username, status FROM prescriptions1 WHERE username = %s",username)
            records = command_handler.fetchall()
            for record in records:
                print(record)
        elif user_option == "2":
            break
        else:
            print("No valid option was selected")
        

def auth_doctor():
    print("********************************************************************")
    print("*                         DOCTOR LOGIN                             *")
    print("********************************************************************")
    username = input(str("Username : "))
    password = input(str("Password : "))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users1 WHERE username = %s AND password = %s AND privilege = 'doctor'",query_vals)
    if command_handler.rowcount <= 0:
        print("Login not recognized")
    else:
        doctor_session()
    
    
def doctor_session():
    while 1:
        print("********************************************************************")
        print("*                         DOCTORS ACCOUNT                          *")
        print("********************************************************************")        
        print("*                     1. Prescribe                                 *")
        print("*                     2. View prescription status                  *")
        print("*                     3. Logout                                    *")
        print("********************************************************************")        
        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Log new prescription")
            command_handler.execute("SELECT username FROM USERS1 WHERE privilege = 'patient'")
            records = command_handler.fetchall()
            date    = input(str("Date : DD/MM/YYYY : "))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")

            #Prescribed | Not prescribed
            status = input(str("Status for " + str(record) + "P / NP : "))
            query_vals = (str(record),date,status)
            command_handler.execute("INSERT INTO prescriptions1 (username, date, status) VALUES(%s,%s,%s)",query_vals)
            db.commit()
            print(record + " has been marked as " + status)
        elif user_option == "2":
            print("")
            print("Viewing all patients prescriptions status")
            command_handler.execute("SELECT username, date, status FROM prescriptions1")
            records = command_handler.fetchall()
            print("Displaying all prescription status")
            for record in records:
                print(record)
        elif user_option == "3":
            break
        else:
            print("No valid option was selected")


def main():
    while 1:
        print("********************************************************************")
        print("*                                                                  *")
        print("*            Welcome to Wema Hospital Management System            *")
        print("*                                                                  *")
        print("********************************************************************")
        print("********************************************************************")        
        print("*                        1. Login as Patient                       *")
        print("*                        2. Login as Doctor                        *")
        print("*                        3. Login as Admin                         *")
        print("*                        4. Exit                                   *")
        print("********************************************************************")
        user_option = input(str("Option : "))
        if user_option == "1":
            auth_patient()       
        elif user_option == "2":
            auth_doctor()    
        elif user_option == "3":
            auth_admin()
        elif user_option == "4":
            break
        else:
            print("No valid option was selected")
main()