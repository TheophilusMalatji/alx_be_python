def safe_divide(numerator,denominator):
    if denominator == "0":
                print("Error: Cannot divide by zero.")
    num = float(numerator)
    den = float(denominator)
    try:
       result = num / den
       return(f'The result of the division is {result}')
    

    except ValueError:
        return("Error: Please enter numeric values only.")
    