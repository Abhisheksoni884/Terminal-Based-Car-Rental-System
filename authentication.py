import psycopg2
from connection_file import DBMS_connection
from validation_file import Validation
import query_file
import car_renatal_constant

class Authentication:

	def __init__(self):
		self.connection = DBMS_connection()
		self.validate = Validation()

	def get_role(self, email, password):
		"""
		This function is used for get the role id of the user by using their email and password
		"""
		try:
			query = query_file.GET_ROLE_ID
			role = self.connection.execute_fetch_one(query,(email, password))
			return role	
			
		except Exception as error:
			print(f"{error}")

	def login_user(self):

		"""
		This function is used for get the email and password from the user for authentication
		"""
		while True:
			
			email = input(car_renatal_constant.ENTER_EMAIL_MSG)
			password = input(car_renatal_constant.ENTER_PASSWORD_MSG)
				
			try:
				user_info = self.get_role(email, password)
				if user_info == 1:
					return "Admin"
				elif user_info == 2:
					return email, "Customer"
				else:
					print(car_renatal_constant.INVALID_CREDENTIALS)

			except Exception as error:
				print(f"{error}")
				return None




