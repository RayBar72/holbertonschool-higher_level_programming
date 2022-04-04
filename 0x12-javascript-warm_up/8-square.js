#!/usr/bin/node

const largo = process.argv.len;
let impresion = '';
if (largo < 3 || !parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    impresion += 'X';
  }
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(impresion);
  }
}
