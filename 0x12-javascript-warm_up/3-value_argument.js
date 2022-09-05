#!/usr/bin/node
const value = process.argv[2];
console.log(value !== undefined ? value : 'No argument');
