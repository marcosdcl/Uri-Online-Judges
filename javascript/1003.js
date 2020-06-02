// Simple Sum

var input = require('fs').readFileSync('./dev/stdin/file.txt', 'utf8');
var lines = input.split('\n');

let a = parseInt(lines.shift());
let b = parseInt(lines.shift());

function simpleSum(a, b) {
  return a + b;
}

const sum = simpleSum(a, b);
console.log(`SOMA = ${sum}`);
