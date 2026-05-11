async function generateQuestions() {

    const jobTitle = document.getElementById("jobTitle").value;
    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    loading.style.display = "block";
    result.innerHTML = "";

    try {

        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                job_title: jobTitle
            })
        });

        const data = await response.json();

        loading.style.display = "none";

        if (data.error) {
            result.innerHTML = `
                <p style="color:red;">
                    Error: ${data.error}
                </p>
            `;
            return;
        }
        
        result.innerHTML = `
        <h3>Generated Questions</h3>
        <ol>
            ${data.questions
            .split("\n")
            .filter(q => q.trim())
            .map(q => `<li>${q.replace(/^\d+\.\s*/, "")}</li>`)
            .join("")}
        </ol>
        `;
      
        

    } catch (error) {

        loading.style.display = "none";

        result.innerHTML = `
            <p style="color:red;">
                Something went wrong.
            </p>
        `;
    }
}