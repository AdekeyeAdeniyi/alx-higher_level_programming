#!/usr/bin/node
const dict = require('./100-data').dict;
console.log(dict);

const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!newDict[value]) {
    newDict[value] = [];
    newDict[value].push(key);
  } else {
    newDict[value].push(key);
  }
}

console.log(newDict);
