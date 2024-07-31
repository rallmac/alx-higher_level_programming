#!/usr/bin/node

const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Check if the URL is provided
if (!url) {
  console.error('Please provide a URL as the first argument.');
  process.exit(1);
}

// Make the GET request to the URL
request(url, (error, response) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
