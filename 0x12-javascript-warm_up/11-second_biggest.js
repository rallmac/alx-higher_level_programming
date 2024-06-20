#!/usr/bin/node

const args = process.argv.slice(2);

const numbers = args.map(arg => parseInt(arg, 10)).filter(num => !isNaN(num));

if (numbers.length < 2) {
  console.log('0');
} else {
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const number of numbers) {
    if (number > largest) {
      secondLargest = largest;
      largest = number;
    } else if (number > secondLargest && number < largest) {
      secondLargest = number;
    }
  }

  console.log(`${secondLargest}`);
}
