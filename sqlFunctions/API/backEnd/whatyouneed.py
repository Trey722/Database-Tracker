import backEnd.start as start 
import backEnd.ingridentQueries as ingridentQueries


# This funciton returns what you need and how much when you input the SUPPLIER
def getWhatYouNeed(SUPPLIER_ID):
    query1 = f"SELECT INGREDIENT_ID FROM SUPPLIER_SUPPLIES WHERE SUPPLIER_ID = {SUPPLIER_ID}"
    
    result = start.executeQuery(query1)
    
    if (result[0] == False):
        return False
    
    
    array = []
    amount_need = []
    for i in range(len(result[1])):
        array.append(result[1][i])
    
    for i in range(len(array)):
        array[i] = array[i][0]
        
    for i in array:
        MIN = ingridentQueries.getMIN(i)
        
        curAmount = ingridentQueries.getAmount(i)
        
        if (curAmount[0] == False):
            return [False, curAmount]
        
        
            
        
        if (curAmount[1] < MIN):
            curNeed = ingridentQueries.amountNeeded_TO_MAX(INGREDIENTS_ID=i)
            amount_need.append([i, curNeed])
            
        
    
    
        
    return amount_need

