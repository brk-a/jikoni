// const loanRepaymentScheduleJS = (a, instalment, r) => {
//     let arr = new Array()

//     do {
//         let interest = (r/100) * a
//         let principal = instalment - interest 
//         let cb = a - principal

//         arr.push({
//             ob: a,
//             interest,
//             principal,
//             cb,
//         })

//         a = cb
//     } while (a>0)

//     return arr
// }

const loanRepaymentScheduleJS = (amount, intRate, numPay, instalment) => {
    let oldBal = amount
    let newBal = amount
    let mthly = instalment
    let owedInterest = 0
    let totalInterestPaid = 0
    intRate = (intRate/100) / 12
    let displayInt
    let arr = []

    for (let i = 1; i <= numPay; i++) {
        let loopNum = i
        owedInterest = newBal * intRate
        displayInt = `${owedInterest}`
        totalInterestPaid += owedInterest

        if(i<numPay) {
            mthly = instalment - displayInt
            oldBal = newBal
            newBal = oldBal - mthly
            
        } else {
            mthly = (instalment-displayInt) + owedInterest
            oldBal = newBal
            newBal = 0
            mthly = mthly
        }

        arr.push({
            ob: oldBal,
            interest: owedInterest,
            principal: oldBal - owedInterest,
            cb: newBal,
        })
    }

    return arr
}

console.log(loanRepaymentScheduleJS(2640000, 18.5, 48, 78242))