let valueDisplays = document.querySelectorAll(".num");
let interval = 400;

valueDisplays.forEach((valueDisplay) => {
  let startValue = 0;
  let endValue = parseInt(valueDisplay.getAttribute("data-val"));
  let duration = Math.floor(interval / endValue);
  let counter = setInterval(function () {
    startValue += 1;
    valueDisplay.textContent = startValue;
    if (startValue == endValue) {
      clearInterval(counter);
    }
  }, duration);
});



/*=============== ACCORDION ===============*/
const accordionItems = document.querySelectorAll('.accordion__item')

// 1. Selecionar cada item
accordionItems.forEach((item) =>{
    const accordionHeader = item.querySelector('.accordion__header')

    // 2. Seleccionar cada click del header
    accordionHeader.addEventListener('click', () =>{
        // 7. Crear la variable
        const openItem = document.querySelector('.accordion-open')

        // 5. Llamar a la funcion toggle item
        toggleItem(item)

        // 8. Validar si existe la clase
        if(openItem && openItem!== item){
            toggleItem(openItem)
        }
    })
})

// 3. Crear una funcion tipo constante
const toggleItem = (item) =>{
    // 3.1 Crear la variable
    const accordionContent = item.querySelector('.accordion__content')

    // 6. Si existe otro elemento que contenga la clase accorion-open que remueva su clase
    if(item.classList.contains('accordion-open')){
        accordionContent.removeAttribute('style')
        item.classList.remove('accordion-open')
    }else{
        // 4. Agregar el height maximo del content
        accordionContent.style.height = accordionContent.scrollHeight + 'px'
        item.classList.add('accordion-open')
    }
}





// $.fn.randomize = function(selector){
//       var $elems = selector ? $(this).find(selector) : $(this).children(),
//       $parents = $elems.parent();
//
//       $parents.each(function(){
//         $(this).children(selector).sort(function(){
//             return Math.round(Math.random()) - 0.5;
//         }).detach().appendTo(this);
//       });
//
//       return this;
//     };


// let slideIndex = 0;
// showSlides();
//
// function showSlides() {
//   let i;
//   let slides = document.getElementsByClassName("content-area");
//   let dots = document.getElementsByClassName("dot");
//
//   // onInitialize : function(){
//   //  $(slides).randomize();
//   // }
//
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   slideIndex++;
//
//   if (slideIndex > slides.length) {slideIndex = 1}
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" active", "");
//   }
//
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " active";
//
//   setTimeout(showSlides, 4000); // Change image every 2 seconds
// }