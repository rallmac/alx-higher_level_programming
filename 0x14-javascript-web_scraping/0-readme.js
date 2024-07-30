#!/usr/bin/node

const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('Please provide a file path as the first argument.');
  process.exit(1);
}

// Read the file content in UTF-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }
  console.log(data);
});
