const { send } = require("process");

//Helper function 
function stringToArray(str) {
    const arr = str.split(',');
    const trimmedArray = arr.map(item => parseInt(item.trim(), 10)); // Using parseInt to convert to integers

    return trimmedArray;
}


function requestOrder()
{
    let customer_ID = document.getElementById('CUSTOMER_ID_S').value; 
    let PRODUCT_IDS = document.getElementById('PRODUCT_ID_FUNCTION1').value; 
    let array = stringToArray(PRODUCT_IDS); 
    let minutesAwway = document.getElementById('GOAL_TIME').value


    let data = {
        ID: customer_ID,
        PRODUCT_IDs: array,
        MINUTES: minutesAwway
    }

    closePopup()

    let apiendpoint = "/add/Customer_Order"

    sendData(data, apiendpoint)
}

function editIngrident()
{
    let INGREDIENT_ID = document.getElementById("Ingrident_ID_F_2").value;
    let NEW_COST = document.getElementById("COST_F_2").value;
    let NEW_SUPPLIER_ID = document.getElementById("SUPPLIER_ID_F_2").value; 

    let data = {
        INGREDIENT_ID: INGREDIENT_ID, 
        NEW_COST: NEW_COST, 
        NEW_SUPPLIER_ID: NEW_SUPPLIER_ID
    }


    closePopup()

    console.log(data); 

    let apiEndpoint = "/edit/INGRIDENT"

    sendData(data, apiEndpoint)


}


function seeIngridentsNeeded()
{
    let supplier_ID = document.getElementById('SUPPLIER_ID_F_3').value

    let data= {supplier_ID: supplier_ID}; 

    console.log(supplier_ID); 

    let apiEndpoint = "/seewhatyouneed" 

    closePopup()


    sendData(data, apiEndpoint);


}