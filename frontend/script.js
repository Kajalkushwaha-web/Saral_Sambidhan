function toggleChat() {
    const box = document.getElementById("chatBox");
    box.classList.toggle("active");

    if (box.classList.contains("active")) {
        document.getElementById("userText").focus();
    }
}

async function sendMessage() {
    const textInput = document.getElementById("userText");
    const responseBox = document.getElementById("chatResponse");
    const query = textInput.value.trim();

    if (!query) return;

    responseBox.classList.remove("hidden");
    responseBox.innerHTML = `<div style="color:#666;font-size:0.9rem;">AI is thinking...</div>`;

    try {
        const response = await fetch("http://127.0.0.1:8000/api/explain", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: query })
        });

        const data = await response.json();

        responseBox.innerHTML = `
            <div style="font-weight:700;color:var(--primary-red);font-size:0.8rem;">AI EXPLANATION</div>
            <div>${data.explaination.replace(/\n/g, "<br>")}</div>
        `;

        textInput.value = "";

    } catch (error) {
        responseBox.innerHTML = `<b style="color:red;">Backend not running on port 8000</b>`;
    }
}

document.addEventListener('keydown', (e) => {
    const textInput = document.getElementById("userText");
    if (e.key === "Enter" && !e.shiftKey && document.activeElement === textInput) {
        e.preventDefault();
        sendMessage();
    }
});
