let openMenu = document.querySelectorAll(".openMenu");
let closeMenu = document.getElementById("closeMenu");
let actions = document.getElementById("actions");
let lastScrollTop = 0;
actions.style.right = "-150%";
actions.style.opacity = "0";
let nav = document.querySelector("nav");
window.addEventListener("scroll", function () {
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  if (scrollTop > lastScrollTop) {
    nav.style.top = "-80px";
  } else {
    nav.style.top = "0px";
  }
  lastScrollTop = scrollTop;
});

openMenu.forEach(function (el) {
  el.addEventListener("click", function () {
    actions.style.opacity = "1";
    actions.style.right = "0";
    nav.style.top = "-80px";
    document.body.classList.add("no_scroll");
  });
});
closeMenu.addEventListener("click", function () {
  actions.style.opacity = "0";
  actions.style.right = "-150%";
  nav.style.top = "0px";
  document.body.classList.remove("no_scroll");
});
let slide_up_message = document.getElementById("slide-up-message");
if (slide_up_message) {
  setTimeout(() => {
    slide_up_message.style.display = "none";
  }, 3000);
}

function visiblePassword(el, password) {
  if (el.classList.contains("fa-eye")) {
    el.classList.remove("fa-eye");
    el.classList.add("fa-eye-slash");
    password.setAttribute("type", "text");
  } else {
    el.classList.remove("fa-eye-slash");
    el.classList.add("fa-eye");
    password.setAttribute("type", "password");
  }
}
