#!/usr/bin/node

const arg = process.argv;
const num = parseInt(arg[2], 10);

if (arg[2]) {
  if (num) {
    for (let i = 0; i < num; i++) {
      let square = '';
      for (let j = 0; j < num; j++) {
        square += 'X';
      }
      console.log(square);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
