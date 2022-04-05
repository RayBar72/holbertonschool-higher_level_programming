#!/usr/bin/node

const implist = require('./100-data').list;

const plist = implist.map((element, index) => element * index);
console.log(implist);
console.log(plist);
