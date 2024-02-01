const hamburger = document.getElementById("hamburger");
const linktxt = document.getElementsByClassName("linktxt");
const logo = document.getElementById("logo");
const logoMobile = document.getElementById("logo-mobile");
const navlist = document.getElementsByTagName("nav")[0].getElementsByTagName("a")

if(window.matchMedia("(max-width: 900px)").matches){
    for (let i = 0; i < navlist.length; i++) {
        navlist[i].classList.add("hint--right")
    }
}

hamburger.addEventListener("click", ()=>{
    var prop
    if (linktxt[0].style.display === "none") {
        prop = "block"
        logoMobile.style.display = "none"
        logo.style.display = "block"
        hamburger.innerHTML = "<span class='material-symbols-outlined'>close</span>"
        hamburger.ariaLabel = "Collapse"
    } else {
        prop = "none"
        logoMobile.style.display = "block"
        logo.style.display = "none"
        hamburger.innerHTML = "<span class='material-symbols-outlined'>chevron_right</span>"
    }
    for (let i = 0; i < linktxt.length; i++) {
        linktxt[i].style.display = prop;
    }
})

window.addEventListener("resize", function() {
    if (window.matchMedia("(min-width: 900px)").matches) {
        logo.style.removeProperty("display")
        logoMobile.style.removeProperty("display")
        for (let i = 0; i < linktxt.length; i++) {
            linktxt[i].style.removeProperty("display");
        }
        for (let i = 0; i < navlist.length; i++) {
            navlist[i].classList.remove("hint--right")
        }
    }
    if(window.matchMedia("(max-width: 900px)").matches){
        for (let i = 0; i < navlist.length; i++) {
            navlist[i].classList.add("hint--right")
        }
    }
})