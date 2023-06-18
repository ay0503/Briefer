window.onload = function() {
  fetch('http://localhost:3000/summarize', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text: document.body.innerText })
  })
  .then(response => {
    console.log('fetching');
    console.log(response.text());
    return response.text();
  })
  .then(summary => {
    // Store the summary
    chrome.storage.local.set({summary: summary});
  })
  .catch(error => console.error('Error:', error));
};

