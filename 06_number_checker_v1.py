# Code to check that the number is valid...


def temp_check(low):
    valid = False
    while not valid:

        try:
            response = float(input("Enter a number: "))

            if response < low:
                print("Too cold!!")
            else:
                return response

        except ValueError:
            print("Please enter a number")