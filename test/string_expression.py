def StringExpression(strParam):
    # __define-ocg__ The function reads a string containing written numbers and operators
    num_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    
    op_map = {
        "plus": "+", "minus": "-"
    }
    
    varOcg = ''  # String to store the final converted expression
    num_str = ''
    varFiltersCg = ''  # String to hold intermediate result, will help filter out operators

    i = 0
    while i < len(strParam):
        # Extract the number part
        for word in num_map:
            if strParam[i:i+len(word)] == word:
                varOcg += str(num_map[word])  # Add the number to varOcg
                i += len(word)
                break
        # Extract operator part
        for word in op_map:
            if strParam[i:i+len(word)] == word:
                varOcg += op_map[word]  # Add the operator to varOcg
                i += len(word)
                break

    # Now evaluate the mathematical expression
    try:
        result = eval(varOcg)
    except SyntaxError:
        return "Invalid expression"

    # Convert the result to its written-out form
    result_str = convert_number_to_words(result)

    # Return the final result in written form
    return result_str

def convert_number_to_words(num):
    # Function to convert a number to words
    num_map = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    
    if num == 0:
        return num_map[num]
    
    # If the number is negative
    if num < 0:
        num = abs(num)
        result_str = "negative"
    else:
        result_str = ""
    
    # Convert the number to words
    for digit in str(num):
        result_str += num_map[int(digit)]
    
    return result_str

# Test examples
print(StringExpression("onezeropluseight"))  # Output: oneeight
print(StringExpression("oneminusoneone"))   # Output: negativeonezero
