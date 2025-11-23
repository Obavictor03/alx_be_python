FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp_value = int(input(("Enter the temperature to convert: ")))
if not temp_value.replace('.', '', 1).lstrip('-').isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    result = convert_to_fahrenheit(temp_value)
    print(f"{temp_value}°C is equal to {result:.2f}°F")
elif unit == "F":
    result = convert_to_celsius(temp_value)
    print(f"{temp_value}°F is equal to {result:.2f}°C")
else:
    print("Invalid unit")