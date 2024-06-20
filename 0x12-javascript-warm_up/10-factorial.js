#!/usr/bin/node

const args = process.argv.slice(2);

const firstArg = args[0];
const n = parseInt(firstArg, 10);

function factorial(n) {
  if (n === 0) {
    return n = 1;
}

return n * factorial(n - 1);
}

if (!isNaN(n)) {
  const result  = factorial(n);
  console.log(`${result}`);
} else {
  console.log(`1`);
}
