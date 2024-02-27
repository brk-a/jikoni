const compound = (p: number, i: number, n: number): number => {
    return p * Math.pow(1 + (i/100), n)
}

const discount = (p: number, i: number, n: number): number => {
    return p * Math.pow(1 + (i/100), -n)
}

const compoundFactor = (i: number, n: number): number => {
    return Math.pow(1 + (i/100), n)
}

const discountFactor = (i: number, n: number): number => {
    return Math.pow(1 + (i/100), -n)
}

const d = (i: number) : number => {
    return i / (1+i)
}

const iMthly = (i: number, m: number): number => {
    const mthlyCompound = compoundFactor(i, 1/m)
    return m * (mthlyCompound - 1)
}

const dMthly = (i: number, m: number): number => {
    const iM = iMthly(i, m)
    return iM / (1+iM)
}

const forceOfInterest = (i: number): number => {
    return Math.log(1+i)
}

const annuityDuePV = (i: number, n: number): number => {
    const annImmPV = annuityImmediatePV(i, n-1)
    return 1 + annImmPV
}

const mthlyAnnuityDuePV = (i: number, m: number, n: number): number => {
    const mthlyAnnImmPV = mthlyAnnuityImmediatePV(i, m, n)
    const mthlyCompound = compoundFactor(i, 1/m)
    return mthlyCompound * mthlyAnnImmPV
}

const mthlyAnnuityDueFV = (i: number, m: number, n: number): number => {
    const mthlyAnnDuePV = mthlyAnnuityDuePV(i, m, n)
    const compound = compoundFactor(i, n)
    return compound * mthlyAnnDuePV
}

const annuityImmediatePV = (i: number, n: number): number => {
    const v = discountFactor(i, n)
    return (1-v) / i
}

const annuityImmediateFV = (i: number, n: number): number => {
    const cpdFactor = compoundFactor(i, n)
    return (cpdFactor - 1) / i
}

const mthlyAnnuityImmediateFV = (i: number, m: number, n: number): number => {
    const annImmFV = annuityImmediateFV(i, n)
    const iM = iMthly(i, m)
    return (i / iM) * annImmFV
}

const mthlyAnnuityImmediatePV = (i: number, m: number, n: number): number => {
    const annImmPV = annuityImmediatePV(i, n)
    const iM = iMthly(i, m)
    return (i / iM) * annImmPV
}

const perpetuityImmediatePV = (i: number) : number => {
    return 1 / i
}

const perpetuityDuePV = (i: number) : number => {
    const dd = d(i)
    return 1 / dd
}

const deferredAnnuityImmediatePV = (i: number, n: number, m: number) : number => {
    const annMPlusN = annuityImmediatePV(i, m+n)
    const annM = annuityImmediatePV(i, m)
    return annMPlusN - annM
}

const deferredAnnuityDuePV = (i: number, n: number, m: number) : number => {
    const vM = discountFactor(i, m)
    const annN = annuityDuePV(i, n)
    return vM * annN
}

const mthlyDeferredAnnuityImmediatePV = (i: number, m: number, n: number, q: number): number => {
    const mthlyAnnImmPV = mthlyAnnuityImmediatePV(i, m, n)
    const vQ = discountFactor(i, q)
    return vQ * mthlyAnnImmPV
}

const mthlyDeferredAnnuityDuePV = (i: number, m: number, n: number, q: number): number => {
    const mthlyAnnDuePV = mthlyAnnuityDuePV(i, m, n)
    const vQ = discountFactor(i, q)
    return vQ * mthlyAnnDuePV
}

const continuousAnnuityPV = (i: number, n: number): number => {
    const force = forceOfInterest(i)
    const annImmPV = annuityImmediatePV(i, n)
    return (i/force) * annImmPV
}

const deferredContinuousAnnuityPV = (i: number, n: number, q: number): number => {
    const contAnnQN = continuousAnnuityPV(i, q+n)
    const contAnnQ = continuousAnnuityPV(i, q)
    return contAnnQN - contAnnQ
}

const continuousAnnuityFV = (i: number, n: number): number => {
    const force = forceOfInterest(i)
    const annImmFV = annuityImmediateFV(i, n)
    return (i/force) * annImmFV
}
