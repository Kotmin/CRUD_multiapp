

var delayInMilliseconds = 1000; //1 second

const toggleBtn = document.getElementById("night_theme_toogle");
const theme = document.documentElement.getAttribute("data-theme");
let darkMode = localStorage.getItem("dark");



document.addEventListener("keydown", e=>{
  e.preventDefault();
  if (e.key.toLowerCase() === "u"
      // && e.ctrlKey //to make combo and change it to ctrl+u
  
  ){
    alert("U has been pressed");
  }
})


document.addEventListener("keydown", e=>{
  e.preventDefault();
  if (e.key.toLowerCase() === "m"
  
  ){
    document.getElementById('night_theme_toogle').click();
  }
})

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