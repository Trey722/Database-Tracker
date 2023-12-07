import start 
import pymysql

# COMPELETED
def addINGREDIENTS(INGREDIENTS_ID, INGREDIENTS_NAME, AMOUNT_LEFT, MIN_AMOUNT, MAX_AMOUNT, COST):
    query = "INSERT INTO INGREDIENTS(INGREDIENT_ID, INGREDIENT_NAME, AMOUNT_LEFT, MIN_AMOUNT, MAX_AMOUNT, COST) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (INGREDIENTS_ID, INGREDIENTS_NAME, AMOUNT_LEFT, MIN_AMOUNT, MAX_AMOUNT, COST)

    try:
        cursor = start.connection.cursor()
        cursor.execute(query, values)
        start.connection.commit()
        cursor.close()
        return [True]
    except Exception as e:
        return [False, str(e)]

    
 # WARNING returns the actually qeury
 # COMPLETED
def amountNeeded_TO_MAX(INGREDIENTS_ID):
    query1 = f"SELECT MAX_AMOUNT, AMOUNT_LEFT FROM INGREDIENTS WHERE INGREDIENT_ID = {INGREDIENTS_ID}"
    
    result = start.executeQuery(query=query1)
    
    if (result[0] == False):
        return result
    
    if (result[0] == True):
        return result[1][0][0] - result[1][0][1]
    
    
    


# COMPLETED
def take_x_Amount(INGREDIENT_ID, amountNeeded):
    amount_left = getAmount(INGREDIENTS_ID=INGREDIENT_ID)[1]
    newAmount = amount_left - amountNeeded
    
    query = f"UPDATE INGREDIENTS SET AMOUNT_LEFT = {newAmount} WHERE INGREDIENT_ID = {INGREDIENT_ID}"
    
    result = start.executeQuery(query=query)
    
    return result
    
    
    
# COMPLETED
def add_X_Amount(INGREDIENT_ID, ADDED):
    amount_left = getAmount(INGREDIENTS_ID=INGREDIENT_ID)[1]
    newAmount = amount_left + ADDED
    
    query = f"UPDATE INGREDIENTS SET AMOUNT_LEFT = {newAmount} WHERE INGREDIENT_ID = {INGREDIENT_ID}"
    
    result = start.executeQuery(query=query)
    
    return result
    
  
        
    
    


# THis function calcutes the amount of reosurces
#COMPLETED
def getAmount(INGREDIENTS_ID):
    query1 = f"SELECT AMOUNT_LEFT FROM INGREDIENTS WHERE INGREDIENT_ID = {INGREDIENTS_ID}"
    
    result = start.executeQuery(query1)
    
    if (result[0] == True):
        result[1] = result[1][0][0]
    
    return result
    
    
# This function calls get amount and then calcutes to see if enough ingridents exist
#COMPLETED
def checkEnough(INGREDIENTS_ID, amountNeeded):
   
    queryResult = getAmount(INGREDIENTS_ID=INGREDIENTS_ID)
    
    if (queryResult[0] == False):
        return queryResult 
    
    amount_left = queryResult[1] 
    
    
    if (amount_left < amountNeeded):
        return [True, False]
    
    else:
        return [True, True]
    
    



    

    
   
   




