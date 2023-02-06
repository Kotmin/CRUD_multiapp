
// const title = localStorage.getItem('hidden_text');

const inputs = document.querySelector(".inputs"),
resetBtn = document.querySelector(".reset-btn"),
typingInput = document.querySelector(".typing-input");


let text = "Ala ma kota";


function randomText(){
    let html ="";
    for(let i = 0; i< text.length;i++){
        html=`<input type="text" disabled>`;
    }
    inputs.innerHTML = html;
    
}

randomText();

function initGame(e) {
    let key = e.target.value;
    if(key.match(/^[A-Za-z0-9]+$/)){
        console.log(key);
    }
    
}
//16:15 v
resetBtn.addEventListener("click",randomText);
// alert(title);

typingInput.addEventListener("input", initGame);
document.addEventListener("keydown", () => typingInput.focus());