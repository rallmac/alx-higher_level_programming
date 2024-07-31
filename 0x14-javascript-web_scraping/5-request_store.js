#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and the file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both the URL and the file path are provided
if (!url || !filePath) {
  console.error('Please provide a URL as the first argument and a file path as the second argument.');
  process.exit(1);
}

// Make the request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch the webpage. Status code: ${response.statusCode}`);
    return;
  }

  // Write the body of the response to the file in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to the file:', err);
    }
  });
});
