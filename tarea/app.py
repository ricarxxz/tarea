def convertir_celsius(celsius):
    
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9/5) + 32
    
    return {
        'kelvin': kelvin,
        'fahrenheit': fahrenheit
    }



celsius = float(input("Ingrese la temperatura en Celsius: "))

resultado = convertir_celsius(celsius)
print(f"Kelvin: {resultado['kelvin']}K  Fahrenheit: {resultado['fahrenheit']}°F")
