#!/usr/bin/node
/* Print movies title from API call */

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const { title } = JSON.parse(body);
    console.log(title); // Print movie `title`
  }
});
