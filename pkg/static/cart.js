// Get the elements
const decrementBtn = document.querySelectorAll(".decrement");
const incrementBtn = document.querySelectorAll(".increment");

// Add click event for decrement button
incrementBtn.forEach(button =>{
    button.addEventListener('click', ()=>{
        const cartitem = button.parentElement;
        const quantityInput = cartitem.querySelector('.quantity-input')
quantityInput.value = parseInt(quantityInput.value) + 1;      
    })
})


decrementBtn.forEach(button =>{
    button.addEventListener('click', ()=>{
        const cartitem = button.parentElement;
        const quantityInput = cartitem.querySelector('.quantity-input')
        let currentquantity = parseInt(quantityInput.value)
        if( currentquantity > 0){
            quantityInput.value = currentquantity -1
        }
    })
})
