let photos=document.querySelector(".photos")

console.log("hi");
console.log(photos);

// let leftBtn=document.querySelector(".leftSlider");

// let rightBtn=document.querySelector(".rightSlider");


// photos.addEventListener("wheel",(evt)=>{
//     evt.preventDefault();
//     photos.scrollLeft+=evt.deltaY;
//     photos.style.scrollBehavior="auto";
// })

// leftBtn.addEventListener("click",()=>{
//     photos.style.scrollBehavior="smooth";
//     photos.scrollLeft-=5000;
// })

// rightBtn.addEventListener("click",()=>{
//     photos.style.scrollBehavior="smooth";
   
//     photos.scrollLeft+=5000;
// })

let globe=document.getElementById('globeId');

globe.addEventListener('click',function(){
   window.open('https://www.acculizeintech.com/');

})

const faqs = document.querySelectorAll(".faq");


faqs.forEach((faq)=>{
    faq.addEventListener("click", () => {
        faq.classList.toggle("active");
      })
})
