from flask import Flask, jsonify, request, render_template
from backEnd import start
from backEnd import customerQueries
from backEnd import productQueriies
from backEnd import ingridentQueries
from backEnd import supplierQueiries
from backEnd import Order
from backEnd import functions
from backEnd import uodateCostAndSupplier
from backEnd import whatyouneed
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Add section 
@app.route('/connectDatabase', methods=['POST'])
def connectDatabase():
    print("An attempt was made to send data")
    data = request.json
    USER_DATA = data['username']
    DATABASE_DATA = data['Database']
    PASSWORD_DATA = data['password']
    port = data['port']
    start.addConnectInfo(USER_d=USER_DATA, PASSWORD_d=PASSWORD_DATA, DATABASE_d=DATABASE_DATA, PORT_D=int(port))
    test = start.establish_connection()
    
    if test[0] == False:
        return jsonify({"error": test[1], "status": 400}) 
    else:
        return jsonify({f"success": f"successfully connected to {DATABASE_DATA} as {USER_DATA}", "status": 200})
    


    

     
    
    
# Search Section 


def procceseData_Tables(TABLE_NAME, result):
    
    
    
    # If fialed returns erorr
    if result[0] == False: 
        result = str(result[1])
        return jsonify({"error": result[1], "status": 400})
    else:
        rawColumnData = start.getColumns(TABLE=TABLE_NAME)
        columnData = []
        row1 = []
        for i in rawColumnData[1]:
            row1.append(i[0])
            
        columnData.append(row1)
            
        for i in result[1]:
            row = i
            columnData.append(row)
        print(result)
            
        if (rawColumnData[0] == False):
            return jsonify({"error": f"{rawColumnData[1], rawColumnData[2]}", "status": 400})
            
        return jsonify({"success": f"{TABLE_NAME} added successfully", "status": 201, "data": columnData})
    
    
    
@app.route("/search/customer", methods=['POST'])
def api_get_Customer():
    data = request.json
    CUSTOMER_ID = data.get('CUSTOMER_ID')

    result = customerQueries.searchCustomerID(CUSTOMER_ID=CUSTOMER_ID)
    
    return procceseData_Tables("CUSTOMER", result)
    
@app.route("/search/products", methods=['POST'])
def api_GET_PRODUCTS():
    data = request.json
    PRODUCT_ID = data.get("PRODUCT_ID")
    
    result = productQueriies.searchProducts(PRODUCT_ID=PRODUCT_ID)
    
    return procceseData_Tables("PRODUCTS", result)

@app.route("/search/INGREDIENTS", methods=['POST'])
def api_GET_INGREDIENTS():
    data = request.json
    INGREDIENT_ID = data.get("INGREDIENT_ID")
    
    
    result = ingridentQueries.searchIngridents(INGREDIENTS_ID=INGREDIENT_ID)
    
    return procceseData_Tables("INGREDIENTS", result)


@app.route("/search/SUPPLIER", methods=["POST"])
def api_GET_SUPPLIER():
    data = request.json
    SUPPLIER_ID = data.get("SUPPLIER_ID")
    
    result = supplierQueiries.searchSupplier(SUPPLIER_ID=SUPPLIER_ID)
    
    return procceseData_Tables("SUPPLIER", result)


@app.route("/search/Order", methods=['POST'])
def api_GET_ORDER():
    data = request.json
    
    ORDER_ID = data.get('ORDERS_ID')
    
    
    result = Order.searchOrder(ORDER_ID)
    
    
    return procceseData_Tables("REQUESTS", result)
    
@app.route("/search/orderContents", methods=['POST'])
def APIT_GET_ORDER_CONTETNS():
    data  = request.json 
    ORDER_ID = data.get("ORDER_ID")
    
    result = Order.searchOrderContents(ORDER_ID)
    
    print(result)
    return procceseData_Tables("REQUEST_CONTENTS", result)

@app.route("/search/IG", methods=['POST'])
def API_GET_IG():
    data = request.json
    IG_ID = data.get('INGREDIENTS_ID_IG')
    
    result = supplierQueiries.searchIG_SUPPLY(IG_ID)
    
    return procceseData_Tables("SUPPLIER_SUPPLIES", result)
    
    

    
# Function 

@app.route("/add/Customer_Order", methods=["POST"])
def add_ORDER():
    data = request.json
    
    array = data.get('PRODUCT_IDs')
    CUSTOMER_ID = data.get('ID')
    MINUTES = data.get('MINUTES')
    
    print(array)
    
    GOAL_TIME = functions.calculate_future_time(int(MINUTES))
    
    result = Order.createCustomerOrder(CUSTOMER_ID, array, GOAL_TIME, ORDER_ID=False)
    
    if result[0] == True:
        return jsonify({"succues": f"The orderID is = {result[1]}", "status": 200})
    else:
        return jsonify({"error": "unidentfied", "status": 500})
    
    
@app.route("/edit/INGRIDENT", methods=["POST"])
def edit_INGRIENT():
    data = request.json 
    
    INGREDIENT_ID = data.get('INGREDIENT_ID')
    NEW_COST = data.get('NEW_COST')
    NEW_SUPPLIER_ID = data.get('NEW_SUPPLIER_ID')
    
    try:
        NEW_COST = float(NEW_COST)
    except:
        NEW_COST = None 
        
    try:
        NEW_SUPPLIER_ID = int(NEW_SUPPLIER_ID)
    except:
        NEW_SUPPLIER_ID = None
        
    result = uodateCostAndSupplier.updateIngrident(INGREDIENT_ID, NEW_PRICE=NEW_COST, New_Supplier_ID=NEW_SUPPLIER_ID)
    
    
    return jsonify({"succese": f"{result}", "status": 200})
    
@app.route("/seewhatyouneed", methods=["POST"])
def check_SUpplier():
    data = request.json
    SUPPLIER_ID = data.get("supplier_ID")
    
    
    result = whatyouneed.getWhatYouNeed(SUPPLIER_ID=SUPPLIER_ID)
    
    
    newData = []
    
    newData.append(["INGRIDENT_ID", "AMOUNT_NEEDED"])
    
    for i in result:
        newData.append([i[0], i[1]])
    
    
    return jsonify({"succese": "INGRIDENTS_NEEDED", "status": 201, "data": newData})
    
    
    
    
     
    
    