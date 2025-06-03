temp = int(input("Enter temperture: "))

units = input("Enter Units(K or F or C): ")
if units == "K":
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{temp}K is {celsius:.2f}C and {fahrenheit:.2f}F")
elif units == "F":
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{temp}F is {celsius:.2f}C and {kelvin:.2f}K")
elif units == "C":
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print(f"{temp}C is {fahrenheit:.2f}F and {kelvin:.2f}K")
else:
    print("Invalid units. Please enter K, F, or C.")