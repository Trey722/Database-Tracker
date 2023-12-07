import start


# This function will add a TUPLE to the CUSTOMER TABLE 
# COMPLETED
def addCustomer(FNAME, LNAME, CUSTOMER_ID):
    query1 = f"INSERT CUSTOMER(FNAME, LNAME, CUSTOMER_ID) VALUES('{FNAME}', '{LNAME}', {CUSTOMER_ID})"
    
    result = start.executeQuery(query=query1)
    
    return result






