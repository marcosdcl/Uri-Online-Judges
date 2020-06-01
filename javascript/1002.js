// Area of a Circle

var input = require('fs').readFileSync('./dev/stdin/file.txt', 'utf8');
var lines = input.split('\n');

const π = 3.14159;
let r = parseFloat(lines.shift());

function areaCircle(r) {
  area = π * (r * r);
  return area;
}

let a = areaCircle(r).toFixed(4);
console.log(`A=${a}`);
