const cart_click=document.querySelector('#cart')
const cart_click2=document.querySelector('#cart1')

const cart=document.querySelector('.cart-popup')

cart_click.addEventListener('click',()=>{
    cart.classList.toggle('remove-popup')
})

cart_click2.addEventListener('click',()=>{
    cart.classList.remove('remove-popup')
})
