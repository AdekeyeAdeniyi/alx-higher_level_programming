#!/usr/bin/node
const integer = parseInt(process.argv[2]);
console.log(isNaN(integer) ? 'Not a number' : 'My number: ' + integer);
