document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('scrapeButton').addEventListener('click', function() {
        fetch('/run-scraper', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: 'file:///C:/Users/ANUSHKA%20PANDEY/OneDrive/Documents/WindowsPowerShell/fashion_article.html' })  // Replace with the URL you want to scrape
        })
        .then(response => response.json())
        .then(data => {
            console.log('Scrape successful:', data);
            if (data.output) {
                alert('Scraping completed:\n' + data.output);  // Display the output from the scraper
            } else if (data.error) {
                alert('Error during scraping:\n' + data.error);  // Display any errors
            }
        })
        .catch(error => {
            console.error('Error during scraping:', error);
        });
    });
});
