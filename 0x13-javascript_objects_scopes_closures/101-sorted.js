#!/usr/bin/node

const dict = require('./101-data').dict;

const nDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!nDict[occurrences]) {
    nDict[occurrences] = [];
  }
  nDict[occurrences].push(userId);
}

function customStringify (obj) {
  let result = '{ ';
  const entries = Object.entries(obj);
  for (let i = 0; i < entries.length; i++) {
    const [key, value] = entries[i];
    result += `'${key}': [ '${value.join("', '")}' ]`;
    if (i < entries.length - 1) {
      result += ', ';
    }
  }
  result += ' }';
  return result;
}

console.log(customStringify(nDict));
