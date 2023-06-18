chrome.runtime.sendMessage({method: "getSummary"}, function(response) {
  console.log(response.summary);
  document.getElementById('summary').innerText = response.summary;
});
