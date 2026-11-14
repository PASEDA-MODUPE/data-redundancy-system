const customerForm = document.getElementById("customerForm");
const message = document.getElementById("message");

const API_URL = "https://3zjgzxeyh7ntoljatnku5kaqa40cxztz.lambda-url.us-east-1.on.aws/";

customerForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (!name || !email || !phone) {
        message.textContent = "Please complete all fields.";
        message.style.color = "red";
        return;
    }

    const button = customerForm.querySelector("button");
    button.disabled = true;
    button.textContent = "Registering...";
    message.textContent = "";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, email, phone })
        });

        const result = await response.json();

        message.textContent = result.message;
        message.style.color = result.success ? "green" : "red";

        if (result.success) {
            customerForm.reset();
        }

    } catch (error) {
        message.textContent = "Unable to connect to the server. Please try again.";
        message.style.color = "red";
    } finally {
        button.disabled = false;
        button.textContent = "Register Customer";
    }
});
