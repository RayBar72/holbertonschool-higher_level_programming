#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let tabla = process.argv.slice(2);
  tabla = tabla.map(function (x) {
    return parseInt(x);
  });
  tabla = tabla.sort(function (a, b) {
    return b - a;
  });
  console.log(tabla[1]);
}
