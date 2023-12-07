
global PASSWORD 
PASSWORD = "TD6812"


import pymysql

# Establish a connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password=PASSWORD,
    database='TRACKER',
    port=3306  # Change the port number if necessary
)

def dropAllTABLES():
    
    cursor = connection.cursor()

    # Get all table names in the database
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # Generate and execute DROP TABLE statements
    for table in tables:
        table_name = table[0]
        drop_query = f"DROP TABLE {table_name}"
        cursor.execute(drop_query)
        
        
    
def createTables():
    
    





    # Execute SQL queries
    query1 = "CREATE TABLE PRODUCTS (Product_Name VARCHAR(255), SALE_PRICE FLOAT(10), COST_TO_MAKE_IT FLOAT(10), AMOUNT_ORDERED INT(10), DATE_ADDED DATE, PRODUCT_ID INT(10) PRIMARY KEY);"

    query2 = "CREATE TABLE INGREDIENTS (INGREDIENT_NAME VARCHAR(255) NOT NULL UNIQUE, AMOUNT_LEFT INT(10), MIN_AMOUNT INT(10), INGREDIENT_ID INT(10) NOT NULL PRIMARY KEY, MAX_AMOUNT INT(10), COST FLOAT(10));"
    
    query3 = "CREATE TABLE PRODUCT_INGREDIENTS (PRODUCT_ID INT(10), INGREDIENT_ID INT(10), AMOUNT_NEED INT(10) NOT NULL,  FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTS(PRODUCT_ID), FOREIGN KEY (INGREDIENT_ID) REFERENCES INGREDIENTS(INGREDIENT_ID));"
    
    query4 = "CREATE TABLE CUSTOMER ( FNAME VARCHAR(255),  LNAME VARCHAR(255),  CUSTOMER_ID INT(10) NOT NULL PRIMARY KEY);"
    
    query5 = "CREATE TABLE REQUESTS (READY_BY DATETIME,  PRICE FLOAT(10) NOT NULL,  ORDER_ID INT(10), FILLED BIT(1) NOT NULL,  TIME_FILLED DATETIME, PRIMARY KEY (ORDER_ID)); "
    
    query6 = "CREATE TABLE CUSTOMER_REQUESTS (CUSTOMER_ID INT, ORDER_ID INT, FILLED BIT NOT NULL, REFUNDED BIT NOT NULL, REFUND_REQUEST BIT NOT NULL, FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID), FOREIGN KEY (ORDER_ID) REFERENCES REQUESTS(ORDER_ID));"
    
    query7 = "CREATE TABLE CUSTOMER_FAVORITE_ITEM (CUSTOMER_ID INT, FAVORITE_ORDER_ID INT, FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID), FOREIGN KEY (FAVORITE_ORDER_ID) REFERENCES REQUESTS(ORDER_ID));"
    
    query8 = "CREATE TABLE REQUEST_CONTENTS (PRODUCT_ID INT, REQUEST_ID INT, FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTS(PRODUCT_ID), FOREIGN KEY (REQUEST_ID) REFERENCES REQUESTS(ORDER_ID));"
    
    query9 = "CREATE TABLE SUPPLIER (SUPPLIER_ID INT, SUPPLIER_NAME VARCHAR(255), PRIMARY KEY (SUPPLIER_ID));"

    
    

    query = [query1, query2, query3, query4, query5, query6, query7, query8, query9]
    
    
    for i in query:
        executeQuery(i)
        
        
    return True
    
    
     
            
    


def executeQuery(query):
    try:
        cursor = connection.cursor()
    except:
        return [False, "Failed to connect"]
    
    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        return [False, "Failed to execute", e]
    
    try:  
        result = cursor.fetchall()
        cursor.close()  # Corrected closing of the cursor
        return [True, result]
    except:
        return [False, "Failed to fetch data"]
    
    

        
    

    

    