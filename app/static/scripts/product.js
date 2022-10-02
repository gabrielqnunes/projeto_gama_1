const menuItemElements = document.querySelectorAll('.menu-item')
const allFormElements = document.querySelectorAll('.menu-item form')
const allLinkElements = document.querySelectorAll('.menu-item a')

menuItemElements.forEach((element) => {
    const linkElement = element.querySelector('a')

    linkElement.addEventListener('click', () => {
        const formElement = element.querySelector('form')
        const isFlex = formElement.style.display == 'flex'
        if (isFlex) {
            formElement.style.display = 'none'
            allLinkElements.forEach((element) => element.classList.remove('selected'))
        } else {
            formElement.style.display = 'flex'
            linkElement.classList.add('selected')
            allLinkElements.forEach((element) => {
                if (element != linkElement) {
                    element.classList.remove('selected')
                }
            })
        }
        allFormElements.forEach((element) => {
            if (element != formElement) {
                element.style.display = 'none'
            }
        })



    })
})