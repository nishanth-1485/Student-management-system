function addStudent(){

    let name = document.getElementById("name").value;
    let roll = document.getElementById("roll").value;
    let branch = document.getElementById("branch").value;

    if(name == "" || roll == "" || branch == ""){
        alert("Please fill all fields");
        return;
    }

    let table = document.getElementById("studentTable");

    let row = table.insertRow();

    row.insertCell(0).innerHTML = name;
    row.insertCell(1).innerHTML = roll;
    row.insertCell(2).innerHTML = branch;

    let deleteBtn = document.createElement("button");
    deleteBtn.innerHTML = "Delete";

    deleteBtn.onclick = function(){
        table.deleteRow(row.rowIndex);
    }

    row.insertCell(3).appendChild(deleteBtn);

    document.getElementById("name").value="";
    document.getElementById("roll").value="";
    document.getElementById("branch").value="";
}