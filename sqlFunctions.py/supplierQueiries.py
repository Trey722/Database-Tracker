import start

# COMPLETED
def addSupplier(SUPPLIER_ID, SUPPLIER_NAME):
    query1 = f"INSERT SUPPLIER(SUPPLIER_ID, SUPPLIER_NAME) VALUES({SUPPLIER_ID}, '{SUPPLIER_NAME}')"
    
    result = start.executeQuery(query1)
    
    return result

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



