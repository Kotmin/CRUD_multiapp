
// const title = localStorage.getItem('hidden_text');

const inputs = document.querySelector(".inputs"),
resetBtn = document.querySelector(".reset-btn"),
orginalTask = document.querySelector(".result"),
guessLeft = document.querySelector(".guess-left span"),
wrongLetter = document.querySelector(".wrong-letters span"),
typingInput = document.querySelector(".typing-input");

 

let text = "Ala ma kota, ale nie ma żółwia.";
// text = "ala";

let working_text = text.split(' ');

console.log(working_text);

console.log(working_text[0]);

console.log(working_text[1]);

console.log(working_text[2]);



let incorrects = [];


let maxGuesses = 10;

let howManyHidden = 3,
randomIndex = [],
temp ="",
randomIntHolder=0,
i=0;



function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function prepareBoard(){
    while(i<howManyHidden) {
        randomIntHolder=getRandomInt(working_text.length);
        if (working_text[randomIntHolder].includes("/[,;.]/g") || randomIndex.includes(randomIntHolder)) {
            continue;
        }
        randomIndex.push(randomIntHolder);
        i++;
    }

}
console.log(randomIndex);
prepareBoard();

function showBoard(){

}

function showOrginal(){
    orginalTask.innerText = text;
}

function randomText(){

    guessLeft.innerText = maxGuesses;

    let html ="";
    for(let i = 0; i< text.length;i++){
        html +=`<input type="text" disabled>`;
    }
    inputs.innerHTML = html;
    
}

randomText();


function initGame(e) {
    let key = e.target.value;
    if(key.match(/^[A-Za-z0-9;\.\,]+$/) && !incorrects.includes(` ${key}`)){
        console.log(key);
        if(text.includes(key)) {
            for (let i = 0; i < text.length; i++) {
                if (text[i] === key) {
                    inputs.querySelectorAll("input")[i].value = key;
                }
            }
        }
        else{
            // console.log("letter not found");
            maxGuesses--;
            incorrects.push(` ${key}`);
        }
        guessLeft.innerText = maxGuesses;
        wrongLetter.innerText = incorrects;
    }
    typingInput.value ="" ;

    if (maxGuesses < 1) {
        for (let i = 0; i < text.length; i++) {
            inputs.querySelectorAll("input")[i].value = text[i];
        }
        showOrginal();
    }
}
//16:15 v
resetBtn.addEventListener("click",randomText);
// alert(title);

typingInput.addEventListener("input", initGame);
document.addEventListener("keydown", () => typingInput.focus());