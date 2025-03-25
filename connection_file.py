import psycopg2

class DBMS_connection:

	def __init__(self):
		self.conn = None
		self.cur = None

	def connect_connection(self):
		"""
		This function is used for set up the connection with the postgres Database and it opens the connection 
		"""
		try:
			self.conn = psycopg2.connect(
				host = "localhost",
				dbname = "car_rental_system",
				user = "postgres",
				password = "Abhishek_08",
				port = 5432)
			
			self.cur = self.conn.cursor()
		except Exception as error:
			print(f"{error}")

	def disconnect_connection(self):
		"""
		This function is used for close the connection with the database 
		"""
		if self.cur:
			self.cur.close()
		if self.conn:
			self.conn.close()

	def execute_fetch_one(self,query,parameters = None):
		"""
		This function is used for execute the query and return a single value in which takes the tuple list in the 'parameters' argument 

		"""
		self.connect_connection()
		self.cur.execute(query, parameters)
		data = self.cur.fetchone()[0]
		self.conn.commit()
		return data

	def execute_fetch_all(self,query,parameters = None):
		"""
		This function is used for execute the query and return a multiple values in which takes the tuple list in the 'parameters' argument 
		"""
		self.connect_connection()
		self.cur.execute(query, parameters)
		data = self.cur.fetchall()
		self.conn.commit()
		return data
	
	def execute_query(self,query,parameters = None):
		"""
		This function is used for execute the query in which takes the tuple list in the 'parameters' argument 
		"""
		self.connect_connection()
		self.cur.execute(query,parameters)
		self.conn.commit()
		
