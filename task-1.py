def from_celsius(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k
def from_fahrenheit(f):
    c = (f - 32) * 5/9
    k = c + 273.15
    return c, k
def from_kelvin(k):
    c = k - 273.15
    f = (c * 9/5) + 32
    return c, f

print("Temperature Conversion Program")
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

if unit == 'C':
    f, k = from_celsius(temp)
    print(f"{temp}°C = {f:.2f}°F = {k:.2f}K")
elif unit == 'F':
    c, k = from_fahrenheit(temp)
    print(f"{temp}°F = {c:.2f}°C = {k:.2f}K")
elif unit == 'K':
    c, f = from_kelvin(temp)
    print(f"{temp}K = {c:.2f}°C = {f:.2f}°F")
else:
    print("Invalid unit entered. Please use C, F, or K.")
