from customer import Customer
import os
import datetime
def Options():
    print("--Options--")
    print("1) Add Customer")
    print("2) Search Customer")
    print("3) Delete Customer")
    print("4) Update Customer")
    print("5) Display Info")
    print("6) Clear Screen")
    print("7) Exit Application")
    print("--------------------------------------")

while True:
    Options()
    Choice= (input("Enter Option Number: "))

    if Choice == "1":
        Enter_customer_name=input("Enter Customer Name: ")
        Enter_customer_CNIC=input("Enter Customer CNIC: ")
        Enter_customer_amount=input("Enter Customer amount: ")
        os.system('cls')
        Customer_Object=Customer(Enter_customer_name,Enter_customer_CNIC,Enter_customer_amount)
        Customer_Object.Save_Customer_Info()
        print("Customer Added Successfully.")
    
    
    
    elif Choice == "2":
        Search_c=input("Enter Customer Name or Account Number: ")
        os.system('cls')
        c= Customer()
        Result=c.Search_Customer(Search_c)
        print(Result)

    
    
    elif Choice == "3":
        User_Identification=input("Enter Customer Name or Account Number: ")
        os.system('cls')
        c=Customer()
        c.Delete_Customer(User_Identification)
    
    
    
    elif Choice == "4":
        User_Identification=input("Enter Customer Name: ")
        os.system('cls')
        update = {'Customer_Name' : input('Enter New Custumer name: '),
        'Customer_Cnic' : input('Enter New CNIC number: '),
        'Customer_Account_No' : int(input('Enter New Account number: ')),
        'Customer_Amount' :  input('Enter New Custumer amount : '),
        'Created_Time' : datetime.datetime.now().isoformat()                
    }
        update_info = Customer()
        update_info.Update_Information(User_Identification , update) 

    
    
    elif Choice == "5":
        os.system('cls')
        c=Customer()
        c.Display_Info()
    
    
    
    elif Choice == "6":
        os.system('cls')

    
    
    elif Choice == "7":
        Program_permission=input("Are you sure to want to close the program? Y/N: ")
        if Program_permission.upper() == "y".upper():
            print("Exiting Program...")
            break
        elif Program_permission.upper() == "n".upper():
            os.system('cls')
            continue
        else:
            os.system('cls')
            continue

    else:
        os.system('cls')
        
