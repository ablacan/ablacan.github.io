// Turns every <span class="email" data-u="..." data-d="..."> (see _includes/email.html)
// into a clickable email link. User and domain are stored reversed in the page
// so that spam bots reading the HTML do not find the address.
document.addEventListener("DOMContentLoaded", function () {
  var flip = function (s) { return s.split("").reverse().join(""); };
  document.querySelectorAll(".email[data-u]").forEach(function (el) {
    var address = flip(el.dataset.u) + "@" + flip(el.dataset.d);
    var link = document.createElement("a");
    link.href = "mailto:" + address;
    link.textContent = address;
    el.replaceChildren(link);
  });
});
