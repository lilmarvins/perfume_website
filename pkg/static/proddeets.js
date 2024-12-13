// Get the elements
const decrementBtn = document.getElementById("decrement");
const incrementBtn = document.getElementById("increment");
const quantityInput = document.getElementById("quantity");

// Add click event for decrement button
decrementBtn.addEventListener("click", () => {
  let currentValue = parseInt(quantityInput.value);
  if (currentValue > parseInt(quantityInput.min)) {
    quantityInput.value = currentValue - 1;
  }
});

// Add click event for increment button
incrementBtn.addEventListener("click", () => {
  let currentValue = parseInt(quantityInput.value);
  quantityInput.value = currentValue + 1;
});