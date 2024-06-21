#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = (w !== undefined) ? w : undefined;
    this.height = (h !== undefined) ? h : undefined;
  }
}

module.exports = Rectangle;
