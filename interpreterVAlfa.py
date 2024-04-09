
def evaluate(x, operator, z): #Evaluate operators
    if operator=="+":
        return x+z
    elif operator=="-":
        return x-z
    elif operator=="*":
        return x*z
    elif operator=="/":
        return x/z
    else:
        return ("Invalid Operation")


def main():
    math=input("Expression: ")
    math=math.strip() #Eliminates spaces
    parts=math.split() #Splits the expression
   

    if len(parts)>=3:  #Make sure lenth of the input is 3 or more
        x=float(parts[0])
        y=parts[1]
        z=float(parts[2])
        
        result=evaluate(x,y,z)
        print(f"{result:.1f}") #Prints result with just 1 float
    else:
        print("Invalid format.")


main()





