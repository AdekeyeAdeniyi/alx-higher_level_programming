#!/usr/bin/node
let counter = parseInt(process.argv[2]);
if (isNaN(counter)) {
  console.log('Missing number of occurrences');
} else {
  while (counter > 0) {
    console.log('C is fun');
    counter--;
  }
}
