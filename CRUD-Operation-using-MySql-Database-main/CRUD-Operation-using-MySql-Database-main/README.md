

CREATE TABLE Product (
    PID INT AUTO_INCREMENT PRIMARY KEY,
    Pname VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL
);


sudo python app.py




Product Management System with RESTful API - Seminar Document
Overview
This seminar introduces a simple Product Management System built using a RESTful API. The system allows users to perform CRUD (Create, Read, Update, Delete) operations on product data stored in a MySQL database. The system is accompanied by a web interface to interact with the API.

Technologies Used
Backend Framework: Flask (Python)
Database: MySQL
Frontend: HTML, CSS, JavaScript
Communication Protocol: REST (Representational State Transfer)
AJAX: Asynchronous JavaScript and XML
Components
Backend (Flask API)
1. Server Setup
The Flask web server is set up to handle HTTP requests and responses.

python
Copy code
from flask import Flask, jsonify, request
import mysql.connector as sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ... (Database connection and CRUD operations)
2. Database Connection
A MySQL database is used to store product information. The Flask app connects to the database to perform CRUD operations.

python
Copy code
def get_db_connection():
    return sql.connect(host="localhost", user="root", passwd="", database='Products')
3. API Endpoints
Several API endpoints are defined to handle different operations on the product data.

GET all products:
python
Copy code
@app.route('/products', methods=['GET'])
def get_all_products():
    # ... (Fetch and return all products)
GET product by ID:
python
Copy code
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    # ... (Fetch and return product by ID)
POST add product:
python
Copy code
@app.route('/products/add', methods=['POST'])
def add_product():
    # ... (Add a new product)
DELETE product by ID:
python
Copy code
@app.route('/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # ... (Delete product by ID)
PUT update product by ID:
python
Copy code
@app.route('/products/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # ... (Update product by ID)
4. Exception Handling
Exception handling is implemented to provide meaningful error messages in case of issues.

python
Copy code
try:
    # ... (Code that might raise an exception)
except Exception as e:
    return jsonify({'error': str(e)})
Frontend (HTML, CSS, JavaScript)
The frontend is a simple web interface that interacts with the Flask API using JavaScript and AJAX.

1. HTML Structure
html
Copy code
<!-- ... (HTML structure for product management form and table) -->
2. CSS Styling
css
Copy code
/* ... (CSS styling for the form, table, and buttons) */
3. JavaScript Interactions
javascript
Copy code
// ... (JavaScript for fetching, adding, updating, and deleting products using AJAX)
Usage
Start the Flask server: python your_flask_app.py
Access the web interface: http://127.0.0.1:5000
Conclusion
This seminar provides an overview of a simple Product Management System with a RESTful API. The combination of Flask, MySQL, and AJAX allows for efficient handling of product data. The system can be extended and customized based on specific requirements.

