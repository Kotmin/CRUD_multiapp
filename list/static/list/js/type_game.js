
// const title = localStorage.getItem('hidden_text');

const inputs = document.querySelector(".inputs"),
resetBtn = document.querySelector(".reset-btn"),
typingInput = document.querySelector(".typing-input");


let text = "Ala ma kota";
// text = "ala";


function randomText(){
    let html ="";
    for(let i = 0; i< text.length;i++){
        html +=`<input type="text" disabled>`;
    }
    inputs.innerHTML = html;
    
}

randomText();

function initGame(e) {
    let key = e.target.value;
    if(key.match(/^[A-Za-z0-9]+$/)){
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
            console.log("letter not found");
        }
    }
    typingInput.value ="" 
}
//16:15 v
resetBtn.addEventListener("click",randomText);
// alert(title);

typingInput.addEventListener("input", initGame);
document.addEventListener("keydown", () => typingInput.focus());