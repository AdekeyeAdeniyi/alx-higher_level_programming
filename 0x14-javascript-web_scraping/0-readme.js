#!/usr/bin/node
/* Read and print content in a file*/

const fileName = argv[2];
const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
