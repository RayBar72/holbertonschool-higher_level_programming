#!/usr/bin/node

const impDic = require('./101-data').dict;
const nDic = {};
for (const i in impDic) {
  if (impDic[i] in nDic) {
    nDic[impDic[i]].push(i);
  } else {
    nDic[impDic[i]] = [i];
  }
}
console.log(nDic);
