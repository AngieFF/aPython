import re #Works with regular expressions: sequence of characters that defines a search pattern
def main():
    name=input("Variable name: ")
    new_name=sep_name(name)
    print(new_name)
    
     

def sep_name(variable):
    parts=re.split(r'(?<=[a-z])(?=[A-Z])',variable)
    result=[part[0].lower() + part[1:] for part in parts]
    final_result="_".join(result)
    return final_result

#?<=[a-z]):positive lookbehind, makes sure that the letter just behind is lowercase
#(?=[A-Z]): positive lookahead, makes sure that the letter ahead is a capital letter

main() 




