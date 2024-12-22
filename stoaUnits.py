def main():
    first_run = True

    while True:
        if first_run:
            print("\nWelcome to stoaUnits :)")
            first_run = False

        print("\nChoose an option:")
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter")
        print("4. Quit")
        user_choice = input("Your choice: ")

        match user_choice:
            case "1":
                result = length()
                if result:
                    print(result)
            case "2":
                result = weight()
                if result:
                    print(result)
            case "3":
                result = temperature()
                if result:
                    print(result)
            case "4":
                print("\nGoodbye :)")
                break
            case _:
                print("Invalid choice. Please choose option 1, 2, 3 or 4")

def length():
    while True:
        print("\nChoose Length Conversion:")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Meters to Feet")
        print("4. Feet to Meters")
        print("5. Go Back")

        user_choice = input("Your choice: ")
        match user_choice:
            case "1":
                while True:
                    try:
                        kilometers = float(input("\nEnter Kilometers: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{kilometers} Kilometers is {str(round(kilometers * 0.621371, 2))} Miles"
            case "2":
                while True:
                    try:
                        miles = float(input("\nEnter Miles: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{miles} Miles is {str(round(miles / 0.621371, 2))} Kilometers"
            case "3":
                while True:
                    try:
                        meters = float(input("\nEnter Meters: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{meters} Meters is {str(round(meters * 3.28084, 2))} Feet"
            case "4":
                while True:
                    try:
                        feet = float(input("\nEnter Feet: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{feet} Feet is {str(round(feet / 3.28084, 2))} Meters"
            case "5":
                return
            case _:
                print("Invalid choice. Please choose option 1, 2, 3, 4 or 5")

def weight():
    print("\nChoose Weight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Ounces")
    print("4. Ounces to Grams")
    print("5. Go Back")

    while True:
        user_choice = input("Your choice: ")
        match user_choice:
            case "1":
                while True:
                    try:
                        kg = float(input("\nEnter Kilograms: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{kg} Kilograms is {round(kg * 2.20462, 2)} Pounds"
            case "2":
                while True:
                    try:
                        pounds = float(input("\nEnter Pounds: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{pounds} Pounds is {round(pounds / 2.20462, 2)} Kilograms"
            case "3":
                while True:
                    try:
                       grams = float(input("\nEnter Grams: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{grams} Grams is {round(grams * 0.035274, 2)} Ounces"
            case "4":
                while True:
                    try:
                        ounces = float(input("\nEnter Ounces: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{ounces} Ounces is {round(ounces / 0.035274, 2)} Ounces"
            case "5":
                return
            case _:
                print("Invalid choice. Please choose option 1, 2, 3, 4 or 5")

def temperature():
    while True:
        print("\nChoose Temperature Conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Go Back")

        user_choice = input("Your choice: ")
        match user_choice:
            case "1":
                while True:
                    try:
                        celsius = float(input("\nEnter Celsius: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{celsius}°C is {round((celsius * 9/5) + 32, 2)}°F"
            case "2":
                while True:
                    try:
                        celsius = float(input("\nEnter Celsius: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{celsius}°C is {round(celsius + 273.15, 2)}K"
            case "3":
                while True:
                    try:
                        fahrenheit = float(input("\nEnter Fahrenheit: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{fahrenheit}°F is {round((fahrenheit - 32) * 5/9, 2)}°C"
            case "4":
                while True:
                    try:
                        fahrenheit = float(input("\nEnter Fahrenheit: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{fahrenheit}°F is {round(((fahrenheit - 32) * 5/9) + 273.15, 2)}K"
            case "5":
                while True:
                    try:
                        kelvin = float(input("\nEnter Kelvin: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{kelvin}K is {round(kelvin - 273.15, 2)}°C"
            case "6":
                while True:
                    try:
                        kelvin = float(input("\nEnter Kelvin: "))
                    except ValueError:
                        print("Invalid input, please type a number")
                    else:
                        return f"{kelvin}K is {round(((kelvin - 273.15) * 9/5) + 32, 2)}°F"
            case "7":
                return
            case _:
                print("Invalid choice. Please choose option 1, 2, 3, 4, 5, 6, or 7")


main()