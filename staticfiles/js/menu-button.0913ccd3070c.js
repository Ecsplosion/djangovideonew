const menuButton = document.getElementById("menu-button")
const hiddenMenu = document.getElementById("hidden-menu")
menuButton.addEventListener("click", function(){
    if(hiddenMenu.style.left =="0px"){
        hiddenMenu.style.left = "-338px"
    } else {
        hiddenMenu.style.left = "0px"
    }
})