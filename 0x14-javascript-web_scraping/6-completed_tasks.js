#!/usr/bin/node
/* Computes the number of tasks completed by user id */

const request = require('request');
const url = `${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = {};
    const data = JSON.parse(body);

    data.forEach(el => {
      if (el.completed) {
        results[el.userId] ? results[el.userId] += 1 : results[el.userId] = 1;
      }
    });

    console.log(results);
  }
});
