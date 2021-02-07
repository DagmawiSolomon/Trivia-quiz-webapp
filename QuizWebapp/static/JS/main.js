// showMenu('nav-toggle', 'nav-menu')
const showMenu = function () {
    const toggle = document.getElementById("nav-toggle")
    const nav = document.getElementById("nav-menu")
    console.log(nav);
    if(toggle && nav){
        toggle.addEventListener("click",()=>{
            nav.classList.toggle("show")
        })
    }
}
showMenu()
/*==================REMOVE MENU=======================*/
const navLink = document.querySelectorAll('.nav_link')
const navMenu = document.getElementById('nav-menu')

function linkAction(){
    navMenu.classList.remove("show")
}
navLink.forEach(n => n.addEventListener('click', linkAction));

/*close ad*/
closebtn = document.querySelector(".close")
adCard =  document.querySelector(".ads")
closebtn.addEventListener("click", function(){
    adCard.style.display="none"
})

/*copy link*/
// Programmatic copy-to-clipboard
var copyBtn = document.getElementById("copy-btn")
var copiedMsg = document.getElementById("copied-msg")
copyBtn.addEventListener("click",function(){
    function copyText(text) {
        var fakeElement = document.createElement('textarea');
        // Move element out of screen vertically
        fakeElement.style.position = 'fixed';
        fakeElement.style.top = '100%';
        fakeElement.readOnly = true;
        fakeElement.value = "https://nifty-lovelace-c01f87.netlify.app/";
        document.body.appendChild(fakeElement);
    
        fakeElement.select();
        document.execCommand('copy');
    
        document.body.removeChild(fakeElement);
       
    }   
   
    copyText()
})
copyBtn.addEventListener("click", function(){
    copiedMsg.style.display="inline-block"
})


