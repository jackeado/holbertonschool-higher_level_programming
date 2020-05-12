#!/usr/bin/node

const SquareBase = require('./5-square.js');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
