

var delayInMilliseconds = 1000; //1 second

const toggleBtn = document.getElementById("night_theme_toogle");
const theme = document.documentElement.getAttribute("data-theme");
let darkMode = localStorage.getItem("dark");



// document.addEventListener("keydown", e=>{
//   // e.preventDefault();
//   if (e.key.toLowerCase() === "m"
  // && e.ctrlKey //to make combo and change it to ctrl+u
//   ){
//     document.getElementById('night_theme_toogle').click();
//   }
// })


// ctrl+m = switch theme
document.onkeydown = function(evt) {
  evt = evt || window.event;
  if(evt.ctrlKey && evt.keyCode == 77){
    document.getElementById('night_theme_toogle').click();
  }
}


//this is also good but have somme issues with other bindings
// document.addEventListener("keypress", function onPress(event) {
//   if (event.key === "m" ){//&& event.ctrlKey) {
//     document.getElementById('night_theme_toogle').click();
//   }
// });



const enableDarkMode = () => {
  document.documentElement.setAttribute("data-theme","dark");
  toggleBtn.checked= false;
  localStorage.setItem("dark", "enabled");
};

const disableDarkMode = () => {
  document.documentElement.setAttribute("data-theme","light");
  toggleBtn.checked= true;
  localStorage.setItem("dark", "disabled");
};

if (darkMode === "enabled") {
  enableDarkMode(); // set state of darkMode on page load
  
}

toggleBtn.addEventListener("click", (e) => {
  darkMode = localStorage.getItem("dark"); // update darkMode when clicked
  if (darkMode === "disabled") {
    enableDarkMode();
  } else {
    disableDarkMode();
  }
});