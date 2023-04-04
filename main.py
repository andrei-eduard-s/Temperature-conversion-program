print("The temperature units will be described as:")
print("C = Celsius")
print("F = Fahrenheit")
print("K = Kelvin")
temp = float(input("Enter the temperature: "))
unit = input("What unit of measure does this temperature have? (C/F/K): ")
desired_unit = input("What unit of measure do you want to convert in? (C/F/K):")

if unit == "C":
    if desired_unit == "F":
        temp = round((9 * temp) / 5 + 32, 3)
        print(f"The temperature in Fahrenheit is: {temp}°F")
    elif desired_unit == "K":
        temp = round (temp + 273.15, 3)
        print(f"The temperature in Kelvin is: {temp} K")
elif unit == "F":
    if desired_unit == "C":
        temp = round ((temp - 32) * 0.5556, 3)
        print(f"The temperature in Celsius is: {temp}°C")
    elif desired_unit == "K":
        temp = round ((temp - 32) * 0.5556 + 273.15, 3)
        print(f"The temperature in Kelvin is: {temp} K")
elif unit == "K":
    if desired_unit == "C":
        temp = round (temp - 273.15, 3)
        print(f"The temperature in Celsius is: {temp}°C")
    elif desired_unit == "F":
        temp = round (temp * 1.8 - 459.67, 3)
        print(f"The temperature in Fahrenheit is: {temp}°F")
else:
    print(f"{unit} is an invalid unit of measurement")