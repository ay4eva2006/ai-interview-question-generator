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

        const raw = data.questions || "";

        const lines = raw
            .split(/\n|•|-/)
            .map(q => q.trim())
            .filter(q => q.length > 0);

        result.innerHTML = `
            <h3>Generated Questions</h3>
            <ol>
                ${lines.map(q =>
                    `<li>${q.replace(/^\d+\.\s*/, "")}</li>`
                ).join("")}
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

console.log("RESPONSE:", response);
console.log("DATA:", data);