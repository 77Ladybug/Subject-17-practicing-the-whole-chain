const myText = document.getElementById("myText");
const content = document.getElementById("content");
const addButton = document.getElementById("addButton");

function addToStorage(){
    const newList = myText.value;
    localStorage.setItem("list",newList);

}


addButton.addEventListener("click", addToStorage);