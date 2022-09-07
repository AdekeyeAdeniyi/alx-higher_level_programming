#!/usr/bin/node
const dict = require('./100-data').dict;
console.log(dict)

let newDict = {};

for (let [key, value] of Object.entries(dict)) {
    if(!newDict[value]) {
        newDict[value] = [];
        newDict[value].push(key);
    }else {
        newDict[value].push(key);
    }
};

return newDict;