import random


def main():
    input_file = open("temps_input.txt", "r")
    output_file = open("temps_input.txt", "w")
    for line in input_file:
        result = converting_fahrenheit_to_celsius(float(line))
        # result = converting_celsius_to_fahrenheit(float(line))
        print(result, output_file)
    input_file.close()
    output_file.close()


def create_input_file(quantity):
    temperatures_file = open("temps_input.txt", "w")
    for i in range(quantity):
        temperature = random.uniform(-200, 200)
        print(temperature, file=temperatures_file)
    temperatures_file.close()


def converting_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def converting_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
