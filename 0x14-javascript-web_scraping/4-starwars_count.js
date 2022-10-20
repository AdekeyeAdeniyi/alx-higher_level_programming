#!/usr/bin/node
/*
*
*prints the number of movies where the character “Wedge Antilles”
*ID - 18
*
*/

const request = require('request');
const url = `${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let index = 0;

    for (let i = 0; i < data.length; i++) {
      data[i].characters.forEach(el => {
        if (el.endsWith('18/')) {
          index++;
        }
      });
    }

    console.log(index);
  }
});
