"""This program converts a decimal value into binary"""

def binary(decimal):
    binary = ""
    reminder = 0
    # Verfiy as a intger
    # Convert from decimal to binary

    try:
        while decimal > 0:#   Until decimal is => 0
            reminder = decimal % 2
            #  Modulo the number and record answer
            binary = str(reminder) + binary
            #  Divide number by 2
            decimal = decimal // 2
        # Return binary format to user
        # Check for input == 0

        print(f"Binary: {binary}")

    except ValueError:
        print("Invalid Input")


def hexadecimal(decimal_input):
    """This program converts decimal to hexadecimal"""

    hex_output = ""
    remainder = 0

    hex_alpha = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    try:
        while decimal_input > 0:
            remainder = decimal_input % 16

            if str(remainder) in hex_output:
                hex_output = hex_output[remainder] + hex_output
            else:
                hex_output = str(remainder) + hex_output

            decimal_input = decimal_input // 16

        print(f"Hexadecimal: {hex_output}")

    except ValueError:
        print("Invalid Input")



def octal(decimal_input):
    """This program converts decimal to ocatal"""

    # Get input from user
    octal = ""
    remainder = 0
        # Validate input with try...exception: ValueError 
    try:
        while decimal_input > 0:
            remainder = decimal_input % 8 
            octal = str(remainder) + octal
            decimal_input = decimal_input // 8

        print(f"Octal:{octal}")
    except ValueError:
        print("Invalid input")
    # Convert to ocatl 

    # Print result
