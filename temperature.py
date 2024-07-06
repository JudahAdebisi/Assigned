def convert_temperature():
    print("Temperature Conversion Program")
    print("-------------------------------")

    while True:
        temperature = input("Enter a temperature (e.g., 32C or 100F): ")
        if temperature.endswith("C") or temperature.endswith("c"):
            celsius = float(temperature[:-1])
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")
            break
        elif temperature.endswith("F") or temperature.endswith("f"):
            fahrenheit = float(temperature[:-1])
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")
            break
        else:
            print("Invalid input. Please enter a temperature with C or F.")

convert_temperature()
