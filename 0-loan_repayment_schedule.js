const loanRepaymentScheduleJS = (a, instalment, r, m) => {
    let arr = new Array()

    do {
        let interest = (r/100)/m * a
        let principal = instalment - interest 
        let cb = a - principal

        arr.push({
            ob: a,
            interest,
            principal,
            cb,
        })

        a = cb
    } while (a>0)

    return arr
}

// const loanRepaymentScheduleJS = (amount, intRate, numPay, instalment) => {
//     let oldBal = amount
//     let newBal = amount
//     let mthly = instalment
//     let owedInterest = 0
//     let totalInterestPaid = 0
//     intRate = (intRate/100) / 12
//     let displayInt
//     let arr = []

//     for (let i = 1; i <= numPay; i++) {
//         // let loopNum = i
//         owedInterest = newBal * intRate
//         displayInt = `${owedInterest}`
//         totalInterestPaid += owedInterest

//         if(i<numPay) {
//             mthly = instalment - displayInt
//             oldBal = newBal
//             newBal = oldBal - mthly
            
//         } else {
//             mthly = (instalment-Number(displayInt)) + owedInterest
//             oldBal = newBal
//             newBal = 0
//             mthly = mthly
//         }

//         arr.push({
//             // ob: oldBal,
//             interest: owedInterest,
//             principal: oldBal - owedInterest,
//             cb: newBal,
//         })
//     }

//     return arr
// }

const discountFactor = (i, n) => {
    return Math.pow(1 + (i/100), -n)
}

const compoundFactor = (i, n) => {
    return Math.pow(1 + (i/100), n)
}

const mthlyAnnuityImmediatePV = (i, m, n) => {
    const annImmPV = annuityImmediatePV(i, n)
    const iM = iMthly(i, m)
    return (i / iM) * annImmPV
}

const iMthly = (i, m) => {
    const mthlyCompound = compoundFactor(i, 1/m)
    return m * (mthlyCompound - 1)
}

const annuityImmediatePV = (i, n) => {
    const v = discountFactor(i, n)
    return (1-v) / i
}

// const loanRepaymentScheduleJS = (amount, intRate, numPay) => {
    // let arr = []
    // let oldBalance = amount
    // let newBalance= amount
    // const instalment = (amount / mthlyAnnuityImmediatePV(intRate, 12, 4)) / 12
    // for (let i=0; i<numPay; i++) {
    //     interest = (1 - discountFactor(intRate, numPay-i)) * instalment
    //     if(i<numPay) {
    //         principal = instalment - interest
    //         oldBalance = newBalance
    //         newBalance = oldBalance - principal
    //     } else {
    //         break
    //     }

    //     arr.push({
    //         interest,
    //         principal,
    //         newBalance,
    //     })
    // }

//     let i=0
//     do  {
//         interest =  (intRate/100) / 12 * oldBalance//(1 - discountFactor(intRate, numPay-i)) * instalment
//         // if(i<numPay) {
//             principal =  instalment - interest //discountFactor(intRate, numPay-i) * instalment
//             oldBalance = newBalance
//             newBalance = oldBalance - principal
//         // } else {
//             // break
//         // }

//         arr.push({
//             oldBalance,
//             interest,
//             principal,
//             newBalance,
//         })
//         i++
//     } while (oldBalance>0 && newBalance>0)
//     return arr
// }

console.log(loanRepaymentScheduleJS(2640000, 78242,  18.5, 12))
console.log("=========================================================================")
console.log(loanRepaymentScheduleJS(100, 1.88,  5, 12))
console.log("=========================================================================")
console.log(loanRepaymentScheduleJS(2640000, 76306.99,  18.5, 12))