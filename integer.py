#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This program tells you if a number is positive, negative, or equal to 0


def main():
    # This function tells you if a number is positive, negative, or equal to 0

    # Input
    integer = int(input("Enter a number (integer): "))
    print("")

    # process
    if integer > 0:
        # Output 1
        print("Your integer is positive")
    elif integer < 0:
        # Output 2
        print("Your integer is negative")
    elif integer == 0:
        # Output 3
        print("Your integer is 0")
    else:
        # Output 4
        print("Error, unable to identify integer")


if __name__ == "__main__":
    main()
