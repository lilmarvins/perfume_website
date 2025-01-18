document.getElementById('year').textContent= new Date().getFullYear();


hamburger= document.querySelector('.hamburger')
sidebar= document.querySelector('.side-bar')
hamburger.addEventListener("click", () => {
    sidebar.classList.toggle('active')
   });