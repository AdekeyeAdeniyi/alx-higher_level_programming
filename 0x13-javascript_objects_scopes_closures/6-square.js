#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let row = this.height; row > 0; row--) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
