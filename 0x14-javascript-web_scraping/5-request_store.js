#!/usr/bin/node
/* Gets the contents of a webpage and stores it in a file */

const request = require('request');
const fs = require('fs');
const url = `${process.argv[2]}`;
const filePath = `${process.argv[3]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
