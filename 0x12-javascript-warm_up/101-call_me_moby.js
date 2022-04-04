#!/usr/bin/node

exports.callMeMoby = function (x, fFunction) {
  while (x-- > 0) {
    fFunction();
  }
};
