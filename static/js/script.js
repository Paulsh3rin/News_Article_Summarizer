document.getElementById('summarizeButton').addEventListener('click', async () => {
    const articleText = document.getElementById('articleInput').value;
    if (!articleText) {
        alert('Please paste an article to summarize.');
        return;
    }

    try {
        const response = await fetch('https://ai-2004-project.onrender.com', {
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

        //Display Summary
        const summaryElement =  document.getElementById('summaryOutput');
        summaryElement.innerText = ''; //clear previous summary
        summaryElement.innerText = data.summary;

        // Display the keywords as hashtags
        const keywordsElement = document.getElementById('keywordsOutput');
        keywordsElement.innerHTML = ''; // Clear previous keywords
        data.keywords.forEach(keyword => {
            const hashtag = document.createElement('span');
            hashtag.className = 'hashtag';
            hashtag.innerText = keyword;
            keywordsElement.appendChild(hashtag);
        });
    } catch (error) {
        console.error('Error:', error);
        alert('There was an error summarizing the article.');
    }
});

document.getElementById('resetButton').addEventListener('click', () => {
    document.getElementById('articleInput').value = '';
    document.getElementById('keywordsOutput').innerHTML = '';
    document.getElementById('summaryOutput').innerText = '';
});
