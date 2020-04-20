from flask import Flask
import pymysql
app = Flask(__name__)

#this file is for refreshing everything in a database, all data will be lost and a default admin account will be created.

#connect('host', 'username', 'password', 'database_name')
db = pymysql.connect('localhost', 'root', '', 'ink')

#cursor executes sql commands
cursor = db.cursor()

try:
	cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
	cursor.execute("DROP TABLE IF EXISTS Account")
	cursor.execute("DROP TABLE IF EXISTS Category")
	cursor.execute("DROP TABLE IF EXISTS Brand")
	cursor.execute("DROP TABLE IF EXISTS Product")
	cursor.execute("DROP TABLE IF EXISTS Cart")
	cursor.execute("DROP TABLE IF EXISTS Order")
	cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
finally:
	account_table = """CREATE TABLE Account (
	AccountID int AUTO_INCREMENT,
	Type enum ('Member', 'Admin'),
	Name varchar(20),
	Email varchar(255),
	Password varchar(30),
	PRIMARY KEY (AccountID))"""
	cursor.execute(account_table)
	#creates admin account for access to admin page
	cursor.execute("INSERT INTO Account (Type, Name, Email, Password) VALUES ('Admin', 'Admin1', 'Admin1@gmail.com', 'admin')")

	category_table = """CREATE TABLE Category (
	CategoryID int AUTO_INCREMENT,
	CategoryName varchar(20),
	PRIMARY KEY (CategoryID))"""
	cursor.execute(category_table)
	#create existing categories
	cursor.execute("INSERT INTO Category (CategoryName) VALUES ('Drawing Pencils'), ('Colored Pencils'), ('Brushes'), ('Tablets')")

	brand_table = """CREATE TABLE Brand (
	BrandID int AUTO_INCREMENT,
	BrandName varchar(20),
	PRIMARY KEY (BrandID))"""
	cursor.execute(brand_table)

	product_table = """CREATE TABLE Product (
	ProductID int AUTO_INCREMENT,
	CategoryID int,
	BrandID int,
	ProductName varchar(50),
	ProductDesc text,
	Picture varchar(255),
	Quantity int,
	Price int,
	PRIMARY KEY (ProductID),
	FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
	FOREIGN KEY (BrandID) REFERENCES Brand(BrandID))
	"""
	cursor.execute(product_table)

	cart_table = """CREATE TABLE Cart (
	CartID int AUTO_INCREMENT,
	ProductID int,
	AccountID int,
	PRIMARY KEY (CartID),
	FOREIGN KEY (AccountID) REFERENCES Account(AccountID),
	FOREIGN KEY (ProductID) REFERENCES Product(ProductID))
	"""
	cursor.execute(cart_table)

	order_table = """CREATE TABLE OrderDesc (
	OrderID int AUTO_INCREMENT,
	ProductID int,
	AccountID int,
	OrderDate datetime,
	PRIMARY KEY (OrderID),
	FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
	FOREIGN KEY (AccountID) REFERENCES Account(AccountID))
	"""
	cursor.execute(order_table)

db.close()