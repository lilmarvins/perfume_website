const hamburger = document.querySelector(".hamburger")
const navmenu = document.querySelector(".nav-menu")
const perfumemodal =document.getElementById('perfumemodal')
const store = document.getElementById('store')
const close = document.querySelector(".close")
const searchicon = document.getElementById("searchicon")
const searchmodal = document.getElementById('search-modal')


searchicon.addEventListener("click", ()=>{
    searchmodal.style.display = searchmodal.style.display === "flex" ? "none" : 'flex'
    
})

hamburger.addEventListener("click", ()=>{
    hamburger.classList.toggle("active");
    navmenu.classList.toggle("active");
})

store.addEventListener("click", ()=>{
    store.classList.add("active");
    perfumemodal.classList.add("active");
})

close.addEventListener('click', ()=>{
    perfumemodal.classList.remove("active");
    navmenu.classList.toggle("active");
    hamburger.classList.toggle("active");



})
document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click",()=>{
    hamburger.classList.remove("active")
    navmenu.classList.remove("active")
}))


document.addEventListener("click", (event)=>{
    const clickedinside = perfumemodal.contains(event.target) || event.target === store;
    if(!clickedinside) {
        perfumemodal.classList.remove("active")
    }
})

window.addEventListener('scroll', reveal);
function reveal(){
    var reveals = document.querySelectorAll('.reveal')
    for(var i=0; i < reveals.length; i++){
        var windoweight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealpoint = 150;
        if ( revealtop < windoweight - revealpoint){
            reveals[i].classList.add('active');
        }
        else{
            reveals[i].classList.remove('active');

        }
    }
}


document.querySelectorAll('.fourth-child').forEach((element, index) =>{
    element.style.animationDelay = `${index *0.3}s`
})


document.getElementById('year').textContent= new Date().getFullYear();



// Get elements
const svg = document.getElementById("account");
const modal = document.getElementById("accountmodal");


// Toggle modal visibility on click
svg.addEventListener("click", () => {
 modal.classList.toggle('active')
});

window.addEventListener("click", (event) => {
  if (!modal.contains(event.target) && event.target !== svg) {
    modal.classList.remove('active')
  }

});