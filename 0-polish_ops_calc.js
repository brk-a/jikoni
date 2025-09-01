// polish operations calculator
// 3 + 4 is + 3 4 etc

const calculate = (expr) => {
  const tokens = expr.trim().split(/\s+/);

  const helper = () => {
    if (tokens.length === 0) throw new Error('Invalid expression');
    const token = tokens.shift();

    if (['+', '-', '*', '/'].includes(token)) {
      const left = helper();
      const right = helper();
      switch (token) {
        case '+': return left + right;
        case '-': return left - right;
        case '*': return left * right;
        case '/': 
          if (right === 0) throw new Error('Division by zero');
          return left / right;
      }
    }

    const num = Number(token);
    if (isNaN(num)) throw new Error(`Invalid number: ${token}`);
    return num;
  };

  const result = helper();

  if (tokens.length > 0) throw new Error('Invalid expression: extra tokens remain');
  return result;
};

// Examples
// calculate('+ 3 4')     // 7
// calculate('- 3 * 4 5') // -17
// calculate('* + 3 4 5') // 35
// calculate('/ - 3 4 + 5 2') // -1
