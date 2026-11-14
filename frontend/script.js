const customerForm = document.getElementById("customerForm");
const message = document.getElementById("message");

customerForm.addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (!name || !email || !phone) {
        message.textContent = "Please complete all fields.";
        message.style.color = "red";
        return;
    }

    message.textContent = "Registration form submitted successfully. Backend connection is not yet configured.";
    message.style.color = "green";

    customerForm.reset();
});
