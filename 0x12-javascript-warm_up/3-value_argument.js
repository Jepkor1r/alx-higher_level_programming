#!/usr/bin/node
const argsNum = process.argv[2];

if (argsNum === undefined) {
    console.log('No argument');
} else {
    console.log(argsNum);
}
