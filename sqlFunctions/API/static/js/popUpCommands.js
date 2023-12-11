function addCustomer()
{
    let FNAME = document.getElementById("FNAME").value; 
    let LNAME = document.getElementById("LNAME").value; 
    let CUST_ID = document.getElementById("CUSTOMER_ID").value

    let data = {
        First_Name: FNAME,
        Last_Name: LNAME, 
        ID: CUST_ID
    }

    closePopup(); 
    let apiEndpoint = '/add/customer'; 
    sendData(data, apiEndpoint); 
}

function addProduct()
{
    let data 
    {
        PRODUCT_NAME; document.getElementById('PRODUCT_NAME_A'), 
        SALE_PRICE; document.getElementById('SALE_PRICE_A'),
        COST; document.getElementById('COST_A'), 
       PRODUCT_ID; document.getElementById('PRODUCT_ID_A')
    }


}


function searchCustomer()
{
    let CUST_ID = document.getElementById("CUSTOMER_ID_S").value;

    closePopup();
    let apiEndpoint = '/search/customer';

    let data = {
        CUSTOMER_ID: CUST_ID
    };
    sendData(data, apiEndpoint);  
}

function searchProduct()
{

    let Product_ID = document.getElementById('PRODUCT_ID_S').value; 
    closePopup();
    let data = {
        PRODUCT_ID: Product_ID
    };
    let apiEndpoint = '/search/products'
    sendData(data, apiEndpoint);  
}

function searchINGREDIENTS()
{
    let INGREDIENTS_ID = document.getElementById('INGREDIENTS_ID_S').value; 
    closePopup();
    let data = {
        INGREDIENT_ID: INGREDIENTS_ID
    };
    let apiEndpoint = '/search/INGREDIENTS'
    sendData(data, apiEndpoint);  
}

function searchSUPPLIER()
{
    let SUPPLIER_ID = document.getElementById('SUPPLIER_ID_S').value; 
    closePopup();
    let data = {
        SUPPLIER_ID: SUPPLIER_ID
    };
    let apiEndpoint = '/search/SUPPLIER'
    sendData(data, apiEndpoint);  
}


function searchOrder()
{
    let ORDER_ID = document.getElementById('ORDER_ID_S').value; 
    closePopup();
    let data = {
        ORDERS_ID: ORDER_ID
    };

    console.log(data);
    let apiEndpoint = '/search/Order';
    sendData(data, apiEndpoint);  
}

function searchOrderContents()
{
    let orderIDe = document.getElementById("ORDER_ID_S_2").value; 

    closePopup(); 
    let data = {ORDER_ID: orderIDe};

    console.log(data);
    let apiEndpoint = '/search/orderContents';
    sendData(data, apiEndpoint);  
}


function searchIG_SUPPLIER()
{

    let INGREDIENTS_ID_IG = document.getElementById('INGREDIENTS_ID_IG').value; 

    let data = {INGREDIENTS_ID_IG: INGREDIENTS_ID_IG};

    closePopup();

    let apiEndpoint = '/search/IG';

    sendData(data, apiEndpoint);

}