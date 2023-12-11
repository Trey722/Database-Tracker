from backEnd import start


# This function will add a TUPLE to the CUSTOMER TABLE 
# COMPLETED
def addCustomer(FNAME, LNAME, CUSTOMER_ID):
    query1 = f"INSERT CUSTOMER(FNAME, LNAME, CUSTOMER_ID) VALUES('{FNAME}', '{LNAME}', {CUSTOMER_ID});"
    
    result = start.executeQuery(query1)
    
    return result




def searchCustomerID(CUSTOMER_ID):
    try:
        CUSTOMER_ID = int(CUSTOMER_ID)
        query  = f"SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = {CUSTOMER_ID}"
    except:
        query = "SELECT * FROM CUSTOMER"
        
    result = start.executeQuery(query)
    
    return result



