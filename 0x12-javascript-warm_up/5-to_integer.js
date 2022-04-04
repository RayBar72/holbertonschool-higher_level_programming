#!/usr/bin/node

largo = process.argv.len;
if (largo < 3 || !parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
