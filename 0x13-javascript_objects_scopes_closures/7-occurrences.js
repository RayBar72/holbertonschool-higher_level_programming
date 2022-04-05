#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const largo = list.length;
  let j = 0;
  for (let i = 0; i < largo; i++) {
    if (list[i] === searchElement) {
      j++;
    }
  }
  return j;
};
