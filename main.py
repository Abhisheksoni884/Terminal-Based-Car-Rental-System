import car_renatal_constant
from admin_functionality import admin_main
from customer_functionality import customer_main
from authentication import Authentication
from connection_file import DBMS_connection

class Role_management:

    def __init__(self):
        self.connection = DBMS_connection()
        self.authenticate = Authentication()
        
    def main_functionality(self):
        """
        This function is used as a path for admin and customer functionality in which it requries the role
        """
        print(car_renatal_constant.ASK_ROLE_ADMIN)
        print(car_renatal_constant.ASK_ROLE_CUSTOMER)
        print(car_renatal_constant.ASK_EXIT)

        while True:
            try:
                role_choice = int(input(car_renatal_constant.ENTER_NUMBER_CHOICE))
                if role_choice == 1:
                    print("abhisheksoni123@gmail.com \nAbhishek@123")
                    type = self.authenticate.login_user()
                    if type == "Admin":
                        admin_main()

                elif role_choice == 2:
                    customer_main()

                elif role_choice == 0:
                    self.connection.disconnect_connection()
                    exit()
                else :
                    print(car_renatal_constant.WRONG_NUMBER_CHOICE)
            except ValueError:
                print(car_renatal_constant.VALUEERROR_MSG)
                
            
if __name__ == '__main__':

    role_obj = Role_management()
    role_obj.main_functionality()

