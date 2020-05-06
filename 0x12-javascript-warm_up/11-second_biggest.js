#!/usr/bin/node
// script that searches the second biggest integer in the list of argument
const args = process.argv.slice(2);
if (!args[0]) {
  console.log('0');
} else if (args.length === 1) {
  console.log('0');
} else {
  console.log(args.sort().reverse()[1]);
}
