function updateTable(data) {
    let rowsLength = data.length;
    let columnLength = data[0].length;
    let table = document.getElementById('table');

    // Clear the existing table content
    table.innerHTML = '';

    // Create new table rows and cells using the provided data
    for (let i = 0; i < rowsLength; i++) {
        let row = table.insertRow(); // Insert a new row

        for (let j = 0; j < columnLength; j++) {
            let cell = row.insertCell(); // Insert a new cell
            cell.textContent = data[i][j]; // Set cell content using data
        }
    }


    table.style.display = 'table'; 
}
