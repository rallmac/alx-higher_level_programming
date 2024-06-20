#!/usr/bin/node

const args = process.argv.slice(2);

const firstArg = args[0];
const num = parseInt(firstArg, 10);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log(`Not a number`);
}
