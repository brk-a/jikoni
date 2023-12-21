/**
there is an array of N elememnts, all ints
write a fuction, solution(A), that returns the smallest positive
int, greater than zero, that is not in the array 
*/

function sortArray(A){
    A.filter(i => i > 0).sort((a, b) => a-b)
    return A
}


function solution(A) {
    // Implement your solution here
    sortedA = sortArray(A)
    let sp = 1
    for(i of sortedA){
        if(sp < i){
            return sp
        }
        sp = sortedA[i] + 1
    }
    return sp
    
}

const a = [1, 3, 6, 4, 1, 2]
const b = solution(a)
console.log(b)