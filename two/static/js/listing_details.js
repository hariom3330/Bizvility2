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



document.getElementById('myForm').addEventListener('submit', function(event) {
  event.preventDefault();
  console.log('Form submission prevented.');

  let text=document.getElementById("textArea").value;
  console.log(text);
  document.getElementById("textArea").value="";


  let parentRevs=document.querySelector(".revs");

  let div1=document.createElement("div");
  let div2=document.createElement("div");

  div2.classList.add("revProf");


  let imageProf=document.createElement("img");
  imageProf.classList.add("profImage")

  imageProf.src="https://img.freepik.com/premium-vector/female-user-profile-avatar-is-woman-character-screen-saver-with-emotions_505620-617.jpg"

  let nameTag=document.createElement("h5");

  nameTag.innerText="Harshita Mahajan";

  div2.appendChild(imageProf);

  div2.appendChild(nameTag);

  div1.appendChild(div2);


  let div3=document.createElement("div");

  div3.innerHTML = `
    <i class="fa-solid fa-star"></i>
    <i class="fa-solid fa-star"></i>
    <i class="fa-solid fa-star"></i>
    <i class="fa-solid fa-star"></i>
    <i class="fa-solid fa-star"></i>
`

div3.classList.add("rateIcon");


div1.appendChild(div3);

let parag=document.createElement("p")

parag.innerText=text;

div1.appendChild(parag);


parentRevs.appendChild(div1);







 
  


});



