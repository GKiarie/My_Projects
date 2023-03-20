#!/usr/bin/node

let maxValue = 5;
let minValue = 0;
let playerGuess;
let randValue = Math.floor(Math.random()*(maxValue + 1));
let guesedRight = false;

while (guesedRight == false) {
    playerGuess = Number(prompt(`Please enter a value btn ${minValue} and ${maxValue}: `));
    if (playerGuess > randValue) {
        console.log("High");
    } else if (playerGuess < randValue) {
        console.log("low");
    } else {
        console.log("Congats, you guessed correct");
        guesedRight = true;
    }
}
