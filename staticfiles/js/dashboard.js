const editDiv = document.getElementById("edit-profile-image");
const a_list = editDiv.getElementsByTagName("a")[0]

//const inputField = document.getElementsByClassName("image_upload_field")[0]
const divToggle = document.getElementById("image-edit-btn")
divToggle.addEventListener("click", function(){
    editDiv.className = "visible-p"
})
function hideDiv(){
    editDiv.className = "invisible-p"
}

a_list.style.display = "none"

var newContent_a = editDiv.innerHTML.replace("Currently:", "")
var newContent_b =newContent_a.replace("Change:", "")
var newContent_c = newContent_b.replace("Choose File", "Upload Image")
// inputField.setAttribute("value", "Upload Image")
editDiv.innerHTML = newContent_c
// console.log(inputField)