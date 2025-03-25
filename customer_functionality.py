import car_renatal_constant
from validation_file import Validation
import query_file
from connection_file import DBMS_connection
from admin_functionality import Admin, Customer_management, Bill_management
from prettytable import PrettyTable
from authentication import Authentication
import subprocess

class Customer:

    def __init__(self):
        self.connection = DBMS_connection()
        self.validate = Validation()
        self.query_table = query_file
        self.admin = Admin()
        self.customer_manage = Customer_management()
        self.authenticate = Authentication()

class Customer_profile(Customer):
    """
    This function is used for profile management in which customer update and view their data
    """

    def __init__(self):
        super().__init__()
        
    def update_customer_data(self):
        """
        This function is used for update profile in which it update their password
        """
        
        customer_id = self.admin.get_customer_id()
        while True:
            new_password = input(car_renatal_constant.ASK_ENTER_PASSWORD)
            if self.validate.correct_password(new_password):
                break
    
        try: 
            query = self.query_table.UPDATE_CUSTOMER_PASSWORD_QUERY
            self.connection.execute_query(query,(new_password,customer_id))
            print(car_renatal_constant.SUCCESSFUL)
            
        except Exception as e:
            print(e)


    def view_customer_data(self):
        """
        This function is used for viewing customer data
        """
        
        customer_id = self.admin.get_customer_id()
        print(customer_id)
        try:
            query = self.query_table.VIEW_CUSTOMER_DATA_QUERY
            
            data = self.connection.execute_fetch_all(query,(customer_id,))
            print(data)

            table = PrettyTable(['Id', 'Name', 'Email', 'Phone_number', 'Address', 'Age', 'Password'])
            for column in data:
                table.add_row([column[0],column[2],column[3],column[4],column[5],column[6],column[7]])
            print(table)

        except Exception as e:
            print(e)


class Customer_car_management(Customer):
    def __init__(self):
        super().__init__()
        self.total_amount = 0
        
    def choose_car(self):
        """
        This function is used for choosing the car by the customer in which it ask car brand and model , location, start_date , end_date and their license number.
        """
        while True:
            print(car_renatal_constant.OPTION_FOR_NEW_USER)

            try:
                choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if choice == 1: 
                    user_id = self.customer_manage.registration()
                    break
                elif choice == 2:
                    email, type  = self.authenticate.login_user()

                    if type == "Customer" :
                        query = self.query_table.GET_CUSTOMER_ID_BY_EMAIL
                        
                        user_id = self.connection.execute_fetch_one(query, (email,))
                        print(car_renatal_constant.MSG_OF_CUSTOMER_ID, user_id)
                        break

                elif choice == 0:
                    customer_main()
                else:
                    print(car_renatal_constant.WRONG_NUMBER_CHOICE)
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)


        
        Data = self.connection.execute_fetch_all(self.query_table.SHOW_BRAND_QUERY)

        Table = PrettyTable(["id","Brand", "Variant"])
        for Column in Data :
            Table.add_row([Column[0],Column[2],Column[3]])
        print(Table)

        brand_id = self.admin.get_brand_id()
        query = self.query_table.SHOW_MODELS_OF_CAR
        
        data = self.connection.execute_fetch_all(query,(brand_id,))

        table = PrettyTable(["id","Model" , "Color" , "Number plate",  "Rent"  ,"Puc_end_date" , "Insaurance_end_date"])
        for column in data :
            table.add_row([column[0],column[2],column[3],column[4],column[5],column[7],column[8]])
        print(table)
    
        model_id = self.admin.get_model_id()

        while True:
            
            location = input(car_renatal_constant.ASK_ENTER_LOCATION)
            if self.validate.correct_name(location):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)


        while True:
            
            start_date = input(car_renatal_constant.ASK_ENTER_START_DATE)
            if self.validate.correct_date(start_date):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        while True:
            
            end_date = input(car_renatal_constant.ASK_ENTER_RETURN_DATE)
            if self.validate.correct_date(end_date):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        while True:
           
            license_number = input(car_renatal_constant.ASK_ENTER_LICENSE)
            if self.validate.correct_license_number(license_number):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        while True:
            try:
                print(car_renatal_constant.OPTION_FOR_PAYMENT_STATUS)

                num =int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if num == 1:
                    amount = self.admin.get_total_money(model_id,start_date,end_date)
                    print(amount)
                    payment_status = "Paid"
                    break

                elif num == 2:
                    amount = self.admin.get_total_money(model_id,start_date,end_date)
                    print(amount)
                    payment_status = "Pending"        
                    break

                else:
                    print(car_renatal_constant.WRONG_NUMBER_CHOICE)
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
            
        try:
        
            query = self.query_table.INSERT_CUSTOMER_DATA_INTO_CAR_RENTAL_TABLE
            self.connection.execute_query(query,(user_id,model_id,location,license_number,start_date,end_date,payment_status))
            print(car_renatal_constant.SUCCESSFUL)

            query = self.query_table.GET_RENTAL_ID_AFTER_SELECTION
            
            rental_id = self.connection.execute_fetch_one(query,(user_id,model_id))
            
            print(car_renatal_constant.MSG_OF_RENTAL_ID,rental_id)
            
            query = self.query_table.INSERT_INTO_BILL_DATA
            self.connection.execute_query(query, (rental_id,amount))
            print(car_renatal_constant.SUCCESSFUL)

            query = self.query_table.GET_BILL_ID_AFTER_SELECTION
            bill_id = self.connection.execute_fetch_one(query, (rental_id,))
            print(car_renatal_constant.MSG_OF_BILL_ID,bill_id)

        except Exception as e:
            print(e)

        while True :
            try:
                print(car_renatal_constant.OPTION_AFTER_SELECT_CAR)
                choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if choice == 1:
                    self.choose_car()
                elif choice == 0 :
                    print(car_renatal_constant.THANK_YOU_MSG)
                    break
                else:
                    print(car_renatal_constant.WRONG_INPUT)
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)


    
    def return_car(self):

        self.connection.connect_connection()
        customer_id = self.admin.get_customer_id()
        rental_id = self.admin.get_rental_id()

        try:
            
            query = self.query_table.UPDATE_BOOKING_STATUS_PENDING
            self.connection.execute_query(query,(customer_id,))
            query = self.query_table.UPDATE_PAYMENT_STATUS_DONE
            self.connection.execute_query(query,(rental_id,))
            print(car_renatal_constant.SUCCESSFUL)

            print(car_renatal_constant.OPTION_FOR_ANOTHER_CAR_RETURN)
            while True:
                try:
                    choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                    if choice == 1:
                        self.return_car()
                    elif choice == 0:
                        return
                    else:
                        print(car_renatal_constant.WRONG_INPUT)
                except ValueError:
                    print(car_renatal_constant.VALUEERROR_MSG)
     
        except Exception as e:
            print(e)

    def extend_return_date(self):  

        customer_id = self.admin.get_customer_id()
        while True:
            new_date = input(car_renatal_constant.ASK_ENTER_RETURN_DATE)
            if self.validate.correct_date(new_date):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        try:
            query = self.query_table.UPDATE_RETURN_DATE
            self.connection.execute_query(query,(new_date, customer_id))
            print(car_renatal_constant.SUCCESSFUL)
            
        except Exception as e:
            print(e)

class Customer_Feedback(Customer):

    def __init__(self):
        super().__init__()
        pass

    def add_feedback(self):

        while True:
            name = input(car_renatal_constant.ASK_ENTER_NAME)
            if self.validate.correct_name(name):
                break
            else:
                print(car_renatal_constant.WRONG_INPUT)

        new_feedback = input(car_renatal_constant.ASK_ENTER_FEEDBACK)
    
        try:
            query = self.query_table.ADD_FEEDBACK_QUERY
            self.connection.execute_query(query,(name,new_feedback))
            print(car_renatal_constant.SUCCESSFUL)
            
        except Exception as e:
            print(e)

    def view_feedback(self):
        
        
        feedback_id = self.admin.get_feedback_id()
        try:
            query = self.query_table.VIEW_CUSTOMER_FEEDBACK_QUERY
            data = self.connection.execute_fetch_all(query,(feedback_id,))
            table = PrettyTable(['id','Name','Feedback'])
            for column in data:
                table.add_row([column[0],column[1],column[2]])
            print(table)
            
        except Exception as e:
            print(e)



def customer_main():

    while True:
        print(car_renatal_constant.SHOW_OPTION_TO_CUSTOMER)
        try:
            choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))

            if choice == 1:
                Customer_car_management().choose_car()

            elif choice == 2:
                Customer_car_management().return_car()

            elif choice == 3 :
                Customer_profile().view_customer_data()

            elif choice == 4:
                Customer_profile().update_customer_data()
            
            elif choice == 5 :
                Customer_car_management().extend_return_date()

            elif choice == 6 :
                Customer_Feedback().add_feedback()

            elif choice == 7 :
                Customer_Feedback().view_feedback()

            elif choice == 8 :
                Bill_management().view_bill()

            elif choice == 0:
                subprocess.run(['python', 'main.py'])
            else:
                print(car_renatal_constant.WRONG_NUMBER_CHOICE)
        except ValueError:
            print(car_renatal_constant.VALUEERROR_MSG)
