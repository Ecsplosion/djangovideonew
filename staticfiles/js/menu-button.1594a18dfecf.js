const menuButton = document.getElementById("menu-button")
const hiddenMenu = document.getElementById("hidden-menu")

menuButton.addEventListener("click", function(){
    var className = hiddenMenu.className;
    if(className =="invisible-m"){
        hiddenMenu.className = "visible-m"
    } else {
        hiddenMenu.className = "invisible-m"
    }
})