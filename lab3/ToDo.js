let inputField = document.getElementById("task");

function addTask() {
    let taskText = inputField.value.trim();
    if (taskText === "") return;

    console.log(taskText.length);

    let text = taskText;

    for (let i = 0; text.length; i++) {
        console.log(text[i]);
    }
    return;


    // for (let i = 0; taskText.length; i++) {
    //     if (taskText[i] >= "1" && taskText[i] <= '9') {
    //         alert(taskText);
    //         return;
    //     }
    // }


    let li = document.createElement("li");
    li.innerHTML = `<input type="checkbox" onclick="toggleTask(this)"> 
                    <span class="task-text">${taskText}</span> 
                    <button class="delete-btn" onclick="deleteTask(this)">🗑</button>`;

    document.getElementById("task-list").appendChild(li);
    inputField.value = "";
}


function toggleTask(checkbox) {
    let taskText = checkbox.nextElementSibling;
    taskText.classList.toggle("completed", checkbox.checked);

}

function deleteTask(button) {
    button.parentElement.remove();
}

// inputField.addEventListener("keydown", function (event) {
//     if (event.key === "Enter") {
//         addTask();
//     }
// });