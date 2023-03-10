#!/usr/bin/node

let userNum = Number(prompt("Enter number between 0 & 10: "));
let generatedNum = Math.floor(Math.random() * 11);

if (userNum < generatedNum) {
	console.log(`${userNum} is less than ${generatedNum}`);
}else if (userNum > generatedNum) {
	console.log(`${userNum} is greater than ${generatedNum}`);
}else {
	console.log(`${userNum} is equal to ${generatedNum}`);
}
