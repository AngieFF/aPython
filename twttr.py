vowels=["a","e","i","o","u","A","E","I","O","U"] #List of vowels
result=""

text=str(input("Writte something to the World: "))

for char in text:
    if char not in vowels:
        result+=char

print(result)

