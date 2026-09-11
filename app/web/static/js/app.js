const dateButton = document.getElementById("date-button");
const demo = document.getElementById("demo");

dateButton.addEventListener("click", () => {
    demo.textContent = new Date().toString();
});
