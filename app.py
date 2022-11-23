#import mysql.connector as mysql

#db = mysql.connect(host="localhost",user="root",password="",database="hospital")
#command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Patient")
        print("2. Register new Doctor")
        print("3. Delete Existing Patient")
        print("4. Delete Existing Doctor")
        print("5. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Register New Patient")
            username = input(str("Patient username : "))
            password = input(str("Patient password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'patient')",query_vals)
            db.commit()
            print(username + " has been registered as a patient")
        
        elif user_option == "2":
            print("")
            print("Register New Doctor")
            username = input(str("Doctor username : "))
            password = input(str("Doctor password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'doctor')",query_vals)
            db.commit()
            print(username + " has been registered as a doctor")
    
        elif user_option == "3":
            print("")
            print("Delete Existing Patient Account")
            username = input(str("Patient username : "))
            query_vals = (username,"patient")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
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
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
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
    print("")
    print("Admin Login")
    print("")
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
    print("")
    print("Patient Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "patient":
        if password == "password":
            patient_session()
        else:
            print("Incorrect Username or Password!")
    else:
        print("Login details not recognized")
        
        
#def patient_session():
    while 1:
        print("")
        print("Patient Menu")
        print("1: View Prescription")
        
        
def auth_doctor():
    print("")
    print("Doctor Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "doctor":
        if password == "password":
            doctor_session()
        else:
            print("Incorrect Username or Password!")
    else:
        print("Login details not recognized")
    
    
#def doctor_session():
    while 1:
        print("")
        print("Doctor Menu")
        print("1: Prescribe medication")
        
    

def main():
    while 1:
        print("")
        print("Welcome to the WEMA Hospital Management system :) ")
        print("")
        print("1. Login as Patient")
        print("2. Login as Doctor")
        print("3. Login as Admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_patient()       
        elif user_option == "2":
            auth_doctor()    
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid option was selected")

main()