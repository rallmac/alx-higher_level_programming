#!/usr/bin/node

const fs = require('fs');

function concatFiles (file1Path, file2Path, destinationPath) {
  fs.readFile(file1Path, 'utf8', (err, data1) => {
    if (err) {
      console.error(`Error reading file ${file1Path}:`, err);
      return;
    }

    fs.readFile(file2Path, 'utf8', (err, data2) => {
      if (err) {
        console.error(`Error reading file ${file2Path}:`, err);
        return;
      }

      const combinedData = data1 + data2;

      fs.writeFile(destinationPath, combinedData, 'utf8', (err) => {
        if (err) {
          console.error(`Error writing to file ${destinationPath}:`, err);
        }
      });
    });
  });
}

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1Path> <file2Path> <destinationPath>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

concatFiles(file1Path, file2Path, destinationPath);
