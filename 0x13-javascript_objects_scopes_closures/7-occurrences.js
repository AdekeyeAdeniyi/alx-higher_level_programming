#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((counter, value) => value === searchElement ? counter + 1 : counter, 0);
};
