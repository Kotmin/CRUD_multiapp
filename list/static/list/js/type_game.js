
// const title = localStorage.getItem('hidden_text');

const inputs = document.querySelector(".inputs"),
resetBtn = document.querySelector(".reset-btn"),
gameBoard = document.querySelector(".board"),
orginalTask = document.querySelector(".result"),
guessLeft = document.querySelector(".guess-left span"),
wrongLetter = document.querySelector(".wrong-letters span"),
typingInput = document.querySelector(".typing-input");

//  Just for testing purposes
// let input_text= "Ala ma kota, ale nie ma żółwia.";

let input_text = plain_text;
let text = ""
// text = "ala";

let working_text = input_text.split(' ');

let incorrects = [];
let corrects = [];


let maxGuesses = 10;

let howManyHidden = 3,
randomIndex = [],
temp ="",
randomIntHolder=0,
i=0,
actualBoard = [],
iteration = 0;

// alert(plain_text);

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function generateHashedWordReplacement(word){
    temp =""
    for (let i = 0; i < word.length; i++) {
        temp +="_";
    }
    return temp;
}

function prepareBoard(){
    iteration=0;
    if (working_text.length<3) {
        howManyHidden = (working_text.length-1) ;
    }
    while(i<howManyHidden) {
        randomIntHolder=getRandomInt(working_text.length);
        if (working_text[randomIntHolder].includes("/[,;.]/g") || randomIndex.includes(randomIntHolder)) {
            continue;
        }
        randomIndex.push(randomIntHolder);
        i++;
    }
    for (i = 0; i < working_text.length; i++) {
        if (randomIndex.includes(i)) {
            actualBoard.push(generateHashedWordReplacement(working_text[i]));
        }
        else{
            actualBoard.push(working_text[i])
        }   
    }     
}
console.log(randomIndex);
console.log(actualBoard);


function showBoard(){
    let board ="";
    console.log(actualBoard);
    for (let i = 0; i < actualBoard.length; i++) {
        board += actualBoard[i] + " ";
    }
    gameBoard.innerText = board;
}

function showOrginal(){
    orginalTask.innerText = input_text;
}

function updateBoard(){
    if(howManyHidden<1){
        showOrginal();
        actualBoard[randomIndex[iteration]]=working_text[randomIndex[iteration]];
        showBoard();
    }
    else{
        actualBoard[randomIndex[iteration]]=working_text[randomIndex[iteration]];
        iteration++;
        showBoard();
        text=working_text[randomIndex[iteration]];
        randomText();
    }

}

function randomText(){

    guessLeft.innerText = maxGuesses;
    incorrects = [];
    corrects = [];

    let html ="";
    for(let i = 0; i< text.length;i++){
        html +=`<input type="text" style="width: 15em" disabled>`;
    }
    inputs.innerHTML = html;
    
}

function restart(){
    incorrects = [];
    corrects = [];
    maxGuesses = 10;

    howManyHidden = 3,
    randomIndex = [],
    temp ="",
    randomIntHolder=0,
    i=0,
    actualBoard = [],
    iteration = 0;

    prepareBoard();
    showBoard();

    randomText();
}

prepareBoard();
showBoard();

randomText();
// showOrginal(); fine


function initGame(e) {
    let key = e.target.value;
    if(key.match(/^[A-Za-z0-9żźćńłą;\.\,]+$/) && !incorrects.includes(` ${key}`)
    && !corrects.includes(key)){
        console.log(key);
        if(text.includes(key)) {
            for (let i = 0; i < text.length; i++) {
                if (text[i] === key) {
                    corrects.push(key);
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
    if (corrects.length === text.length) {
        //congrats you did it
        howManyHidden--;
        updateBoard();
        
    }
    if (maxGuesses < 1) {
        for (let i = 0; i < text.length; i++) {
            inputs.querySelectorAll("input")[i].value = text[i];
            howManyHidden--;
            updateBoard();
        }
    }
}



resetBtn.addEventListener("click",restart);
// alert(title);

typingInput.addEventListener("input", initGame);
document.addEventListener("keydown", () => typingInput.focus());