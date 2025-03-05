package loan_repayment

type repayment struct {
	ob float64;
	i float64;
	p float64;
	cb float64;
}

func loanReapaymentSchedule (float64 a, float64 instalment, float64 r) {
	arr := []repayment{}

	go func(){
		for{
			interest := (r/100) * a
			principal := instalment - interest
			closing_bal := a - principal

			arr.append(arr, {
				ob: a,
				i: interest,
				p: principal,
				cb: closing_bal
			})

			a = closing_bal

			if(a<0){
				break
			}
		}
	}()
}