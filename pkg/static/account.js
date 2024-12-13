const accounttoggle = document.getElementById('account-toggle')
const sideaccount = document.getElementById('sideaccount')


accounttoggle.addEventListener('click', ()=>{
    accounttoggle.classList.toggle('active')
    sideaccount.classList.toggle('active')
})