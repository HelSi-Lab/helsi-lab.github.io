// simple photo carousel for news items
window.addEventListener("load", () => {
  document.querySelectorAll("[data-carousel]").forEach((box) => {
    const slides = box.querySelectorAll(".news-slide");
    const dots = box.querySelectorAll(".news-dot");
    if (slides.length < 2) return;
    let i = 0;
    const show = (n) => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => s.classList.toggle("is-active", k === i));
      dots.forEach((d, k) => d.classList.toggle("is-active", k === i));
    };
    box.querySelector(".news-prev").addEventListener("click", () => show(i - 1));
    box.querySelector(".news-next").addEventListener("click", () => show(i + 1));
    dots.forEach((d, k) => d.addEventListener("click", () => show(k)));
  });
});
