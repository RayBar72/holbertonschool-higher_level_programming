#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let impresion = '';
    for (let i = 0; i < this.width; i++) {
      impresion += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(impresion);
    }
  }

  rotate () {
    const x = this.width;
    const y = this.height;
    this.width = y;
    this.height = x;
  }

  double () {
    const x = this.width * 2;
    const y = this.height * 2;
    this.width = x;
    this.height = y;
  }
}

module.exports = Rectangle;
