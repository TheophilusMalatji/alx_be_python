def safe_divide(numerator,denominator):
    num = float(numerator)
    den = float(denominator)
    try:
       result = num / den
       return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")