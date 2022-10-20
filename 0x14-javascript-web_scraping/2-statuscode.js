#!/usr/bin/node
/* Print URL `GET` request code status */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode); // Print the response status code if a response was received
  }
});
