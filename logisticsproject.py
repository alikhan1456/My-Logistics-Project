drivers=["Zarak", "Ahmad", "Ali", "Khan", "Muhammad"]
jobs=[]



#-----------------------------  CREAT JOB---------------------------------------------------------------------------------#
#-----------------------------  FUNCTION----------------------------------------------------------------------------------# 

def add_job():
    #________________________Pickup-Dropoff______________________________________
    def get_job_location():
        pickup_location= input("Please enter the pickup-location:")
        drop_location= input("Please enter the dropoff-location:")
        return pickup_location, drop_location

    pickup_location, drop_location= get_job_location()

    #____________________________________________________________________________


    #________________________Date-Time___________________________________________
    def get_job_datetime():
        pickup_datetime= input("Enter the pickup date and time:")
        drop_datetime= input("Enter the droppoff date and time:")
        return pickup_datetime,drop_datetime

    pickup_datetime, drop_datetime= get_job_datetime()
    #____________________________________________________________________________





    #________________________Customer Details____________________________________

    def customer_details():
        customer_name= input("Please enter the customer name:")
        customer_phone= input("Enter customer Phone number:")
        customer_email= input("Enter customer email:")
        return customer_name, customer_phone, customer_email

    customer_name,customer_phone,customer_email= customer_details()
    #____________________________________________________________________________    


    #__________________________Basic-job-info____________________________________
    def get_job_basic_info():
        job_id= input("Please enter the job id:")
        job_type= input("Enter job type, eg(House move, Cx job): ")
        weight= float(input("Enter the weight of items:"))
        notes= input("Enter Any notes here: ")
        van_type= input("Enter the van type needed by customer:")
        return job_id,job_type,weight,notes,van_type

    job_id,job_type,weight,notes,van_type= get_job_basic_info()

    #____________________________________________________________________________


    #_________________________Price-details______________________________________
    def get_price_details():
        price= int(input("Enter the price agreed: "))
        commission= (price*20)/100
        return price, commission

    price, commission= get_price_details()

    #____________________________________________________________________________




    #_______________________Assign driver or not and status______________________
    def assign_driver():
        driver= ""
        status= "Unassigned"

        question=input("Do you want the driver assigned?: ").lower()
        if question=="yes":
            driver= input("Enter the driver:")
            if driver in drivers:
                status= "Assigned"
            else: 
                driver=""
                print("The driver is not in the list")
        return driver, status

    driver, status= assign_driver()
    #____________________________________________________________________________



    job={
        "pickup":pickup_location,
        "pickup date/time": pickup_datetime,
        "dropoff":drop_location,
        "dropoff date/time": drop_datetime,
        "job id": job_id,
        "customer name": customer_name,
        "customer phone": customer_phone,
        "customer email": customer_email,
        "job type": job_type,
        "weight-items": weight,
        "notes": notes,
        "van type": van_type,
        "price": price,
        "commission": commission,
        "driver":driver,
        "status":status,

    }
        
    jobs.append(job)    
#------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------- VIEW JOB-----------------------------------------------------------------------#
#---------------------------------------------- Function-----------------------------------------------------------------------#

def view_jobs():
    if not jobs:
            print("No Jobs Available")
    else:
        for job in jobs:
            print(f"Job ID: {job['job id']}")
            print(f"Customer Name: {job['customer name']}")
            print(f"Pickup Adress: {job['pickup']}")    
            print(f"Dropp-off Address: {job['dropoff']}")
            print(f"Driver: {job['driver']}")
            print(f"Price Agreed: {job['price']}")
            print(f"Status: {job['status']}")
            print("__________________________________________")

#--------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------#


  
#__________________________Main-Menue_______________________________________________________________
flag= True
while flag==True:
    print("===== LOGISTICS MANAGEMENT SYSTEM =====")
    print("1. Add New Job")
    print("2. View Jobs")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        add_job()

    elif choice==2:
        view_jobs()
        
    elif choice==3:
        print("Exit Selected")
        flag= False 
    else: print("invalid choice")
       
#___________________________________________________________________________________________________    












         



