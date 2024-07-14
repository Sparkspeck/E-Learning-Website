const btn = document.querySelector('.side')
const nav = document.querySelector('.nav')
const course1 = document.querySelector('.course1')
const course2 = document.querySelector('.course2')
const course3 = document.querySelector('.course3')
const course4 = document.querySelector('.course4')
const course = document.querySelectorAll('.course-nav')
const add = document.querySelector('.add')
const add1 = document.querySelector('.add1')
btn.addEventListener('click', () => {
    nav.classList.toggle('active')
})

const plus = document.querySelector('.plus')
plus.addEventListener('click', (e) => {
    if (add.classList.toggle('minus'))
        plus.innerHTML = '<i class="fa-solid fa-plus"></i>  Indroduction'
    else
        plus.innerHTML = '<i class="fa-solid fa-minus"></i>  Indroduction'



})

const plus1 = document.querySelector('.plus1')
plus1.addEventListener('click', (e) => {
    if (add1.classList.toggle('minus'))
        plus1.innerHTML = '<i class="fa-solid fa-plus"></i>  Design Basics'
    else
        plus1.innerHTML = '<i class="fa-solid fa-minus"></i>  Design Basics'



})

course1.addEventListener('click', () => {
    document.querySelector('.c1').style.display = 'block'
    document.querySelector('.c2').style.display = 'none'
    document.querySelector('.c3').style.display = 'none'
    document.querySelector('.c4').style.display = 'none'
    course1.classList.add('active')
    course2.classList.remove('active')
    course3.classList.remove('active')
    course4.classList.remove('active')

})
course2.addEventListener('click', () => {
    document.querySelector('.c1').style.display = 'none'
    document.querySelector('.c2').style.display = 'block'
    document.querySelector('.c3').style.display = 'none'
    document.querySelector('.c4').style.display = 'none'

    course2.classList.add('active')
    course1.classList.remove('active')
    course3.classList.remove('active')
    course4.classList.remove('active')


})
course3.addEventListener('click', () => {
    document.querySelector('.c1').style.display = 'none'
    document.querySelector('.c2').style.display = 'none'
    document.querySelector('.c3').style.display = 'block'
    document.querySelector('.c4').style.display = 'none'
    course3.classList.add('active')
    course2.classList.remove('active')
    course1.classList.remove('active')
    course4.classList.remove('active')

})
course4.addEventListener('click', () => {
    document.querySelector('.c1').style.display = 'none'
    document.querySelector('.c2').style.display = 'none'
    document.querySelector('.c3').style.display = 'none'
    document.querySelector('.c4').style.display = 'block'

    course4.classList.add('active')
    course2.classList.remove('active')
    course3.classList.remove('active')
    course1.classList.remove('active')
})