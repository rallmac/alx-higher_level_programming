#!/usr/bin/node

const fs = require('fs');

// Function to concatenate two files
function concatFiles (file1Path, file2Path, destinationPath) {
  // Read the first file
  fs.readFile(file1Path, 'utf8', (err, data1) => {
    if (err) {
      console.error(`Error reading file ${file1Path}:`, err);
      return;
    }

    // Read the second file
    fs.readFile(file2Path, 'utf8', (err, data2) => {
      if (err) {
        console.error(`Error reading file ${file2Path}:`, err);
        return;
      }

      // Concatenate the contents of the two files
      const combinedData = data1 + data2;

      // Write the combined data to the destination file
      fs.writeFile(destinationPath, combinedData, 'utf8', (err) => {
        if (err) {
          console.error(`Error writing to file ${destinationPath}:`, err);
        }
      });
    });
  });
}

// Ensure the script is being run with the correct number of arguments
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1Path> <file2Path> <destinationPath>');
  process.exit(1);
}

// Get the file paths from the command line arguments
const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

// Call the function with the provided file paths
concatFiles(file1Path, file2Path, destinationPath);
