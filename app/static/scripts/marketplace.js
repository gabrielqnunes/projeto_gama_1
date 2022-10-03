const listItemsElements = document.querySelectorAll('.product-list-item')
console.log(listItemsElements)

listItemsElements.forEach((element) => {
    const minusButtonElement = element.querySelector('.b-minus')
    const plusButtonElement = element.querySelector('.b-plus')
    const quantity = element.querySelector('.product-quantity')

    minusButtonElement.addEventListener('click', () => {
        if (parseInt(quantity.textContent) > 0) {
            quantity.textContent = (parseInt(quantity.textContent) - 1).toString()
        }
    })

    plusButtonElement.addEventListener('click', () => {
        quantity.textContent = (parseInt(quantity.textContent) + 1).toString()
    })
})

