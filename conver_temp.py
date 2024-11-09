# Convert temperature to Celsius, Fahrenheit, and Kelvin.

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1-6): "))
temperature = float(input("Enter the temperature to convert: "))

def temp_convert(temperature,choice):
    if choice == 1:
        print("Celsius to Fahrenheit",(temperature * 9/5) + 32)
    elif choice == 2:
        print("Celsius to Kelvin",(temperature + 273.15))
    elif choice == 3:
        print("Fahrenheit to Celsius",(temperature - 32) * 5/9)
    elif choice == 4:
        print(" Fahrenheit to Kelvin",(temperature - 32) * 5/9 + 273.15)
    elif choice == 5:
        print("Kelvin to Celsius",(temperature - 273.15))
    elif choice == 6:
        print("Kelvin to Fahrenheit",(temperature - 273.15) * 9/5 + 32)
    else:
        print("Invalid choice. Please select a valid option.")

temp_convert(temperature,choice)
