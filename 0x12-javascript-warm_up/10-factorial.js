#!/usr/bin/node

const x = parseInt(process.argv[2]);
let y = 1;
for (let i = 1; i <= x; i++) {
  y *= i;
}
console.log(y);
