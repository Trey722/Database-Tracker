/*
200 means success
400 implies a user error
500 implies other error
*/
function sendData(data, apiPoint) {
    fetch(apiPoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    })
    .then(responseData => {
        console.log('Response from Flask API:', responseData);
        
        console.log(responseData.status);
        if (responseData.status === 200) {
            popUpSuccess(responseData.success);
    
        } 

        else if (responseData.status === 201) {
            popUpSuccess(responseData.success);
            updateTable(responseData.data); 
        }
        
        else if (responseData.status === 400) {
            popUpError(responseData.error);
        } else if (responseData.status === 500) {
            popUpError(responseData.error);
        } else {
            console.log('Other response scenario');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        popUpError('Error occurred. Please try again.');
    });
}
