chrome.runtime.sendMessage({method: "getSummary"}, function(response) {
  document.getElementById('summary').innerText = response.summary;
});
