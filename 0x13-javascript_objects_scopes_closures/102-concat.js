#!/usr/bin/node

const fileSistem = require('fs');
const textA = fileSistem.readFileSync(process.argv[2], 'utf-8');
const textB = fileSistem.readFileSync(process.argv[3], 'utf-8');
fileSistem.writeFileSync(process.argv[4], textA + textB, 'utf-8');
