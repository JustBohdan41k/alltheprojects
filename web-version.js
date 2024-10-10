

//variables

const buttons = document.querySelectorAll(".calc");
const passgen = document.querySelectorAll(".passgen");
const converter = document.querySelectorAll(".converter");
const back = document.querySelectorAll(".back");
const mtkm = document.querySelectorAll(".mtkm");
const kmtm = document.querySelectorAll(".kmtm");
const ctk = document.querySelectorAll(".ctk");
const ctf = document.querySelectorAll(".ctf");
const socials = document.querySelectorAll(".socials");
const source = document.querySelectorAll(".github");
const website = document.querySelectorAll(".website");
const discord = document.querySelectorAll(".discord");
document.querySelectorAll(".alert");
const milesInKm = 1.609344;
const KmInMiles = 0.621371192;
const kelvinInCelsium = 273.15;
let amount = 0;
let result = 0;
let a = 0;
let b = 0;
let c = "None";
const letters = [
  "A",
  "a",
  "B",
  "b",
  "C",
  "c",
  "D",
  "d",
  "E",
  "e",
  "F",
  "f",
  "G",
  "g",
  "H",
  "h",
  "I",
  "i",
  "J",
  "j",
  "K",
  "k",
  "L",
  "l",
  "M",
  "m",
  "N",
  "n",
  "O",
  "o",
  "P",
  "p",
  "Q",
  "q",
  "R",
  "r",
  "S",
  "s",
  "T",
  "t",
  "U",
  "u",
  "V",
  "v",
  "W",
  "w",
  "X",
  "x",
  "Y",
  "y",
  "Z",
  "z",
];
const num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
const symbols = [
  "!",
  "@",
  "#",
  "$",
  "%",
  "^",
  "&",
  "*",
  "(",
  ")",
  "-",
  "_",
  "=",
  "+",
  ";",
  ":",
  "/",
  "?",
  ".",
  ">",
];

let randomIndex = Math.floor(Math.random() * letters.length);
let randomNum = Math.floor(Math.random() * num1.length);
let randomIndex1 = Math.floor(Math.random() * letters.length);
let randomIndex2 = Math.floor(Math.random() * letters.length);
let randomIndex3 = Math.floor(Math.random() * letters.length);
let randomIndex4 = Math.floor(Math.random() * letters.length);
let randomIndex5 = Math.floor(Math.random() * letters.length);
let randomNum1 = Math.floor(Math.random() * num1.length);
let randomNum2 = Math.floor(Math.random() * num1.length);
let randomSynbol = Math.floor(Math.random() * symbols.length);
let randomSynbol1 = Math.floor(Math.random() * symbols.length);
//functions

function calc() {
  a = parseInt(prompt("First num:"));
  b = parseInt(prompt("Second num:"));
  c = prompt("Action:");
  if (c === "+") {
    alert(`The answer is ${a + b}`);
  } else if (c === "-") {
    alert(`The answer is ${a - b}`);
  } else if (c === "*") {
    alert(`The answer is ${a * b}`);
  } else if (c === "/") {
    if(b === 0){
    alert("You can't divide by zero!")
    }else{
    alert(`The answer is ${a / b}`);
    }
  }
  else if(c !== "+" || c !== "-" || c !== "*" || c !== "/"){
    alert(`Please, use "+", "-", "*" or "/"`);
  }
}
function passwordgen() {
  randomIndex = Math.floor(Math.random() * letters.length);
  randomNum = Math.floor(Math.random() * num1.length);
  randomIndex1 = Math.floor(Math.random() * letters.length);
  randomIndex2 = Math.floor(Math.random() * letters.length);
  randomIndex3 = Math.floor(Math.random() * letters.length);
  randomIndex4 = Math.floor(Math.random() * letters.length);
  randomSynbol = Math.floor(Math.random() * symbols.length);
  randomNum1 = Math.floor(Math.random() * num1.length);
  randomNum2 = Math.floor(Math.random() * num1.length);
  randomSynbol1 = Math.floor(Math.random() * symbols.length);
  alert(
    `I generated a reliable password for you: ${letters[randomIndex]}${letters[randomIndex1]}${num1[randomNum]}${letters[randomIndex2]}${letters[randomIndex3]}${letters[randomIndex4]}${symbols[randomSynbol]}${num1[randomNum1]}${num1[randomNum2]}${symbols[randomSynbol1]}`,
  );
}
function MilesToKm(){
amount = parseInt(prompt("Please, enter the amount of miles:"));
alert(`The result is ${amount * milesInKm}`);
}
function KmToMiles(){
  amount = parseInt(prompt("Please, enter the amount of kilometers:"));
  alert(`The result is ${amount * KmInMiles}`);
}
function celsiumToKelvin(){
  amount = parseFloat(prompt("Please, enter the amount of ℃"));
  alert(`The result is ${amount + kelvinInCelsium} K`);
}
function celsiumToFarenheit(){
  amount = parseInt(prompt("Please, enter the amount of ℃"));
  alert(`The result is ${amount * 9/5 + 32}`);
}
function converter1(){
mtkm.forEach((button) => {
  button.onclick = () => {
    MilesToKm();
  };
});
kmtm.forEach((button) => {
  button.onclick = () => {
    KmToMiles();
  };
});
ctk.forEach((button) => {
  button.onclick = () =>{
    celsiumToKelvin();
  };
});
ctf.forEach((button) => {
  button.onclick = () =>{
    celsiumToFarenheit();
  };
});
}
buttons.forEach((button) => {
  button.onclick = () => {
    calc();
  };
});
passgen.forEach((button) => {
  button.onclick = () => {
    passwordgen();
  };
});
converter.forEach((button) => {
  button.onclick = () => {
    location.replace('https://sqdih2.mimo.run/convert.html');
  };
});
converter1();

back.forEach((button) => {
button.onclick = () => {
location.replace('https://sqdih2.mimo.run/index.html')
};
});
socials.forEach((button) =>{
  button.onclick = () => {
    location.replace('https://sqdih2.mimo.run/socials.html')
  };
});
source.forEach((button) =>{
  button.onclick = () => {
    location.replace('https://github.com/JustBohdan41k/alltheprojects');
  };
});
website.forEach((button) =>{
  button.onclick = () => {
    location.replace('https://trr5ws.mimo.run/');
  };
});
discord.forEach((button) =>{
  button.onclick = () => {
    location.replace('https://discord.com/invite/VAQhRYfgsB');
  };
});
