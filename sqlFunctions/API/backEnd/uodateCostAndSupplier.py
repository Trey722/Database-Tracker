import backEnd.start as start
import backEnd.supplierQueiries as supplierQueiries
import backEnd.ingridentQueries as ingridentQueries




def updateIngrident(INGRIDENT_ID, NEW_PRICE=None, New_Supplier_ID=None):
    status = []
    if (New_Supplier_ID != None):
        result = supplierQueiries.editIngridentSupplier(INGRIEDNT_ID=INGRIDENT_ID, NEW_SUPPLIER_ID=New_Supplier_ID)
        if (result[0] != True):
            status.append("Failed to change supplier", result)
            
    if (NEW_PRICE != None):
        result = ingridentQueries.editPrice(INGREDIENTS_ID=INGRIDENT_ID, NEW_PRICE=NEW_PRICE)
        if (result[0] == False):
            status.append("FAILED to change Price", result)
            
    return status



            
    
        