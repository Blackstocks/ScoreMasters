const mainleft = document.getElementsByClassName("left")[0];
const mainright = document.getElementsByClassName("right")[0];
const mainmiddle = document.getElementsByClassName("middle")[0];
const profile = document.getElementsByClassName("pricard")[0].getElementsByClassName("profile")[0];
const activity = document.getElementsByClassName("pricard")[0].getElementsByClassName("activity")[0];
const hint = document.getElementsByClassName("hint--right");

if(window.matchMedia("(max-width: 700px)").matches){
    profile.innerHTML = mainright.getElementsByClassName("profile")[0].innerHTML
    activity.innerHTML = mainright.getElementsByClassName("stats")[0].innerHTML
}

window.addEventListener("resize", function() {
    if (window.matchMedia("(max-width: 700px)").matches) {
        profile.style.display = "block"
        profile.innerHTML = mainright.getElementsByClassName("profile")[0].innerHTML
        activity.innerHTML = mainright.getElementsByClassName("stats")[0].innerHTML
    } else{
        profile.style.display = "none"
    }
})