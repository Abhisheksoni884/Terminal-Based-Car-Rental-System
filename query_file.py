import psycopg2
from connection_file import DBMS_connection


CREATE_ROLE_TABLE = """
Create table if not exists Role(
id int Primary key NOT NULL,
Type VARCHAR(20) NOT NULL)
"""
CREATE_USER_TABLE = """
Create table if not exists Customer(
id SERIAL primary key NOT NULL,
Role_id INT REFERENCES Role(id) ON DELETE CASCADE,
User_name Varchar(50)NOT NULL,
Email varchar(50) NOT NULL,
Phone_number BIGINT ,  
Address VARCHAR(100),
Age int NOT NULL,
Password varchar(30) NOT NULL,
Created_by int NOT NULL,
Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
Updated_by int NOT NULL,
Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

CREATE_CAR_TABLE = """
create table if not exists Car(
id serial Primary key NOT NULL,
User_id INT REFERENCES Customer(id)ON DELETE CASCADE,
Brand_name Varchar(50) NOT NULL,
Car_variant Varchar(50), 
Created_by INT REFERENCES Customer(id),
Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
Updated_by INT REFERENCES Customer(id),
Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

CREATE_CAR_CATEGORY_TABLE = """
create table if not exists Category(
id serial primary key NOT NULL,
Brand_id int References Car(id) ON DELETE CASCADE,
Model_name varchar(20),
Color varchar(20) NOT NULL,
Number_plate Varchar(20) NOT NULL,
Rent INT ,
Booking_status Varchar(20) NOT NULL,
Puc_end_date DATE, 
Insaurance_end_date DATE,
Created_by INT REFERENCES Customer(id),
Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
Updated_by INT REFERENCES Customer(id),
Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

CREATE_FEEDBACK_TABLE = """
Create table if not exists Feedback(
id serial primary key NOT NULL,
name varchar(20) NOT NULL,
Feedback_given VARCHAR(200),
Created_by INT REFERENCES Customer(id),
Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
Updated_by INT REFERENCES Customer(id),
Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

"""


CREATE_CAR_RENTAL_TABLE ="""
create table if not exists Car_Rental_Data(
id serial primary key NOT NULL,
User_id int References Customer(id) ON DELETE CASCADE,
Model_id int References Category(id) ON DELETE CASCADE,
Location VARCHAR(20),
License VARCHAR NOT NULL,
Assign_date DATE,
Return_date DATE,
Payment_status Varchar(20),
Created_by INT REFERENCES Customer(id),
Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
Updated_by INT REFERENCES Customer(id),
Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

CREATE_EXTRA_CHARGES_TABLE = """
Create table if not exists Extra_Charges(
id serial primary key NOT NULL,
Car_rental_id int references Car_Rental_Data(ID) ON DELETE CASCADE,
Reason VARCHAR (100),
Fine int )
"""

CREATE_TABLE_BILLING = """
Create table if not exists  Billing_Data(
id serial primary key NOT NULL,
Car_rental_id int references Car_Rental_Data(Id) ON DELETE CASCADE,
Total_amount INT ,
Created_by INT REFERENCES customer(id),
Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
Updated_by INT REFERENCES customer(id),
Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

INITIAL_CUSTOMERS_DATA = """
INSERT INTO Customer (Role_id, User_name, Email, Phone_number, Address, Age, Password, Created_by, Updated_by)
VALUES
(2, 'aaquib badlapur', 'aaquibbadla123@gmail.com', 7845221639, 'H :no adhikar society', 21, 'aaquib129', 2, 1),
(2, 'rahul desai', 'rahuldesai123@gmail.com', 9123456789, '1234 Shivaji Nagar', 25, 'rahul@123', 2, 1),
(2, 'priya sharma', 'priyasharma123@gmail.com', 9876543210, 'Kishan Colony, Sector 12', 23, 'priya@abc', 2, 1),
(2, 'manish gupta', 'manishgupta123@gmail.com', 9765432101, 'Gali no. 4, Park street', 26, 'manish@789', 2, 1),
(2, 'neha kapoor', 'neha.kapoor123@gmail.com', 9977886655, 'MG Road, Room 305', 22, 'neha@xyz', 2, 1),
(2, 'raj kumar', 'rajkumar234@gmail.com', 7894561230, '2nd floor, M block', 24, 'raj@pass', 2, 1),
(2, 'seema agarwal', 'seemaagarwal123@gmail.com', 9845612345, 'Windsor Palace, Flat 10', 28, 'seema@456', 2, 1),
(2, 'vikash patel', 'vikashpatel456@gmail.com', 9876512345, 'Vijay Nagar, Shop no. 2', 29, 'vikash@789', 2, 1),
(2, 'nisha rani', 'nisharani123@gmail.com', 9586124789, 'Shakti Apartments, B-Block', 20, 'nisha@123', 2, 1),
(2, 'aman singh', 'amansingh123@gmail.com', 9778832211, 'New market, Road no. 5', 27, 'aman@singh', 2, 1),
(2, 'siddhi jadhav', 'siddhijadhav456@gmail.com', 9494958901, 'Central park, Office no. 4', 21, 'siddhi@456', 2, 1),
(2, 'sumit yadav', 'sumityadav123@gmail.com', 9123344556, 'A Block, Sector 10', 22, 'sumit@789', 2, 1),
(2, 'kriti khanna', 'kritikhanna123@gmail.com', 9456321098, 'Baker Street, Flat 8', 23, 'kriti@321', 2, 1),
(2, 'pankaj sharma', 'pankajsharma234@gmail.com', 9988776655, 'Ravi Apartments, C-Block', 24, 'pankaj@112', 2, 1),
(2, 'deepika singh', 'deepikasingh123@gmail.com', 9876541230, 'Green Park, Suite 15', 26, 'deepika@998', 2, 1),
(2, 'gagan joshi', 'gaganjoshi456@gmail.com', 9888776655, 'Kailash Colony', 28, 'gagan@xyz', 2, 1),
(2, 'shubham kumar', 'shubhamkumar123@gmail.com', 9034887745, 'Vikas Nagar, Shop 5', 29, 'shubham@com', 2, 1),
(2, 'manju rai', 'manjurai123@gmail.com', 9456124789, 'Hari Mandir Street', 31, 'manju@rai', 2, 1),
(2, 'mohit verma', 'mohitverma123@gmail.com', 9876543212, 'Jeevan Nagar', 27, 'mohit@789', 2, 1),
(2, 'kritika sharma', 'kritikasharma123@gmail.com', 9845237810, 'Indira Gandhi Colony', 22, 'kritika@abc', 2, 1),
(2, 'rahul jain', 'rahuljain123@gmail.com', 9554321098, 'Lakshmi Nagar', 30, 'rahul@987', 2, 1),
(2, 'alisha rana', 'alisharana123@gmail.com', 9332213456, 'Sector 21, 4th Floor', 22, 'alisha@987', 2, 1),
(2, 'sandeep yadav', 'sandeep.yadav123@gmail.com', 9908765432, 'Kumar Garden, B-Block', 32, 'sandeep@456', 2, 1),
(2, 'tanuja rathore', 'tanujarathore123@gmail.com', 9098761234, 'Anand Vihar, House 7', 29, 'tanuja@321', 2, 1),
(2, 'jatin chauhan', 'jatinchauhan123@gmail.com', 9886554433, 'Shanti Apartments', 24, 'jatin@123', 2, 1)
"""

INITIAL_CAR_DATA_QUERY = """
Insert into Car(User_id, brand_name, Car_variant, Created_by, Updated_by)
values
(1,'Honda','City',1,1),
(1,'Honda','Amaze',1,1),
(1,'Honda','WR-V',1,1),
(1,'Honda','Elevate',1,1),
(1,'Hyundai', 'Creta',1,1),
(1,'Hyundai', 'SUV',1,1),
(1,'Hyundai', 'Verna',1,1),
(1,'Hyundai', 'Venue',1,1),
(1,'Maruti-Suzuki','Shift-Dzire',1,1),
(1,'Maruti-Suzuki','Ertiga',1,1),
(1,'Maruti-Suzuki','Celerio',1,1),
(1,'Maruti-Suzuki','Grand-Vitara',1,1),
(1,'TATA', 'Curvv',1,1),
(1,'TATA', 'Nexon',1,1),
(1,'TATA', 'Safarri',1,1),
(1,'TATA', 'Harrier',1,1)
"""
INITIAL_CATEGORY_DATA_QUERY = """
Insert into Category(Brand_id,Model_name, Color, Number_plate, Rent, Booking_status, Puc_end_date, Insaurance_end_date, Created_by, Updated_by)
values
(1,'V1','Black','RJ01MS0001',3000,'Pending','22-06-2025','15-09-2025',1,1),
(1,'V1','White','RJ01MS0450',3000,'Pending','22-06-2025','15-09-2025',1,1),
(1,'V4','Red-Mate','RJ01DS4001',3500,'Pending','22-06-2025','15-09-2025',1,1),
(2,'M1','Black','GJ01MS0001',2000,'Pending','22-06-2025','15-09-2025',1,1),
(2,'M1','Blue','GJ01MS7801',3000,'Pending','22-06-2025','15-09-2025',1,1),
(2,'MG1','Yellow-mate','GJ01MS4501',3000,'Pending','22-06-2025','15-09-2025',1,1),
(3,'X1','White','MH01MS0452',2800,'Pending','22-06-2025','15-09-2025',1,1),
(3,'X2','Pink','MH01MS0892',3100,'Pending','22-06-2025','15-09-2025',1,1),
(4,'Z1','Brown','MH01LM0012',3000,'Pending','22-06-2025','15-09-2025',1,1),
(4,'Z2','Violet','MH01LM0032',3100,'Pending','22-06-2025','15-09-2025',1,1),
(4,'Z4','White','MH01LM0072',3400,'Pending','22-06-2025','15-09-2025',1,1),
(5,'A1','Beige','KA01LM2232',3500,'Pending','22-06-2025','15-09-2025',1,1),
(5,'A2','Maroon','KA01LM2202',3600,'Pending','22-06-2025','15-09-2025',1,1),
(5,'A3','Blue','KA01LM2312',3400,'Pending','22-06-2025','15-09-2025',1,1),
(6,'B1','Orange','KA01XY1001',3700,'Pending','22-06-2025','15-09-2025',1,1),
(6,'B2','Yellow','KA01XY1011',3800,'Pending','22-06-2025','15-09-2025',1,1),
(6,'B3','Silver','KA01XY1021',1900,'Pending','22-06-2025','15-09-2025',1,1),
(7,'C1','Blue','KA02XY1011',4000,'Pending','22-06-2025','15-09-2025',1,1),
(7,'C2','Black','KA02XY1021',4200,'Pending','22-06-2025','15-09-2025',1,1),
(7,'C4','Silver','KA02XY1041',4400,'Pending','22-06-2025','15-09-2025',1,1),
(8,'D1','Yellow','KA03LM1111',2500,'Pending','22-06-2025','15-09-2025',1,1),
(8,'D2','Purple','KA03LM1121',2600,'Pending','22-06-2025','15-09-2025',1,1),
(8,'D3','Green','KA03LM1131',4700,'Pending','22-06-2025','15-09-2025',1,1),
(9,'E1','Pink','KA04XY1211',2900,'Pending','22-06-2025','15-09-2025',1,1),
(9,'E2','Black','KA04XY1221',5000,'Pending','22-06-2025','15-09-2025',1,1),
(9,'E3','Red','KA04XY1231',5100,'Pending','22-06-2025','15-09-2025',1,1),
(10,'F1','Silver','KA05LM2011',5300,'Pending','22-06-2025','15-09-2025',1,1),
(10,'F2','Yellow','KA05LM2021',3400,'Pending','22-06-2025','15-09-2025',1,1),
(10,'F3','Purple','KA05LM2031',3500,'Pending','22-06-2025','15-09-2025',1,1),
(11,'G1','Maroon','KA06XY2111',5700,'Pending','22-06-2025','15-09-2025',1,1),
(11,'G2','Orange','KA06XY2121',3800,'Pending','22-06-2025','15-09-2025',1,1),
(12,'G3','Blue','KA06XY2131',5900,'Pending','22-06-2025','15-09-2025',1,1),
(12,'G4','Red','KA06XY2141',4500,'Pending','22-06-2025','15-09-2025',1,1),
(13,'H1','Black','KA07LM3011',2100,'Pending','22-06-2025','15-09-2025',1,1),
(13,'D1','Black','KA07LS3001',4100,'Pending','22-06-2025','15-09-2025',1,1),
(13,'F4','Pink','KA05LM2041',5600,'Pending','22-06-2025','15-09-2025',1,1),
(14,'E4','White','KA04XY1241',2200,'Pending','22-06-2025','15-09-2025',1,1),
(14,'D4','Blue','KA03LM1141',2800,'Pending','22-06-2025','15-09-2025',1,1),
(14,'C3','Red','KA02XY1031',4300,'Pending','22-06-2025','15-09-2025',1,1),
(15,'B4','Red','KA01XY1031',4000,'Pending','22-06-2025','15-09-2025',1,1),
(15,'A4','Purple','KA01LM2322',3300,'Pending','22-06-2025','15-09-2025',1,1),
(15,'Z3','Black','MH01LM0052',3300,'Pending','22-06-2025','15-09-2025',1,1),
(16,'X4','Blue','MH01XY0022',3400,'Pending','22-06-2025','15-09-2025',1,1),
(16,'V4','Blue','MH01XY0022',3400,'Pending','22-06-2025','15-09-2025',1,1)
"""



INITIAL_FEEDBACKS_DATA = """
INSERT INTO Feedback(name, email, Feedback_given, created_by, updated_by)
VALUES

('John Doe', 'Great service, will rent again!', 2, 2),
('Jane Smith', 'Had a good experience, but the car could have been cleaner.', 2, 2),
('Sam Johnson', 'The rental process was smooth and easy to follow.', 2, 2),
('Emily Davis', 'The car was in excellent condition and met all expectations.', 2, 2),
('Michael Brown', 'Very convenient location and friendly staff.', 2, 2),
('Sarah Miller', 'I was charged more than expected, but the car was fine.', 2, 2),
('David Wilson', 'Good rental experience, but the return process was a bit slow.', 2, 2),
('Sophia Lee', 'The car was not as described, but everything else was good.', 2, 2),
('James Harris', 'Easy booking, but the pickup time was delayed.', 2, 2),
('Mia Clark', 'Customer service was responsive, but I had issues with the booking website.', 2, 2),
('Daniel Lewis', 'Great value for money, will recommend to others.', 2, 2),
('Olivia Walker', 'Had a few issues with the car, but it was resolved quickly.', 2, 2),
('Lucas Scott', 'The car rental was good, but the drop-off location was inconvenient.', 2, 2),
('Amelia Hall', 'Fantastic experience! The car was clean and well-maintained.', 2, 2),
('Ethan Allen', 'Not happy with the car model, but otherwise fine.', 2, 2),
('Charlotte Young', 'Good service, but the prices were a bit high for my liking.', 2, 2),
('Benjamin King', 'Fast and easy process, but I expected better fuel efficiency from the car.', 2, 2),
('Lily Adams', 'The car was in perfect condition, very happy with the rental.', 2, 2),
('Jack Nelson', 'Great customer service, but I had to wait too long for the car.', 2, 2),
('Harper Carter', 'The booking process was seamless, but the car was smaller than expected.', 2, 2)
"""

INITIAL_CAR_RENTAL_DATA = """
INSERT INTO Car_Rental_Data(User_id, Model_id, Location, License, Assign_date, Return_date, Payment_status, Created_by, Updated_by)
VALUES
(1, 2, 'Jaipur', 'DL14 20110012345', '22-01-2025', '24-01-2025', 'Pending', 1, 1),
(2, 3, 'Bangalore', 'DL15 20110012346', '23-01-2025', '25-01-2025', 'Paid', 1, 1),
(3, 4, 'Chennai', 'DL16 20110012347', '24-01-2025', '26-01-2025', 'Pending', 1, 1),
(4, 5, 'Mumbai', 'DL17 20110012348', '25-01-2025', '27-01-2025', 'Paid', 1, 1),
(5, 6, 'Delhi', 'DL18 20110012349', '26-01-2025', '28-01-2025', 'Pending', 1, 1),
(6, 7, 'Kolkata', 'DL19 20110012350', '27-01-2025', '29-01-2025', 'Paid', 1, 1),
(7, 8, 'Pune', 'DL20 20110012351', '28-01-2025', '30-01-2025', 'Pending', 1, 1),
(8, 9, 'Hyderabad', 'DL21 20110012352', '29-01-2025', '31-01-2025', 'Paid', 1, 1),
(9, 10, 'Agra', 'DL22 20110012353', '30-01-2025', '01-02-2025', 'Pending', 1, 1),
(10, 11, 'Goa', 'DL23 20110012354', '31-01-2025', '02-02-2025', 'Paid', 1, 1),
(11, 12, 'Jaipur', 'DL24 20110012355', '01-02-2025', '03-02-2025', 'Pending', 1, 1),
(12, 13, 'Chennai', 'DL25 20110012356', '02-02-2025', '04-02-2025', 'Paid', 1, 1),
(13, 14, 'Bangalore', 'DL26 20110012357', '03-02-2025', '05-02-2025', 'Pending', 1, 1),
(14, 15, 'Delhi', 'DL27 20110012358', '04-02-2025', '06-02-2025', 'Paid', 1, 1),
(15, 16, 'Mumbai', 'DL28 20110012359', '05-02-2025', '07-02-2025', 'Pending', 1, 1),
(16, 17, 'Kolkata', 'DL29 20110012360', '06-02-2025', '08-02-2025', 'Paid', 1, 1),
(17, 18, 'Pune', 'DL30 20110012361', '07-02-2025', '09-02-2025', 'Pending', 1, 1),
(18, 19, 'Hyderabad', 'DL31 20110012362', '08-02-2025', '10-02-2025', 'Paid', 1, 1),
(19, 20, 'Agra', 'DL32 20110012363', '09-02-2025', '11-02-2025', 'Pending', 1, 1),
(20, 21, 'Goa', 'DL33 20110012364', '10-02-2025', '12-02-2025', 'Paid', 1, 1),
(21, 22, 'Jaipur', 'DL34 20110012365', '11-02-2025', '13-02-2025', 'Pending', 1, 1),
(22, 23, 'Chennai', 'DL35 20110012366', '12-02-2025', '14-02-2025', 'Paid', 1, 1),
(23, 24, 'Bangalore', 'DL36 20110012367', '13-02-2025', '15-02-2025', 'Pending', 1, 1),
(24, 25, 'Delhi', 'DL37 20110012368', '14-02-2025', '16-02-2025', 'Paid', 1, 1),
(25, 26, 'Mumbai', 'DL38 20110012369', '15-02-2025', '17-02-2025', 'Pending', 1, 1),
(1, 27, 'Kolkata', 'DL39 20110012370', '16-02-2025', '18-02-2025', 'Paid', 1, 1),
(2, 28, 'Pune', 'DL40 20110012371', '17-02-2025', '19-02-2025', 'Pending', 1, 1),
(3, 29, 'Hyderabad', 'DL41 20110012372', '18-02-2025', '20-02-2025', 'Paid', 1, 1),
(4, 30, 'Agra', 'DL42 20110012373', '19-02-2025', '21-02-2025', 'Pending', 1, 1),
(5, 31, 'Goa', 'DL43 20110012374', '20-02-2025', '22-02-2025', 'Paid', 1, 1),
(6, 32, 'Jaipur', 'DL44 20110012375', '21-02-2025', '23-02-2025', 'Pending', 1, 1),
(7, 33, 'Chennai', 'DL45 20110012376', '22-02-2025', '24-02-2025', 'Paid', 1, 1)
"""
INITIAL_BILL_DATA = """
Insert into Billing_Data(Car_Rental_id, Total_amount, Created_by, Updated_by)
values(1, 4500, 1, 1),
      (2, 5000, 1, 1),
      (3, 4700, 1, 1),
      (4, 5200, 1, 1),
      (5, 4600, 1, 1),
      (6, 4800, 1, 1),
      (7, 5300, 1, 1),
      (8, 5500, 1, 1),
      (9, 4900, 1, 1),
      (10, 5100, 1, 1)
"""



INSERT_ROLE_QUERY = """
Insert into Role(id, type) 
values(1, 'Admin'),(2, 'Customer')
"""

INSERT_ADMIN_DETAILS_QUERY = """
Insert into Customer(Role_id, User_name, Email, Phone_number, Address, Age, Password, Created_by, Updated_by)
values(1,'Abhishek Soni', 'abhisheksoni123@gmail.com', 9414551449,'H-NO:451 Nehru Nagar Ahmedabad',23, 'Abhishek@123', 1,1)
"""

INSERT_CUSTOMER_DATA_QUERY = """
Insert into Customer(Role_id, User_name, Email, Phone_number, Address, Age, Password, Created_by, Updated_by)
values(2,%s,%s,%s,%s,%s,%s,2,1)
"""

INSERT_NEW_CATEGORY_QUERY = """
Insert into Category(Brand_id, Model_name, Color, Number_plate,Rent,Booking_status, Puc_end_date, Insaurance_end_date, Created_by, Updated_by)
values(%s,%s,%s,%s,%s,'Pending',%s,%s,1,1)
"""

INSERT_NEW_CAR_DATA_QUERY = """ 
Insert into Car(User_id, Brand_name, Car_variant, Created_by, Updated_by)
values(1,%s,%s,1,1)
"""
INSERT_CUSTOMER_DATA_INTO_CAR_RENTAL_TABLE = """
Insert into Car_Rental_Data(User_id, Model_id, Location, License, Assign_date, Return_date,Payment_status,Created_by, Updated_by)
Values(%s,%s,%s,%s,%s,%s,%s,1,1)
"""

INSERT_CUSTOMER_BILL_QUERY = """
Insert into Billing_Data(Car_Rental_id, Total_amount, Created_by, Updated_by)
valus(%s,%s,1,1)
"""
ADD_FEEDBACK_QUERY = """
Insert into Feedback(name,Feedback_given,created_by,updated_by)
values(%s,%s,2,2)
"""

VIEW_BRAND_DATA = """
Select * from car
"""
VIEW_CATEGORY_TABLE = """
Select * from Category
"""
VIEW_MODEL_DATA_QUERY = """
select brand_name, car_variant, model_name,color, number_plate, rent, booking_status, puc_end_date, 
insaurance_end_date from car,category where category.brand_id = car.id and category.id = 4
"""


VIEW_FEEDBACK_TABLE = """
SELECT * FROM Feedback
"""
VIEW_ALL_CUSTOMER = """
select * from customer where role_id = 2
"""

VIEW_ALL_FEEDBACK = "SELECT * FROM feedback"
VIEW_CUSTOMER_DATA_QUERY = "Select * from Customer where id = %s" 

VIEW_CUSTOMER_FEEDBACK_QUERY = """
Select * from Feedback where id = %s
"""
VIEW_CAR_RENTAL_DATA = """
Select * from Car_Rental_Data
"""

VIEW_CUSTOMER_CAR_RENTAL_DATA ="""
Select * from Car_Rental_Data where User_id = %s
"""
VIEW_CUSTOMER_BILL_QUERY = """
select billing_data.id , customer.user_name, car.brand_name,car.car_variant, 
category.model_name, category.color, category.rent, car_rental_data.assign_date, car_rental_data.return_date,
car_rental_data.payment_status,
billing_data.total_amount from customer,car,category,billing_data,car_rental_data 
where billing_data.car_rental_id = car_rental_data.id and customer.id = car_rental_data.user_id 
and category.id = car_rental_data.model_id and car.id = category.brand_id and car_rental_data.user_id = %s
"""

UPDATE_BOOKING_STATUS_PENDING = """
update category set booking_status = 'Pending' where id in (select model_id from car_rental_data where user_id = %s)
"""
UPDATE_PAYMENT_STATUS_DONE = """
Update car_rental_data set Payment_status = 'Paid' where id = %s
"""
UPDATE_CUSTOMER_PASSWORD_QUERY = """Update customer set password = %s where id = %s """

UPDATE_RETURN_DATE = "Update car_rental_data set return_date = %s where user_id = %s"

UPDATE_INSAURANCE_END_DATE = "update category set Insaurance_end_date = %s where id = %s"

UPDATE_PUC_END_DATE = "update category set Puc_end_date = %s where id = %s"


GET_RENTAL_ID_AFTER_SELECTION = "Select id from car_rental_data where user_id = %s and model_id = %s"

DELETE_BRAND_QUERY = """Delete from car where id = %s """
DELETE_CATEGORY_QUERY = "DELETE FROM Category where id = %s"
DELETE_CUSTOMER_DATA_QUERY = "DELETE FROM CUSTOMER where id = %s "
GET_ROLE_ID = """
SELECT role_id FROM customer WHERE email = %s and password = %s
"""
GET_CUSTOMER_ID = """Select id from customer where email = %s """
GET_BILL_ID_AFTER_SELECTION = """
Select id from billing_data where car_rental_id = %s
"""

GET_THE_RENT_OF_CARS = """
Select rent from category where id = %s
"""

GET_CUSTOMER_ID_BY_EMAIL = """
select id from Customer where email = %s
"""

SHOW_BRAND_QUERY = """
Select * from car 
"""
SHOW_MODELS_OF_CAR =  """
select * from category where brand_id = %s and Booking_status = 'Pending'
"""
SHOW_CARS_TO_CUSTOMER = """
Select category.id ,Brand_name, Car_variant,Model_name,Color,Number_plate,Rent,Booking_status,Puc_end_date,Insaurance_end_date from car, category
where car.id = category.brand_id
"""

INSERT_INTO_BILL_DATA = """
Insert into Billing_Data(Car_Rental_id, Total_amount, Created_by, Updated_by)
values(%s,%s,1,1)
"""

DROP_ROLE_TABLE = "DROP TABLE IF EXISTS ROLE CASCADE"
DROP_USER_TABLE = "DROP TABLE IF EXISTS CUSTOMER CASCADE"
DROP_CAR_TABLE = "DROP TABLE IF EXISTS CAR CASCADE"
DROP_CATEGORY_TABLE = "DROP TABLE IF EXISTS CATEGORY CASCADE"
DROP_CAR_RENTAL_TABLE = "DROP TABLE IF EXISTS CAR_RENTAL_DATA CASCADE"
DROP_BILLING_TABLE = "DROP TABLE IF EXISTS BILLING_DATA CASCADE"
DROP_FEEDBACK_TABLE = "DROP TABLE IF EXISTS FEEDBACK CASCADE"
DROP_EXTRACHARGES_TABLE = "DROP TABLE IF EXISTS EXTRA_CHARGES CASCADE"

def delete_all_tables():
    connection = DBMS_connection()

    connection.execute_query(DROP_ROLE_TABLE)
    connection.execute_query(DROP_USER_TABLE)
    connection.execute_query(DROP_CAR_TABLE)
    connection.execute_query(DROP_CATEGORY_TABLE)
    connection.execute_query(DROP_CAR_RENTAL_TABLE)
    connection.execute_query(DROP_BILLING_TABLE)
    connection.execute_query(DROP_FEEDBACK_TABLE)
    connection.execute_query(DROP_EXTRACHARGES_TABLE)


    connection.disconnect_connection()

def create_tables():

    connection = DBMS_connection()
    
    connection.execute_query(CREATE_ROLE_TABLE)
    connection.execute_query(CREATE_USER_TABLE)
    connection.execute_query(CREATE_CAR_TABLE)
    connection.execute_query(CREATE_CAR_CATEGORY_TABLE)
    connection.execute_query(CREATE_CAR_RENTAL_TABLE)
    connection.execute_query(CREATE_TABLE_BILLING)
    connection.execute_query(CREATE_FEEDBACK_TABLE)
    connection.execute_query(CREATE_EXTRA_CHARGES_TABLE)


    connection.disconnect_connection()


def insert_data_table():

    connection = DBMS_connection()

    connection.execute_query(INSERT_ROLE_QUERY)
    connection.execute_query(INSERT_ADMIN_DETAILS_QUERY)
    connection.execute_query(INITIAL_CUSTOMERS_DATA)
    connection.execute_query(INITIAL_CAR_DATA_QUERY)
    connection.execute_query(INITIAL_CATEGORY_DATA_QUERY)
    connection.execute_query(INITIAL_CAR_RENTAL_DATA)
    connection.execute_query(INITIAL_FEEDBACKS_DATA)
    connection.execute_query(INITIAL_BILL_DATA)

    connection.disconnect_connection()


if __name__ == '__main__':
    delete_all_tables()
    create_tables()
    insert_data_table()