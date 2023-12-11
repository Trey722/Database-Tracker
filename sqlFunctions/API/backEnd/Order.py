import backEnd.functions as functions

import backEnd.productQueriies as productQueriies
import backEnd.requestQueries as requestQueries
import backEnd.ingridentQueries as ingridentQueries
from backEnd import start
"""

A customer requests an Order


The "Customer_Orders", "order_contents", "Product", "Product_ingridnets", and "Ingridents",
and "Order" table is accesed, and “ingridnets_needed” maybe me accesed
input: Customer ID, and Products
Steps
1. Order Id is generated, and order is sent to customer_order tables with order ID and
Customer ID, and statis is sent to pending
2. Order is added to Order Table, and products are sent to Order_Contents table along with
Order ID
3. The avavility of prouducts is checked using prouduct ID, which then checks using
ingridnet ID. If ingrdient are below the minium after the order. The ingrdient_table gets
anj entry of the ingridnets needed to make it max
4. If there aren't enough ingrdients then stus is chnaged to NN. If there are enough then
they are taken away from igrdnets and set to qued, and an editmated wait time is sent
until the order is filled

"""


# 1. The user inputs the CUSTOMER_ID, PRODUCTS, and the goal date
def createCustomerOrder(CUSTOMER_ID, PRODUCTS, GOAL_READY_BY, ORDER_ID=False): # PRODUCTS needs to be a list of PRODUCT_ID's 
    
    # AN order ID is generated
    if (ORDER_ID == False):
        ORDER_ID = int(functions.generate_unique_id(str(CUSTOMER_ID)))
    
    
        
    INGREDIENT_ARRAY = []
    for i in PRODUCTS:
        INGREDIENTS = productQueriies.getArrayOfIngriedents(i)
        if (INGREDIENTS[0] == False):
            return False
        for j in INGREDIENTS:
            INGREDIENT_ARRAY.append(j)
    
    INGREDIENT_ARRAY = set(INGREDIENT_ARRAY)
    # The system checks to see if the INGREDIENTS exist
    for i in INGREDIENT_ARRAY:
        amount_needed = productQueriies.getAmountIngriendentNeeded(INGRIDENT_ID=i)
        if (amount_needed[0] == False):
            return False
        
        amount_needed = amount_needed[1]
        check = ingridentQueries.checkEnough(INGREDIENTS_ID=i, amountNeeded=amount_needed)
        
       
        if (check == False):
            return (False, f"NOT ENOUGH of {i}")
    
    
        
       
       
    # The price is calcuted 
        
    PRICE = 0 
    
    
    # It is quued to the PRODUCT QUEIRIES, and contents table
    for i in range(len(PRODUCTS)):
        curPrice = productQueriies.get_Price_Product(PRODUCTS[i]) # The problem was fixed simply by  moving eveything that changes the DB State after
        if (curPrice[0] == False):
            return False
        PRICE += curPrice[1]
        
        
    for i in INGREDIENTS:
        amount_needed  = productQueriies.getAmountIngriendentNeeded(INGRIDENT_ID=i)
        ingridentQueries.take_x_Amount(INGREDIENT_ID=i, amountNeeded=amount_needed[1])
        
            
        
        
   
            
    
    
    print(requestQueries.addRequest(ORDER_ID=ORDER_ID, READY_BY=GOAL_READY_BY, PRICE=PRICE))
    
    for i in range(len(PRODUCTS)):
        requestQueries.addProdcuts_TO_REQUESTS_Contents(ORDER_ID=ORDER_ID, PRODUCT_ID=PRODUCTS[i])
        
    return [True, ORDER_ID]
        
        
def searchOrder(ORDER_ID):
    try:
        ORDER_ORDER = int(ORDER_ID)
        query = f"SELECT * FROM REQUESTS WHERE ORDER_ID = {ORDER_ID}"
    except:
        query = "SELECT * FROM REQUESTS"
    
    result = start.executeQuery(query)
    
    if result[0] == True:
        modified_result = []
        for row in result[1]:
            if row[3] == b'\x00':
                modified_result.append(row[:3] + (0,) + row[4:])
            else:
                modified_result.append(row[:3] + (1,) + row[4:])
        
        # Creating a new tuple with the modified result list
        result = (result[0], tuple(modified_result))

    return result


def searchOrderContents(ORDER_ID):
    try:
        ORDER_ORDER = int(ORDER_ID)
        query = f"SELECT * FROM REQUEST_CONTENTS WHERE REQUEST_ID = {ORDER_ID}"
    except:
        query = "SELECT * FROM REQUESTS"
    
    result = start.executeQuery(query)


    return result



    
