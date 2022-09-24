#!/usr/bin/node
const fs = require('fs')
const filesPath = [process.argv[2], process.argv[3]];
const outputFile = process.argv[4]

filesPath.forEach(file => {
    fs.readFile(file, (err, inputD) => {
       if (err) throw err;
          if(inputD.toString()){
            fs.appendFile(outputFile, `${inputD.toString()}\n`, function (err) {
                if (err) throw err;
            });
          }
    })
})