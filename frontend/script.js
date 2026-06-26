const reviewBtn = document.getElementById("reviewBtn");
const codeInput = document.getElementById("codeInput");
const reviewOutput = document.getElementById("reviewOutput");
const loading = document.getElementById("loading");

reviewBtn.addEventListener("click", async () => {

    const code = codeInput.value.trim();

    if(code === ""){
        alert("Please enter Python code.");
        return;
    }

    loading.classList.remove("hidden");
    reviewOutput.textContent = "";

    try{

        const response = await fetch("http://127.0.0.1:8000/review",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                code:code
            })

        });

        const data = await response.json();

        reviewOutput.textContent = data.review;

    }

    catch(error){

        reviewOutput.textContent = "Unable to connect to the backend.";

        console.error(error);

    }

    finally{

        loading.classList.add("hidden");

    }

});