import car_renatal_constant
from validation_file import Validation
from connection_file import DBMS_connection
import query_file
from prettytable import PrettyTable
from datetime import datetime
import subprocess

class Admin:
    def __init__(self):
        self.validate = Validation()
        self.connection = DBMS_connection()
        self.query_table = query_file

    def get_model_id(self):
        """
        This function is used for return a model_id
        """
        self.connection.connect_connection()
        while True:    
            try :
                model_id = int(input(car_renatal_constant.ASK_ENTER_MODEL_ID))
                if self.validate.correct_numeric(model_id):
                    break
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)

        return model_id
    
    def get_customer_id(self):
        """
        This function is used for return a customer id
        """
        self.connection.connect_connection()
        while True:
            try:
                customer_id = int(input(car_renatal_constant.ASK_CUSTOMER_ID))
                if self.validate.correct_numeric(customer_id):
                    break
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
        return customer_id 
    
    def get_bill_id(self):
        """
        This function is used for return a bill id
        """
        self.connection.connect_connection()
        while  True:
            try:
                bill_id = int(input(car_renatal_constant.ASK_BILL_ID))
                if self.validate.correct_numeric(bill_id):
                    break
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
        return bill_id

    def get_feedback_id(self):
        """
        This function is used for return a feedback id
        """
        self.connection.connect_connection()
        while True:
            try:
                feedback_id = int(input(car_renatal_constant.ASK_FEEDBACK_ID))
                if self.validate.correct_numeric(feedback_id):
                    break
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
        return feedback_id
    
    def get_rental_id(self):
        """
        This function is used for return a car rental id
        """
        self.connection.connect_connection()
        while True:
            try:

                rental_id = int(input(car_renatal_constant.ASK_ENTER_RENTAL_ID))
                if self.validate.correct_numeric(rental_id):
                    break
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
        return rental_id
    
    def get_brand_id(self):
        """
        This function is used for return a car brand id
        """
        self.connection.connect_connection()
        while True:
            try:
                brand_id = int(input(car_renatal_constant.ASK_BRAND_ID))
                if self.validate.correct_numeric(brand_id):
                    break
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
        return brand_id
    
    def get_total_money(self,id,d1,d2):
        """
        This function is used for return a total amount that have to pay 
        """
        d1 = datetime.strptime(d1, "%d-%m-%Y")
        d2 = datetime.strptime(d2, "%d-%m-%Y")
        differnce = abs((d2 - d1).days)

        differnce += 1
        
        query = self.query_table.GET_THE_RENT_OF_CARS
        
        rent = self.connection.execute_fetch_one(query, (id,))
        return differnce*rent
    

    def view_all_cars(self):
        """
        This function is used for show all the cars
        """

        query = self.query_table.VIEW_CATEGORY_TABLE
        
        car_data = self.connection.execute_fetch_all(query)
        table = PrettyTable(['Model_id','Brand_id', 'Model_name', 'Color', 'Number_plate','Rent','Booking_status', 'Puc_end_date', 'Insaurance_end_date'])
        for column in car_data:
            table.add_row([column[0],column[1],column[2],column[3],column[4],column[5],column[6],column[7],column[8]])
        print(table)


    def view_all_brands(self):
        """
        This function is used for show all brands of the car
        """

        query = self.query_table.VIEW_BRAND_DATA
        brand_data = self.connection.execute_fetch_all(query)

        table = PrettyTable(['id','Brand', 'Variant'])

        for column in brand_data:
            table.add_row([column[0],column[2],column[3]])
        print(table)
        

    def view_all_customers(self):
        """
        This funtion is used for show all the customers and their details
        """
        query = self.query_table.VIEW_ALL_CUSTOMER
        customers_data = self.connection.execute_fetch_all(query)
        table = PrettyTable(['id','Name','email','Phone Number','Adress','Age','Password'])
        for column in customers_data:
            table.add_row([column[0],column[2],column[3],column[4],column[5],column[6],column[7]])
        print(table)


    def view_all_feedback(self):
        """
        This function is used for view all the feedback of the persons
        """

        query = self.query_table.VIEW_ALL_FEEDBACK
        customers_data = self.connection.execute_fetch_all(query)
        table = PrettyTable(['id','Name','Review'])
        for column in customers_data:
            table.add_row([column[0],column[1],column[2]])
        print(table)

class Car_management(Admin):
    def __init__(self):
        super().__init__()


    def add_brand(self):
        """
        This function is used for adding a new car brand and variant in the CAR Table
        """
        self.view_all_brands()
        while True:
            new_brand = input(car_renatal_constant.ASK_NEW_BRAND_NAME)
            if self.validate.correct_name(new_brand):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)
                
        new_variant = input(car_renatal_constant.ASK_NEW_VARIANT_NAME)
            
        try:
            query = self.query_table.INSERT_NEW_CAR_DATA_QUERY
            self.connection.execute_query(query,(new_brand,new_variant))
            print(car_renatal_constant.ADD_BRAND_SUCCESSFUL_MSG)
        except Exception as e:
            print(e)


    def add_car_category(self):
        """
        This function is used for adding a new model of car in which it requires the brand id , color, model name,
        number plate , puc end date , rent of car, insaurance end date
        """

        brand_id = Admin().get_brand_id()
        while True:
            new_color = input(car_renatal_constant.ASK_NEW_COLOR_NAME)
            if self.validate.correct_name(new_color):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        while True:
            new_model = input(car_renatal_constant.ASK_NEW_MODEL_NAME)
            if self.validate.correct_model(new_model):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)
        
        while True:
            puc_end_date = input(car_renatal_constant.ASK_NEW_PUC_END_DATE)
            if self.validate.correct_puc_date(puc_end_date):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        while True:
            insaurance_end_date = input(car_renatal_constant.ASK_NEW_CAR_INSAURANCE)
            if self.validate.correct_puc_date(insaurance_end_date):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)
        

        number_plate = self.validate.get_number_plate()

        while True:
            try :
                rent = int(input(car_renatal_constant.ASK_INSERT_RENT))
                if self.validate.correct_numeric(rent):
                    break
                else:
                    print(car_renatal_constant.WRONG_INPUT)
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)

        try:
            query = self.query_table.INSERT_NEW_CATEGORY_QUERY
            self.connection.execute_query(query,(brand_id, new_model, new_color, number_plate, rent, puc_end_date, insaurance_end_date))
            print(car_renatal_constant.SUCCESSFUL)

        except Exception as e:
            print(e)

        

    def update_car(self):
        """
        This function is used for update car details like puc end date and insaurance end date
        """

        self.view_all_cars()
        print(car_renatal_constant.OPTION_FOR_UPDATE_CAR)
        
        choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
        if choice == 1:

            model_id = Admin().get_model_id()
            while True:
                new_puc_end_date = input(car_renatal_constant.ASK_NEW_PUC_END_DATE)
                if self.validate.correct_puc_date(new_puc_end_date):
                    break 
                else:
                    print(car_renatal_constant.WRONG_INPUT)

            try:
                query = self.query_table.UPDATE_PUC_END_DATE
                self.connection.execute_query(query,(new_puc_end_date,model_id))
                print(car_renatal_constant.SUCCESSFUL)

            except Exception as e:
                print(e)


        elif choice == 2:
            while True :
                model_id = Admin().get_model_id()
                new_insaurance_date = input(car_renatal_constant.ASK_NEW_CAR_INSAURANCE)
                if self.validate.correct_date(new_insaurance_date):
                    break
                else:
                    print(car_renatal_constant.WRONG_INPUT)
            try:
                
                query = self.query_table.UPDATE_INSAURANCE_END_DATE
                self.connection.execute_query(query,(new_insaurance_date,model_id))
                print(car_renatal_constant.SUCCESSFUL)

            except Exception as e:
                print(e)


        elif choice == 0 :
            admin_main()
        else:
            print(car_renatal_constant.WRONG_NUMBER_CHOICE)


    def view_car(self):
        """
        This function is used for showing the model of the car
        """
        self.view_all_cars()
        model_id = Admin().get_model_id()
        try:
            query = self.query_table.VIEW_MODEL_DATA_QUERY
            data = self.connection.execute_fetch_all(query,(model_id,))
            table = PrettyTable(["Brand","variant","Model" , "Color" ,  "Number plate",  "Rent"  ,"Booking status", "Puc_end_date" , "Insaurance_end_date"])
            for column in data :
                table.add_row([column[0],column[1], column[2],column[3],column[4],column[5],column[6],column[7],column[8]])
            print(table)

        except Exception as e:
            print(e)


    def delete_car_brand(self):
        """
        This function is used for deleting a model of the car
        """

        self.view_all_brands()
        brand_id = Admin().get_model_id()

        try:
            query = self.query_table.DELETE_BRAND_QUERY
            self.connection.execute_query(query,(brand_id,))
            print(car_renatal_constant.DELETE_BRAND_SUCCESSFUL_MSG)

        except Exception as e:
            print(e)
  

    
    def delete_car_category(self):
        """
        This function is used for deleting a model of the car
        """
        self.view_all_cars()
        model_id = Admin().get_model_id()

        try:
            query = self.query_table.DELETE_CATEGORY_QUERY
            self.connection.execute_query(query,(model_id,))
            print(car_renatal_constant.DELETE_CATEGORY_SUCCESSFUL)

        except Exception as e:
            print(e)
        
        
class Customer_management(Admin):

    def __init__(self):
        super().__init__()


    def registration(self):
        """
        This function is used for inserting the customer details into the user table in which it takes the 
        customer name, age,email, address,phone number and password
        
        """
        while True:
            name = input(car_renatal_constant.ASK_ENTER_NAME)
            if self.validate.correct_name(name):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        while True:
            try :
                age = int(input(car_renatal_constant.ASK_ENTER_AGE))
                if self.validate.correct_age(age):
                    break
                else:
                    print(car_renatal_constant.WRONG_INPUT)
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
        
        while True:
            email = input(car_renatal_constant.ASK_ENTER_EMAIL)
            if self.validate.correct_email(email):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        while True: 
            try:
                phone_number = int(input(car_renatal_constant.ASK_ENTER_PHONE_NUMBER))
                if self.validate.correct_phone_number(phone_number):
                    break
                else:
                    print(car_renatal_constant.WRONG_INPUT)
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
        
        while True:
            password = input(car_renatal_constant.ASK_ENTER_PASSWORD)
            if self.validate.correct_password(password):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        address = input(car_renatal_constant.ASK_ENTER_ADDRESS)

    
        try:
            query = self.query_table.INSERT_CUSTOMER_DATA_QUERY
            self.connection.execute_query(query, (name,email,phone_number,address,age,password))
            print(car_renatal_constant.SUCCESSFUL)

            query = self.query_table.GET_CUSTOMER_ID
            customer_id = self.connection.execute_fetch_one(query,(email,))
            print(car_renatal_constant.MSG_OF_CUSTOMER_ID,customer_id)
            return customer_id
            
        except Exception as e:
            print(e)


    def view_customer(self):
        """
        This function is used for viewing the customer data

        """
        self.view_all_customers()
        customer_id = Admin().get_customer_id()
        try:
            
            query = self.query_table.VIEW_CUSTOMER_DATA_QUERY
            
            data = self.connection.execute_fetch_all(query,(customer_id,))

            table = PrettyTable(['Id', 'Name', 'Email', 'Phone_number', 'Address', 'Age', 'Password'])
            for column in data:
                table.add_row([column[0],column[2],column[3],column[4],column[5],column[6],column[7]])
            print(table)

        except Exception as e:
            print(e)



    def delete_customer(self):
        """
        This function is used for deleting a customer record from the user table
        """
        customer_id = Admin().get_customer_id()

        try:
            query = self.query_table.DELETE_CUSTOMER_DATA_QUERY
            self.connection.execute_query(query,(customer_id,))
            print(car_renatal_constant.DELETE_CUSTOMER_SUCCESSFUL)
            
        except Exception as e:
            print(e)



class Bill_management(Admin):
    """
    This class manage bill management in which it has function of showing bill
    """
    def __init__(self):
        super().__init__()

    def view_bill(self):
        """
        This function is used for show bill to customer by admin
        """

        customer_id = self.get_customer_id()
        try:
            query = self.query_table.VIEW_CUSTOMER_BILL_QUERY
            
            data = self.connection.execute_fetch_all(query,(customer_id,))

            table = PrettyTable(['Bill id','Name','Brand','Variant','Model','Color','Rent','Assign_date', 'Return_date','Payment_status','Total_amount'])
            for column in data :
                table.add_row([column[0],column[1],column[2],column[3],column[4],column[5],column[6],column[7],column[8],column[9],column[10]])
            print(table)
            
        except Exception as e:
            print(e)

    
    
class Feedback_management(Admin):
    def __init__(self):
        super().__init__()

    def view_feedback(self):
        """
        This function is used for view feedback given by the customer
        """
        self.view_all_feedback()
        
        feedback_id = Admin().get_feedback_id()
        try:
            query = self.query_table.VIEW_CUSTOMER_FEEDBACK_QUERY
            
            data = self.connection.execute_fetch_all(query,(feedback_id,))

            table = PrettyTable(['id','Name','Feedback'])
            for column in data:
                table.add_row([column[0],column[1],column[2]])
                
            print(table)
            
        except Exception as e:
            print(e)

    


def admin_main():        
    """
    Admin functionality start from here 
    """
    print(car_renatal_constant.SHOW_OPTION_TO_ADMIN)
    choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
    try :

        if choice == 1:
            # for Car Management

            while True:
                print(car_renatal_constant.OPTION_FOR_CAR)
                choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if choice == 1:
                    Car_management().add_brand()
                if choice == 2:
                    Car_management().add_car_category()
                elif choice == 3:
                    Car_management().update_car()
                elif choice == 4:
                    Car_management().view_car()
                elif choice == 5:
                    Car_management().delete_car_brand()
                elif choice == 6 :
                    Car_management().delete_car_category()
                elif choice == 0:
                    admin_main()
                else:
                    print(car_renatal_constant.WRONG_NUMBER_CHOICE)
            
        elif choice == 2:
            # for Customer Management
            while True:

        
                print(car_renatal_constant.ASK_VIEW_CUSTOMER)
                print(car_renatal_constant.ASK_DELETE_CUSTOMER)
                print(car_renatal_constant.ASK_GO_BACK)
                choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if choice == 1:
                    Customer_management().view_customer()
                elif choice == 2:
                    Customer_management().delete_customer()
                elif choice == 0:
                    admin_main()
                else:
                    print(car_renatal_constant.WRONG_NUMBER_CHOICE)

        elif choice == 3:
            # for feedback management

            while True:

                print(car_renatal_constant.ASK_VIEW_FEEDBACK)
                print(car_renatal_constant.ASK_GO_BACK)
                
                choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if choice == 1:
                    Feedback_management().view_feedback()
                elif choice == 0:
                    admin_main()
                else:
                    print(car_renatal_constant.WRONG_NUMBER_CHOICE)


        elif choice == 4:
            # for bill management
            while True:
                print(car_renatal_constant.ASK_VIEW_BILL)
                print(car_renatal_constant.ASK_GO_BACK)
                choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if choice == 1:
                    Bill_management().view_bill()
                elif choice == 0:
                    admin_main()
                else:
                    print(car_renatal_constant.WRONG_NUMBER_CHOICE)

        elif choice == 0:
            subprocess.run(['python', 'main.py'])
        else:
            print(car_renatal_constant.WRONG_NUMBER_CHOICE)
    except ValueError:
        print(car_renatal_constant.VALUEERROR_MSG)
        admin_main()
