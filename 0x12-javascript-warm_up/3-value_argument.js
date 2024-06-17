#!/usr/bin/node
const argsNum = process.argv[2];

if (argsNum === '') {
    console.log('No argument');
} else {
    console.log(argsNum);
}
