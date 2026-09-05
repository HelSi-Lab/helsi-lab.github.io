document.addEventListener("DOMContentLoaded", () => {
  const page = document.querySelector(".research-reference-page");
  if (!page) return;

  const tabs = Array.from(page.querySelectorAll("[data-research-tab]"));
  const panels = Array.from(page.querySelectorAll("[data-research-panel]"));

  const selectPanel = (id) => {
    const selected = panels.some((panel) => panel.dataset.researchPanel === id) ? id : "area";
    panels.forEach((panel) => { panel.hidden = panel.dataset.researchPanel !== selected; });
    tabs.forEach((tab) => {
      const isSelected = tab.dataset.researchTab === selected;
      tab.classList.toggle("active", isSelected);
      tab.setAttribute("aria-selected", String(isSelected));
    });
  };

  const fromHash = () => (window.location.hash || "#area").slice(1);
  selectPanel(fromHash());

  tabs.forEach((tab) => {
    tab.addEventListener("click", (event) => {
      event.preventDefault();
      const id = tab.dataset.researchTab;
      history.replaceState(null, "", `#${id}`);
      selectPanel(id);
    });
  });

  window.addEventListener("hashchange", () => selectPanel(fromHash()));
});
