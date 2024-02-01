const parameters = document.getElementsByClassName("parameters")
const paginationBtns = document.getElementsByClassName("pagination")
const actionBtn = document.getElementsByClassName("action")
const nav = document.getElementsByClassName("nav")

pageOne()

var page = 1;

function nxt(){
    
    if(page == 1){
        pageTwo()
        page = 2
    }else if(page == 2){
        pageThree()
        page = 3
    }
}

function prev(){
    
    if(page == 2){
        pageOne()
        page = 1
    }else if(page == 3){
        pageTwo()
        page = 2
    }
}

function pageOne(){

    paginationBtns[0].classList.add("page");
    paginationBtns[1].classList.remove("page");
    paginationBtns[2].classList.remove("page");

    for (let i = 0; i < 3; i++) {
        parameters[i].style.display = "block"
    }
    for (let i = 3; i < 6; i++) {
        parameters[i].style.display = "none"
    }
    for (let i = 6; i < 9; i++) {
        parameters[i].style.display = "none"
    }
    for (let i = 0; i < 2; i++) {
        actionBtn[i].style.display = "none"
    }
    for (let i = 0; i < 3; i++) {
        paginationBtns[i].style.display = "block"
    }
    page = 1

}

function pageTwo(){

    paginationBtns[0].classList.remove("page");
    paginationBtns[1].classList.add("page");
    paginationBtns[2].classList.remove("page");
    
    for (let i = 0; i < 3; i++) {
        parameters[i].style.display = "none"
    }
    for (let i = 3; i < 6; i++) {
        parameters[i].style.display = "block"
    }
    for (let i = 6; i < 9; i++) {
        parameters[i].style.display = "none"
    }
    for (let i = 0; i < 2; i++) {
        actionBtn[i].style.display = "none"
    }
    for (let i = 0; i < 3; i++) {
        paginationBtns[i].style.display = "block"
    }
    page = 2

}

function pageThree(){

    paginationBtns[0].classList.remove("page");
    paginationBtns[1].classList.remove("page");
    paginationBtns[2].classList.add("page");
    
    for (let i = 0; i < 3; i++) {
        parameters[i].style.display = "none"
    }
    for (let i = 3; i < 6; i++) {
        parameters[i].style.display = "none"
    }
    for (let i = 6; i < 9; i++) {
        parameters[i].style.display = "block"
    }
    for (let i = 0; i < 2; i++) {
        actionBtn[i].style.display = "block"
    }
    for (let i = 0; i < 3; i++) {
        paginationBtns[i].style.display = "none"
    }
    page = 3

}
