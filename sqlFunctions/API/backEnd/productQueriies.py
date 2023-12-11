import backEnd.functions as func


from backEnd import start


# Ingirdnets and amount_Needed must be the same size
# COMPLETED
def queryProducts(Product_Name, SALE_PRICE, COST_TO_MAKE_IT, AMOUNT_ORDERED, PRODUCT_ID, INGRIDENTS, amount_Needed):
    query = f"INSERT INTO PRODUCTS (PRODUCT_ID, PRODUCT_NAME, SALE_PRICE, COST_TO_MAKE_IT, AMOUNT_ORDERED, DATE_ADDED) VALUES ({PRODUCT_ID}, '{Product_Name}', {SALE_PRICE}, {COST_TO_MAKE_IT}, {AMOUNT_ORDERED}, CURRENT_TIMESTAMP)"
    
    
    
    if (len(INGRIDENTS) != len(amount_Needed)):
        return [False, "Every Ingrident does not have a price"]
    
    
    result = start.executeQuery(query)
    
    if (result[0] == False):
        return result
    
    for i in INGRIDENTS:
        addProductIngriedents(PRODUCT_ID=PRODUCT_ID, INGREDIENT_ID=i)

    return result


def searchProducts(PRODUCT_ID):
    try:
        PRODUCT_ID = int(PRODUCT_ID)
        query = f"SELECT * FROM PRODUCTS WHERE PRODUCT_ID = {PRODUCT_ID}"
    except:
        query = "SELECT * FROM PRODUCTS"
        
    result = start.executeQuery(query=query)
    return result
    

# COMPLTEED
def addProductIngriedents(PRODUCT_ID, INGREDIENT_ID, AMOUNT_NEED):
    query = f"INSERT INTO PRODUCT_INGREDIENTS(PRODUCT_ID, INGREDIENT_ID, AMOUNT_NEED) VALUES({PRODUCT_ID}, {INGREDIENT_ID}, {AMOUNT_NEED})"
    result = start.executeQuery(query)
    return result

    
    
# THis functions excutes a query to get a price of a PRODUCT_ID
# COMPLETED
def get_Price_Product(PRODUCT_ID):

       
    query1 = f"SELECT SALE_PRICE FROM PRODUCTS WHERE PRODUCT_ID = {PRODUCT_ID}"
        
       
    result = start.executeQuery(query=query1)
    
    if (result[0] == False):
        return result
    
    result[1] = result[1][0][0]
    
    return result
    

# THis function gets all the ingridnets needed for a product and returns an array of it
# COMPLETED 
def getArrayOfIngriedents(PRODUCT_ID):
    query1 = f"SELECT INGREDIENT_ID FROM PRODUCT_INGREDIENTS WHERE PRODUCT_ID = {PRODUCT_ID}"
    
    
    result = start.executeQuery(query=query1)
    
    if (result[0] == False):
        return result

    
    array = []
    
    for i in result[1]:
        array.append(i)
    

    result[1] = array
    
    result = [elem[0] if len(elem) == 1 else tuple(elem) for elem in result[1]]
    
    return result 

# COMPLETED
def getAmountIngriendentNeeded(INGRIDENT_ID):
    query1 = f"SELECT AMOUNT_NEED FROM PRODUCT_INGREDIENTS WHERE INGREDIENT_ID = {INGRIDENT_ID}"
    
    result = start.executeQuery(query=query1)
    
    if (result[0] == False):
        return result
    
    result[1] = result[1][0][0]

    
    
    return result 


print(getArrayOfIngriedents(56789043))






    
