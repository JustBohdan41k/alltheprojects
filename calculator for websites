// 1. Create a new HTML file
// 2. Create a button with "calc" class
// 3. Add <script>
// 4. Paste this script into <script> and </script>

//variables

const buttons = document
 .querySelectorAll('.calc');
let a = 0;
let b = 0;
let c = "None";

//functions

function calc() {
    a = parseInt(prompt(
     "First num:"));
    b = parseInt(prompt(
     "Second num:"));
    c = prompt("Action:");
    if(c === "+"){
    alert(`The answer is ${a + b}`);
    } else if(c === "-"){
      alert(`The answer is ${a - b}`);
    } else if(c === "*"){
      alert(`The answer is ${a * b}`);
    } else if(c === "/"){
      alert(`The answer is ${a / b}`);
    }
 }

 buttons.forEach(button => {
   button.onclick = () => {
    calc();
   };
});
