import os 
import json
import datetime
class Customer:
    def __init__(self,name="",cnic="",amount=""):
        self.name=name
        self.cnic=cnic
        self.amount=amount

# 1) Create New Customer
    def Save_Customer_Info(self):
        Customer_account_in_string=(round(datetime.datetime.now().timestamp()))
        New_Customer={
            "Customer_Name": self.name,
            "Customer_Account_No":str(Customer_account_in_string),
            "Customer_Cnic": self.cnic,
            "Customer_Amount": self.amount,
            "Created_Time": datetime.datetime.now().isoformat()
        }
        if os.path.getsize("Data.json")>0:
            file_in_read_mode=open("Data.json","r")
            file_content=file_in_read_mode.read()
            parsed_content=json.loads(file_content)
            parsed_content.append(New_Customer)
            file_in_read_mode.close()
            file_in_writing_mode=open("Data.json","w")
            string_content=json.dumps(parsed_content)
            file_in_writing_mode.write(string_content)
            file_in_writing_mode.close()
        else:
            file_in_writing_mode = open("Data.json","w")
            string_content=json.dumps([New_Customer])
            file_in_writing_mode.write(string_content)
            file_in_writing_mode.close()
    
# 2) Search Customer
    def Search_Customer(self,Search_c):
        file_in_read_mode=open("Data.json","r")
        file_content=file_in_read_mode.read()
        Customers=json.loads(file_content)
        for customer in Customers:
            if customer["Customer_Name"].upper()==Search_c.upper():
                return customer
        return ("Customer not found.")

# 3) Delete Customer
    def Delete_Customer(self,User_Identification):
        if os.path.getsize('Data.json') > 0:
           file_in_read_mode = open('Data.json', 'r')
           file_content = file_in_read_mode.read()
           customers = json.loads(file_content)
           file_in_read_mode.close()
           for i in range(len(customers)):
               if customers[i]['Customer_Account_No'] == User_Identification or customers[i]['Customer_Name'].upper() == User_Identification.upper():
                   del customers[i]  
           file_in_write_mode = open('Data.json', 'w')
           file_in_write_mode.write(json.dumps(customers))
           file_in_write_mode.close()
           print('Customer has been deleted')



# 4) Update Information
    def Update_Information(self,User_Identification="",update=""):
        if os.path.getsize('Data.json') > 0 :
            file_r = open('Data.json', 'r')    
            custumers = json.loads(file_r.read())
            file_r.close()
            for custumer in range(len(custumers)) :
                if custumers[custumer]['Customer_Name'].upper() == User_Identification.upper():
                    del custumers[custumer]
            file_w = open('Data.json', 'w')
            file = file_w.write(json.dumps(custumers))
            file_w.close()
            file_ru = open('Data.json' , 'r')
            info = json.loads(file_ru.read())
            info.append(update) 
            file_ru.close()
            file_wu = open('Data.json' , 'w')
            file_wu.write(json.dumps(info))
            file_wu.close()
        print("Account Updated successfully.")

            


# 5) Display All Information
    def Display_Info(self):
        if os.path.getsize("Data.json")>0:
            file_in_read_mode=open("Data.json","r")
            file_content= file_in_read_mode.read()
            parsed_content=json.loads(file_content)
            print(parsed_content)
            file_in_read_mode.close()
        else:
            print("No Data found inside the record.")