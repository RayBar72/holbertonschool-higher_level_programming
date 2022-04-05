#!/usr/bin/node

exports.esrever = function (list) {
  const nuevo = [];
  let largo = list.length;
  while (largo--) {
    nuevo.push(list[largo]);
  }
  return nuevo;
};
