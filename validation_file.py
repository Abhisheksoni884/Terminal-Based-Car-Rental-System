import re
import random
import string
class Validation:
    
        
    def correct_name(self,name):
        
        flag = True
        for character in name:
            # name contain only Alphabets and space
            if not ((65 <= ord(character) <= 90) or (90 <= ord(character) <= 122) or (" " == character)) :
                return False
        return True
            

    def correct_age(self,age):
        try :
            if age < 1 and age > 200 :
                return False
            return True
        except Exception as e:
            print(e)

    def correct_email(self,email):

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(self.pattern, email):
            return False
        return True
    

    def correct_phone_number(self,phone_no):
        if len(str(phone_no)) == 10:
            return True
        else:
            print("Contact Number should be exact 10 numbers.")


    def correct_password(self,password):
        while True:
            if (len(password) < 8):
                print("Please enter more than 8 characters in the password field.")
                return False
            elif not re.search(r"[a-z]" , password):
                print("Password must contain atleast one lowercase letter. [Hint: a, b,c]")
                return False
            elif not re.search(r"[0-9]", password):
                print("Password must contain  atleast one digit. [Hint : 1,2,3]")
                return False
            elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                print("Password must contain atleast one special character. [Hint: @,!,#]")
                return False
            return True 

    def correct_license_number(self,license_no):
        pattern = ("^(([A-Z]{2}[0-9]{2})" + "( )|([A-Z]{2}-[0-9]" + "{2}))((19|20)[0-9]" + "[0-9])[0-9]{7}$")
    
        p = re.compile(pattern)
    
        # If the string is empty 
        if (license_no == None):
            return False
    
        if(re.search(p, license_no)):
            return True
        else:
            return False 


    def correct_puc_date(self,date):
        
        pattern_str = r'^\d{2}-\d{2}-\d{4}$'
        if re.match(pattern_str, date):
            return True
        return False
        pass

    def get_number_plate(self):

    
        part1 = ''.join(random.choices(string.ascii_uppercase, k =2))
        
        part2 = ''.join(random.choices(string.digits,k = 2))

        part3 = ''.join(random.choices(string.ascii_uppercase, k =2))
        
        part4 = ''.join(random.choices(string.digits,k = 4))
        

        # Combine all parts to form the number plate
        number_plate = part1 + part2 + part3 + part4
        return number_plate


    def correct_numeric(self, num):
        if num > 0:
            return True
        return False

    def correct_model(self,name):
        flag = True
        for character in name:
            # name contain only Alphabets and space
            if not ((65 <= ord(character) <= 90) or (90 <= ord(character) <= 122) or (" " == character) or ("0" <= character <= "9" )) :
                return False
        return True
    
    def correct_date(self,date):

        pattern_str = r'^\d{2}-\d{2}-\d{4}$'
        if re.match(pattern_str, date):
            return True
        return False
    
if __name__ == '__main__':

    validate_obj = Validation()