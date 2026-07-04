const reviewBtn = document.getElementById("reviewBtn");
const folderInput = document.getElementById("folderInput");
const codeInput = document.getElementById("codeInput");
const reviewOutput = document.getElementById("reviewOutput");
const loading = document.getElementById("loading");

const ignoredFolders = [
    "venv",
    "__pycache__",
    ".git",
    "node_modules",
    "dist",
    "build"
];

const ignoredExtensions = [
    ".pyc",
    ".log",
    ".db",
    ".sqlite",
    ".env",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".pdf",
    ".zip",
    ".exe",
    ".dll",
    ".so"
];

reviewBtn.addEventListener("click", async () => {

    const formData = new FormData();

    if (folderInput.files.length > 0) {

        let pythonFiles = 0;

        for (const file of folderInput.files) {

            const path = file.webkitRelativePath || file.name;

            if (ignoredFolders.some(folder => path.split("/").includes(folder))) {
                continue;
            }

            if (ignoredExtensions.some(ext => path.endsWith(ext))) {
                continue;
            }

            if (!path.endsWith(".py")) {
                continue;
            }

            formData.append("files", file);
            pythonFiles++;
        }

        if (pythonFiles === 0) {
            alert("No Python files found in the selected folder.");
            return;
        }

    } else {

        const code = codeInput.value.trim();

        if (code === "") {
            alert("Please upload a project folder or paste Python code.");
            return;
        }

        formData.append("code", code);
    }

    loading.classList.remove("hidden");
    reviewOutput.textContent = "";

    try {
        const response = await fetch("/review", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {

            const error = await response.text();
            throw new Error(error);

        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {

            const { done, value } = await reader.read();

            if (done) {
                break;
            }

            reviewOutput.textContent += decoder.decode(value, {
                stream: true
            });

        }

    } catch (error) {

        reviewOutput.textContent = error.message;
        console.error(error);

    } finally {

        loading.classList.add("hidden");

    }

});