def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #Delete $, and return a float with 2 decimals
    return float(d.strip("$"))
    


def percent_to_float(p):
    #Delete % and convert it into a float
    return float(p.strip("%"))/100


main()