import pandas as pd 

datafile = "one.xlsx"


ex = pd.DataFrame(columns=["ID", "Email", "Password", "AccountNumber", "BankBalance","Status"])
ex.to_excel(datafile, index=False)

class UserInfo:
    def __init__(self):
        self.id = 0
        self.email = None
        self.accountnumber = None
        self.password = None
        self.bankbalance = 0
        self.status="active"

    def register(self):
        print("======Welcome to Register=======")
        self.id += 1
        print("Your ID is:", self.id)
        self.email = input("Enter Email: ")
        self.password = input("Enter Password: ")
        self.accountnumber = input("Enter Your Account Number: ")
        print("Register Successful, Login and use services")
        
        ex = pd.read_excel(datafile)

        if self.email in ex['Email'].values:
            print("Error: This email is already registered.\n")
            return

        user = pd.DataFrame([[self.id, self.email, self.password, self.accountnumber, self.bankbalance,self.status]], 
                            columns=["ID", "Email", "Password", "AccountNumber", "BankBalance","Status"])
        ex = pd.concat([ex, user], ignore_index=True)
        
        ex.to_excel(datafile, index=False)
        print("User added successfully!\n")

class Login(UserInfo):
    def logincheck(self):
        print("======Welcome to Login=======")
        self.username = input("Enter email: ")
        self.password = input("Enter Password: ")

        ex = pd.read_excel(datafile)
        user = ex[ex['Email'] == self.username]
    
        if ((self.username in ex['Email'].values) and (self.password in ex['Password'].values[0]) and (ex['Status'].values[0]=="active")):
            print("Login Successful")
            self.afterlogin()
        else:
            print("Please enter correct email and password or register if you don't have an account.")

    def afterlogin(self):
        while True:
            print("*************************")
            print("Welcome user information")
            print("*************************")
            print("1. Credit")
            print("2. Debit")
            print("3. Account Info")
            print("4. Close Account")
            print("5. Exit")

            j = int(input("Choose: "))

            if j == 1:
                self.credit()
                # Add credit
            elif j == 2:
                self.debit()
                # Add debit
            elif j == 3:
                self.showuserinfo()
            elif j == 4:
                self.closeaccount()
                break
            elif j == 5:
                print("Back to Main Menu")
                break
            else:
                print("Choose valid information")

    def showuserinfo(self):
        ex = pd.read_excel(datafile)
        user_info = ex[ex['Email'] == self.username]

        if not user_info.empty:
    
            print("Welcome, user! Here is your information:")
            print("Your ID:", user_info['ID'].values[0])
            print("Your Account Number:", user_info['AccountNumber'].values[0])
            print("Your Email:", user_info['Email'].values[0])
            print("Your Bank Balance:", user_info['BankBalance'].values[0])
            print("Status:", user_info['Status'].values[0])
        else:
            print("User information not found.")

    def credit(self):
        ex = pd.read_excel(datafile)
        
        user_info = ex[ex['Email'] == self.username]
        self.credit=int(input("Enter Credit Amount: "))
        currentamount =  ex['BankBalance'].values[0]
        self.totalcredit = self.credit+currentamount
        # user = pd.DataFrame([[self.totalcredit]],columns=['BankBalance'])
        ex.loc[ex['Email'] == self.username, 'BankBalance'] = self.totalcredit

        ex.to_excel(datafile, index=False)
        ex = pd.read_excel(datafile)
        print("------------------------------------------")
        print("Amount Credit Successfully!\n")
        print("Available Balance:",ex['BankBalance'].values[0])
        print("------------------------------------------")
        
            
    def debit(self):
        ex = pd.read_excel(datafile)
        if ex['BankBalance'].values != 0:
            self.debit=int(input("Enter Debit Amount: "))
            currentamount =  ex['BankBalance'].values[0]
            self.totalcredit = currentamount-self.debit
            # user = pd.DataFrame([[self.totalcredit]],columns=['BankBalance'])
            ex.loc[ex['Email'] == self.username, 'BankBalance'] = self.totalcredit

            # Save the updated DataFrame back to the Excel file
            ex.to_excel(datafile, index=False)
            ex = pd.read_excel(datafile)
            print("------------------------------------------")
            print("Amount Debit Successfully!\n")
            print("Available Balance:",ex['BankBalance'].values[0])
            print("------------------------------------------")
        else:
            print("Your Balance is 0 so first credit then debit")

    def closeaccount(self):
        ex = pd.read_excel(datafile)
        self.statuschange="inactive"
        print("Are you sure you want to close your bank account?")
        choice = int(input("Enter 1 for Yes / 2 for No: "))


        if choice == 1:
            ex.loc[ex['Email'] == self.username, 'Status'] = self.statuschange
            ex.to_excel(datafile, index=False)
            print("Account Closed Successfully!\n")

def main():
    manager2 = Login()

    while True:
        print("==============================")
        print("Welcome to Bank Application")
        print("==============================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("==============================")

        i = int(input("Choose: "))

        if i == 1:
            manager2.logincheck()
        elif i == 2:
            manager2.register()
        elif i == 3:
            print("Thank You for visiting")
            break
        else:
            print("Choose a valid Option")

main()
