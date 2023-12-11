var connect = false
var openPopUps = []


var formToID  = {
'customerA': "addCustomerForm",
'ProductA': "addProductForm",
'customerS': "searchCustomerForm",
'productS': "searchProductForm",
'ingridentS': "searchINGREDIENTSForm",
'supplierS': "searchSUPPLIERForm",
'orderS': "searchORDERForm",
'orderContentsS': "searchORDERCONTENTS",
'Request_Order': "requestOrderForm",
'editIngrident': 'editIngridentForm',
'whatYouNeed': "whatYouNeedForm",
'IG_SUPPLIER': "IG_SUPPLIER_FORM"

}



function openPopup(id)
{
    document.getElementById(id).style.display = "block";
    openPopUps.push(id);
    
}

function popUpError(text)
{
    openPopup("popUpError"); 
    document.getElementById("Error_Message").innerText = text; 
}

function popUpSuccess(text)
{
    openPopup("popUpsuccess"); 
    document.getElementById("Success_Message").innerText = text; 
}

function closePopup() {
    id = openPopUps[0]
    openPopUps.shift();
    document.getElementById(id).style.display = "none";
    console.log(`"${id}" should be closed`); 
  }

function excutePopup(kind) 
{
    if (openPopUps.length > 0) closePopup();

    if (connect === false && kind !== "connect") 
    {
        popUpError("Not Connected to a Database"); 
        return; 
    }

    else if (kind === "connect" && connect === false) 
    
    {
        openPopup('connectInformation');
        console.log("ConnectPopUp should be open"); 
    }

    let ID = formToID[kind];
    openPopup(ID); 
    
}
