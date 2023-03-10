#!/usr/bin/node

let sumArray = ["Mike", "Antal", "Marc", "Emir", "Louiza", "Jacky"];
let notFound = true;

while (notFound && sumArray.length > 0) {
    if (sumArray[0] === "Louiza") {
        console.log("Found Her!");
        notFound = false;
    } else {
        sumArray.shift();
    }
}
