'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}


function getSecondLargest(nums) {
    // Complete the function
    var sArray = nums.sort(function (a,b){
        return a - b;
    });
    var uSarray = sArray.filter(function (elm, index, self){
        return index == self.indexOf(elm);
    });
    return uSarray[uSarray.length - 2];
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);

    console.log(getSecondLargest(nums));
}
