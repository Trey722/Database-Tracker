from backEnd import start

# COMPLETED
def addSupplier(SUPPLIER_ID, SUPPLIER_NAME):
    query1 = f"INSERT SUPPLIER(SUPPLIER_ID, SUPPLIER_NAME) VALUES({SUPPLIER_ID}, '{SUPPLIER_NAME}')"
    
    result = start.executeQuery(query1)
    
    return result


def searchSupplier(SUPPLIER_ID):
    try:
        SUPPLIER_ID = int(SUPPLIER_ID)
        query = f"SELECT * FROM SUPPLIER WHERE SUPPLIER_ID = {SUPPLIER_ID}"
    except:
        query = "SELECT * FROM SUPPLIER"
    
    result = start.executeQuery(query)
    
    return result

def searchIG_SUPPLY(INGRIEDNT_ID):
    try:
        INGRIEDNT_ID = int(INGRIEDNT_ID)
        query = f"SELECT * FROM SUPPLIER_SUPPLIES WHERE INGRIEDNT_ID = {INGRIEDNT_ID}"
    except:
        query = "SELECT * FROM SUPPLIER_SUPPLIES"
        
    reuslt = start.executeQuery(query)
    
    return reuslt

# COMPLETED
def addIngridnetSupply(INGRIEDNT_ID, SUPPLIER_ID):
    query1 = f"INSERT INTO SUPPLIER_SUPPLIES(SUPPLIER_ID, INGREDIENT_ID) VALUES ({SUPPLIER_ID}, {INGRIEDNT_ID})"
    
    result = start.executeQuery(query1)
    
    return result

# COMPLETED
def editIngridentSupplier(INGRIEDNT_ID, NEW_SUPPLIER_ID):
    query1 = f"UPDATE SUPPLIER_SUPPLIES SET SUPPLIER_ID = {NEW_SUPPLIER_ID} WHERE INGREDIENT_ID = {INGRIEDNT_ID}"
    
    result = start.executeQuery(query1)
    
    return result






