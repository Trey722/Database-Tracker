document.getElementById('submitButton').addEventListener('click', function() {

    closePopup(); 


    let username = document.getElementById('user').value;
    let Database = document.getElementById('Database').value;
    let password = document.getElementById('password').value;
    let port = document.getElementById("port").value

    
  
    // Do something with the form data (e.g., log it to console)
    console.log('Username:', username);
    console.log('Database:', Database);
    console.log('Password:', password);
    console.log('port:', port);


    let data = {
        username: username,
        Database: Database,
        password: password,
        port: port
    };

    let apiEndpoint = '/connectDatabase'; 


    sendData(data, apiEndpoint);

    connect = true; 

  
    
  });





  