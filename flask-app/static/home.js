/*------ javascript --------*/

const context = document.querySelector(".context");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

context.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  links.forEach(link => {
    link.classList.toggle("fade");
  });
});

/*---------------------------*/
