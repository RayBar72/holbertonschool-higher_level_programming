#!/usr/bin/node

const largo = process.argv.len;
if (largo < 3 || !parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
