greet=input("Greeting: ").lower().strip()  

#Compares the first letter or word of the user`s answer
if greet.startswith("hello"): 
    print("0$")
elif greet.startswith("h"): 
    print("20$")
else:
    print("100$")