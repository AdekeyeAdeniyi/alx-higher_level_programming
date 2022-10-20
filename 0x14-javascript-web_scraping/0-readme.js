#!/usr/bin/node
/* Read and print content in a file*/
const fs = require('fs/promises');
const { argv } = require('process');
const path = require('path');

const fileName = argv[2];

async function readFile (filename) {
  try {
    const data = await fs.readFile(
      path.join(__dirname, `${filename}`),
      { encoding: 'utf8' }
    );
    console.log(data);
  } catch (err) {
    console.log(err);
  }
}

readFile(fileName);
