document.getElementById('summarizeButton').addEventListener('click', async () => {
    const articleText = document.getElementById('articleInput').value;
    if (!articleText) {
        alert('Please paste an article to summarize.');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ article: articleText })
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        document.getElementById('summaryOutput').innerText = data.summary;
    } catch (error) {
        console.error('Error:', error);
        alert('There was an error summarizing the article.');
    }
});