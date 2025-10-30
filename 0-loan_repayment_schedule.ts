const loanRepaymentScheduleTS = (amount: number, intRate: number, numPay: number, instalment: number) => {
    let arr = new Array()

    let oldBal = amount
    let newBal = amount
    let mthly = instalment
    let owedInterest = 0
    let totalInterestPaid = 0
    intRate = (intRate/100) / 12
    let displayInt


    for (let i = 1; i <= numPay; i++) {
        // let loopNum = i
        owedInterest = newBal * intRate
        displayInt = `${owedInterest}`
        totalInterestPaid += owedInterest

        if(i<numPay) {
            mthly = instalment - Number(displayInt)
            oldBal = newBal
            newBal = oldBal - mthly
            
        } else {
            mthly = (instalment-Number(displayInt)) + owedInterest
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

console.log(loanRepaymentScheduleTS(2640000, 18.5, 48, 78242))