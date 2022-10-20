#!/usr/bin/node

/* Print all characters in a movie API */

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charactersUrl = JSON.parse(body).characters;
    charactersUrl.forEach(url => {
      request(url, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
