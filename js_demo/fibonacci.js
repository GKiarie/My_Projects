#!/usr/bin/node

let nr1 = 0;
let nr2 = 1
let temp;
let fibArray = [];

while (fibArray.length < 25) {
	fibArray.push(nr1);
	temp = nr1 + nr2;
	nr1 = nr2;
	nr2 = temp;
}

console.log(fibArray);
