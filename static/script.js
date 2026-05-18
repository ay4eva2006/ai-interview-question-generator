async function generateQuestions() {
    const jobTitle = document.getElementById('jobTitle').value;
    const resultDiv = document.getElementById('result');
    const loading = document.getElementById('loading');

    if (!jobTitle) return;

    loading.style.display = 'block';
    resultDiv.innerHTML = '';

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ job_title: jobTitle }),
        });

        const data = await response.json();
        const aiText = data.questions.trim();

        // 1. CHECK FOR THE NARROWING GUARDRAIL
        if (aiText.includes("[INVALID]") || aiText.length < 5) {
            resultDiv.innerHTML = `
                <div class="error-box">
                    <strong>Invalid Job Title:</strong> 
                    "${jobTitle}" is not a recognized professional career. Please enter a real job title.
                </div>`;
            return;
        }

        // 2. THE BROKEN LINE FIX: Split ONLY by double newlines
        // This prevents sentences from breaking into separate boxes
        const questions = aiText.split(/\n\s*\n/);

        resultDiv.innerHTML = questions
            .slice(0, 3) 
            .map(q => {
                // Remove numbers (1., 2., etc.) if the AI accidentally adds them
                const cleanQuestion = q.replace(/^\d+[\.\)]\s*/, '').trim();
                return `<div class="question-block">${cleanQuestion}</div>`;
            })
            .join('');

    } catch (error) {
        resultDiv.innerHTML = '<p class="error">System error connecting to AI.</p>';
    } finally {
        loading.style.display = 'none';
    }
}