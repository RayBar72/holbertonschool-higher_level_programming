#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let impresion = '';
    for (let i = 0; i < this.width; i++) {
      impresion += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(impresion);
    }
  }
}

module.exports = Square;
