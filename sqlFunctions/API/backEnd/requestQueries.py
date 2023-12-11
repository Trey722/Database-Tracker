import backEnd.start as start

# COMPLETED
def addRequest(ORDER_ID, READY_BY, PRICE):
    
    
    query = f"INSERT INTO REQUESTS(ORDER_ID, READY_BY, PRICE, FILLED, TIME_FILLED) VALUES ({ORDER_ID}, '{READY_BY}', {PRICE}, 0, NULL)"
    
    result = start.executeQuery(query)
    
    
    return result


# COMPLETED
def addProdcuts_TO_REQUESTS_Contents(ORDER_ID, PRODUCT_ID): 
    query = f"INSERT INTO REQUEST_CONTENTS(REQUEST_ID, PRODUCT_ID) VALUES({ORDER_ID}, {PRODUCT_ID})"
    
    result = start.executeQuery(query)
    
    return result
    

# COMPLETED
def changeFILLEDandDATE(ORDER_ID):
    "YYYY-MM-DD "
    query1 = f"UPDATE REQUESTS SET FILLED = 1 WHERE ORDER_ID = {ORDER_ID}"
    query2 = f"UPDATE REQUESTS SET TIME_FILLED = SELECT GETDATE(), WHERE ORDER_ID = {ORDER_ID}"
    
    result = start.executeQuery(query1)
    
    if (result[0] == True):
        result = start.executeQuery(query=query2)
        return result
    
    return result
    


    
    
    