const parameters = document.getElementsByClassName("parameters")
const paginationBtns = document.getElementsByClassName("pagination")
const actionBtn = document.getElementsByClassName("action")
const nav = document.getElementsByClassName("nav")


// for (let i = 3; i < 10; i++){
//     const inputValue = document.getElementsByName("p{{ i }}");
//     console.log(inputValue)
//     inputValue.style.display="none";
// }

// console.log("working!")
// pageOne()

// var page = 1;

// function nxt(){
    
//     if(page == 1){
//         pageTwo()
//         page = 2
//     }else if(page == 2){
//         pageThree()
//         page = 3
//     }
// }

// function prev(){
    
//     if(page == 2){
//         pageOne()
//         page = 1
//     }else if(page == 3){
//         pageTwo()
//         page = 2
//     }
// }

// function pageOne(){

    // paginationBtns[0].classList.add("page");
    // paginationBtns[1].classList.remove("page");
    // paginationBtns[2].classList.remove("page");

    // for (let i = 0; i < 3; i++) {
    //     parameters[i].style.display = "block"
    // }
    // for (let i = 3; i < 6; i++) {
    //     parameters[i].style.display = "none"
    // }
    // for (let i = 6; i < 9; i++) {
    //     parameters[i].style.display = "none"
    // }
    // for (let i = 0; i < 2; i++) {
    //     actionBtn[i].style.display = "none"
    // }
    // for (let i = 0; i < 3; i++) {
    //     paginationBtns[i].style.display = "block"
    // }
    // page = 1

    // for (let i = 3; i < 10; i++){
    //     var inputValue = document.getElementsByClassName("inp{{i}}");
    //     console.log(inputValue);
    //     inputValue.style.visibility="hidden";
    // }


// }

// function pageTwo(){

//     paginationBtns[0].classList.remove("page");
//     paginationBtns[1].classList.add("page");
//     paginationBtns[2].classList.remove("page");
    
//     for (let i = 0; i < 3; i++) {
//         parameters[i].style.display = "none"
//     }
//     for (let i = 3; i < 6; i++) {
//         parameters[i].style.display = "block"
//     }
//     for (let i = 6; i < 9; i++) {
//         parameters[i].style.display = "none"
//     }
//     for (let i = 0; i < 2; i++) {
//         actionBtn[i].style.display = "none"
//     }
//     for (let i = 0; i < 3; i++) {
//         paginationBtns[i].style.display = "block"
//     }
//     page = 2

// }

// function pageOne(){

//     paginationBtns[0].classList.remove("page");
//     paginationBtns[1].classList.remove("page");
//     paginationBtns[2].classList.add("page");
    
//     for (let i = 0; i < 3; i++) {
//         parameters[i].style.display = "none"
//     }
//     for (let i = 3; i < 6; i++) {
//         parameters[i].style.display = "none"
//     }
//     for (let i = 6; i < 9; i++) {
//         parameters[i].style.display = "block"
//     }
//     for (let i = 0; i < 2; i++) {
//         actionBtn[i].style.display = "block"
//     }
//     for (let i = 0; i < 3; i++) {
//         paginationBtns[i].style.display = "none"
//     }
//     page = 3

// }



function updateRangeValue1() {
    // Get the slider element
    var slider = document.getElementById('scoreSlider');

    // Get the current value of the slider
    var sliderValue = slider.value;

    // Update the text content of rangeValue1
    // document.getElementById('rangeValue1').innerText = sliderValue;
}


// Attach the updateRangeValue1 function to the input event of the slider
document.addEventListener('DOMContentLoaded', function () {
    var slider = document.getElementById('scoreSlider');
    slider.addEventListener('input', updateRangeValue1);
});

// Function to reset the form (if needed)
function resetForm() {
    document.getElementById('scoreForm').reset();
}




// Function to submit the form
// function submitForm() {
//     // Gather data from the form and make an AJAX request
//     var formData = new FormData(document.getElementById('scoreForm'));
//     var sliderValue = document.getElementById('scoreSlider').value;

//     formData.append('p1', sliderValue);
//     console.log()
//     // sliderValue=document.getElementById('rangeValue1').innerText ;

//     // Make an AJAX request using fetch
//     // console.log(document.getElementById('scoreForm'));
//     console.log(formData);
//     fetch('/judge/participants', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Handle the response from the server
//         console.log(data);
    
//         // Check if the submission was successful
//         if (data.message === 'Score created successfully') {
//             // Optionally, reset the form after successful submission
//             resetForm();
//         }
//     });
//     console.log(sliderValue);
// }

