const taskForm = document.getElementById("task-form");
const emailInput = document.getElementById("user-email");
const emailError = document.getElementById("email-error");

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

if (taskForm) {
  taskForm.addEventListener("submit", function (event) {
    const emailValue = emailInput.value.trim();

    if (!emailRegex.test(emailValue)) {
      event.preventDefault();
      emailError.classList.remove("hidden");
    } else {
      emailError.classList.add("hidden");
    }
  });

  emailInput.addEventListener("input", function () {
    emailError.classList.add("hidden");
  });
}