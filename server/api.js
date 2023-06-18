const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

app.get('/summarize', (req, res) => {
  const text = req.body.text;

  // Here you would typically call a function to summarize the text.
  // For simplicity, we'll just return the first 100 characters.
  const summary = "text.substring(0, 100)";

  res.send(summary);
});

app.listen(3000, () => console.log('Server listening on port 3000'));
