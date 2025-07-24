from unicodedata import digit

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")


try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
else:
    C_F = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if C_F == "C":
        convert_to_fahrenheit(temperature)
    elif C_F == "F":
        convert_to_celsius(temperature)
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")