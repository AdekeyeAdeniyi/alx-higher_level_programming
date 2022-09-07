#!/usr/bin/node
const dict = require('./100-data').dict;
const newDict = {};

for (const key in dict) {
  if (!newDict[dict[key]]) {
    newDict[dict[key]] = [];
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]].push(key);
  }
}

console.log(newDict);
