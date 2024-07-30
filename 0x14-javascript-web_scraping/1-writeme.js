#!/usr/bin/node

const fs = require('fs');

// Get the file path and the string to write from the command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if both the file path and the string to write are provided
if (!filePath || !stringToWrite) {
  console.error('Please provide a file path as the first argument and a string to write as the second argument.');
  process.exit(1);
}

// Write the string to the file in UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to the file:', err);
  }
});
