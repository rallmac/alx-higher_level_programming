#!/usr/bin/node

const args = process.argv.slice(2);

const firstArg = args[0];
const num = parseInt(firstArg, 10);

if (!isNaN(num)) {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
