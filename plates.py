import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): #This function will return true if valid and false if not 
    if re.fullmatch(r'([A-Za-z]{3,7}|[A-Za-z]{2,}[1-9][0-9]*)', s) and 3 <= len(s) <= 7:
        return True
    return False
        


main()