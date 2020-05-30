// Extremely Basic

var input = require('fs').readFileSync('./dev/stdin/file.txt', 'utf8');
var lines = input.split('\n');

var a = parseInt(lines.shift());
var b = parseInt(lines.shift());

function sum(a, b) {
  let x = a + b;
  return x;
}

console.log( 'X = ' + ( sum(a, b) ) );
