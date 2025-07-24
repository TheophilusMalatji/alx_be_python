FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

temperature = float(input("Enter the temperature to convert:"))
C_F = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()

if C_F == "C":
    convert_to_fahrenheit(temperature)
elif C_F == "F":
    convert_to_celsius(temperature)
