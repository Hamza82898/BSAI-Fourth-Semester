function sendMessage() {
    let userInput = document.getElementById("user-input").value;

    if (userInput.trim() === "") return;

    addMessage(userInput, "user-message");

    fetch("/get", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "message=" + userInput
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "bot-message");
    });

    document.getElementById("user-input").value = "";
}

function addMessage(text, className) {
    let chatWindow = document.getElementById("chat-window");
    let message = document.createElement("div");
    message.className = className;
    message.innerText = text;
    chatWindow.appendChild(message);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
