#!/usr/bin/node

const argumento = process.argv;
const largo = argumento.length;
if (largo < 3) {
  console.log('No argument');
} else if (largo > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
