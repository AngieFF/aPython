print("Hello, lets start 🙂")
mass=int(input("Please type mass (must be in kg): "))
#Calculates the energy
energy= float(mass*pow(300000000,2))
#Print energy
print(energy, "J")

#Get the full number
print(f"{energy:.0f} J")