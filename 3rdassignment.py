from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from datetime import datetime


try:
     uri = "mongodb://localhost:27017" 
     client = MongoClient(uri)
     db = client['Demo'] 
     collection = db['Data']
     collectionj = db['jobDesc'] 
      
     #print("connection successful!")
     
except ConnectionFailure as e:
        print("Could not connect to MongoDB: {e}")
        
def Register():
      Username = input("Enter Your Username ")
      email = input("Enter your Email ")
      Password = input("Enter your Password ")
      Mobile = input("Enter your mobile Numbe ")
      address = input("Enter you address ")

      user_document = {
        "username": Username,
        "email": email,
        "password": Password,
        "mobile": Mobile,
        "address": address,
        "user_type": "user" 
    }
      
      user = collection.find_one({"email":email})
      if user:
            print("User is allready exist Try to login")
      else:
        result = collection.insert_one(user_document)
        print("Registration successful!!!")

def candiatedash():
     print("")

# def viewbyid(jobid):
     
#      print(jobid)

#      job = collectionj.find_one({},{"title":1})
#      newtitle = input("Enter new title ")
#      for i in job:
#           print("Job Title:", newtitle)

def updatejob(jobid):
       
        # viewbyid(jobid)

       title = input("Enter job title ")
       desc = input("Enter job description ")
       department = input("enter department ")
       Location = input("Enter location ")
       empoyment_Type = input("Enter employment Type ")
       Salary = input("Enter Salary ")
       Appliation_Deadline = input("Enter Date and time to set deadline ")
       ReSkills = input("Enter required skills and Experience ")
       AddInfo = input("Enter any benefits and perks ")
       current_date = datetime.today().strftime("%Y-%m-%d")

       update_data = {
            
        "title":title,
         "desc":desc,
         "department":department,
         "location":Location,
         "emptype":empoyment_Type,
         "salary":Salary,
         "deadline":Appliation_Deadline,
         "ReSkills":ReSkills,
         "benefits":AddInfo,
         "created_at": current_date

            
       }
       try:
            result = collectionj.update_one({"_id": jobid}, {"$set": update_data})
            if result.modified_count > 0:
                print("Data Updated!!!")
            else:
                 print("Not updated!!")

            
       except Exception as e:
             
                print("An error occurred during the update:", e)
            

def viewjobs():
    jobs = collectionj.find({}, {"_id": 1, "title": 1, "department": 1, "location": 1, "ReSkills": 1,"created_at":1})
      
    for job in jobs:
        posted_date = job.get('created_at', 'N/A') 
        print("Job Id:",job.get("_id"))
        print("Job Title:", job.get("title"))
        print("Department:", job.get('department', 'N/A'))
        print("Location:", job.get('location', 'N/A'))
        print("Required Skills:", job.get('ReSkills', 'N/A'))
        print("Posted Date:", posted_date)
        print()
    
    print("Want to Update any Job Details")
    while True:
         
        print("1:Update Job")
        print("2:Job Status update")
        print("3:Exit")

        choice = int(input("Enter your Choice "))

        if choice == 1:
             jobid = input("Enter respective job Id ")

             updatejob(jobid)
        elif choice == 2:
             jobid = input("Enter respective job Id ")
          #    updatestatus(jobid)
        elif choice == 3:
             break
        else:
             print("Enter valid input")
        




def postjob():
     
     title = input("Enter job title ")
     desc = input("Enter job description ")
     department = input("enter department ")
     Location = input("Enter location ")
     empoyment_Type = input("Enter employment Type ")
     Salary = input("Enter Salary ")
     Appliation_Deadline = input("Enter Date and time to set deadline ")
     ReSkills = input("Enter required skills and Experience ")
     AddInfo = input("Enter any benefits and perks ")

     current_date = datetime.today().strftime("%Y-%m-%d")

     jobData = {
         "title":title,
         "desc":desc,
         "department":department,
         "location":Location,
         "emptype":empoyment_Type,
         "salary":Salary,
         "deadline":Appliation_Deadline,
         "ReSkills":ReSkills,
         "benefits":AddInfo,
         "created_at": current_date

    }
     collectionj.insert_one(jobData)
     print("Job Post successfully!")

def AdminDash():
     while True:
          
        print("Welcome to Admin Dashboard!!!")
        print("")
        print("1:view Jobs")
        print("2:Post Job")
        print("3:View Candidate")
        print("4:EXIT")

        choice = int(input("Enter you choice "))

        if choice == 1:
             viewjobs()

        elif choice == 2:
             postjob()
        

def Login():
     email = input("Enter your mailId ")
     password = input("Enter you Password ")

     user = collection.find_one({"email":email,"password":password})

     if user:
          #print("Data found")
          user_type = user.get("user_type")
          print(user_type)

          if user_type == "Admin":
               AdminDash()
               #print("Admin dashboar")
          else:
               print("Candidate Dashboard")
               
     else:
          print("Data not found")

while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Login()
            #print("Login function called")
        elif choice == 2:
              Register()
              #print("Register function called")
        elif choice == 3:
            break
        else:
            print("Invalid input!!!")

