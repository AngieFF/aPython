
def evaluate(math): #Evaluate operators
    if "+" in math:
        plus=math.split("+")
        return float(plus[0])+float(plus[1])
    
    elif "-" in math:
        minus=math.split("-")
        return float(minus[0])-float(minus[1])
    
    elif "*" in math:
        multi=math.split("*")
        return float(multi[1])*float(multi[2])
    
    elif "/" in math:
        div=math.split("/")
        return float(div[0])/float(div[1])
    
    else:
        print("Invalid operation")
        return ("Invalid Operation")


def main():
    math=input("Expression: ")
    math=math.strip() #Eliminates spaces
    
   

    
    result=evaluate(math)
    print(f"{result:.1f}") #Prints result with just 1 float
  

main()