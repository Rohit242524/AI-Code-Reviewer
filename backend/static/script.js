const reviewBtn = document.getElementById("reviewBtn");
const codeInput = document.getElementById("codeInput");
const reviewOutput = document.getElementById("reviewOutput");
const loading = document.getElementById("loading");

reviewBtn.addEventListener("click", async () => {

    const code = codeInput.value.trim();

    if (code === "") {
        alert("Please enter Python code.");
        return;
    }

    loading.classList.remove("hidden");
    reviewOutput.textContent = "";

    try {

        const response = await fetch("/review", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        });

        if (!response.ok) {
            throw new Error("Server returned an error.");
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {

            const { done, value } = await reader.read();

            if (done) {
                break;
            }

            reviewOutput.textContent += decoder.decode(value, { stream: true });

        }

    } catch (error) {

        reviewOutput.textContent =
            "An error occurred while reviewing the code.";

        console.error(error);

    } finally {

        loading.classList.add("hidden");

    }

});