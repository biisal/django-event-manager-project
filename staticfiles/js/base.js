let openMenu = document.querySelectorAll(".openMenu");
let closeMenu = document.getElementById("closeMenu");
let actions = document.getElementById("actions");
let body = document.querySelector("main");
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
    body.classList.add("no_scroll");
  });
});
closeMenu.addEventListener("click", function () {
  actions.style.opacity = "0";
  actions.style.right = "-150%";
  nav.style.top = "0px";
  body.classList.remove("no_scroll");
});
