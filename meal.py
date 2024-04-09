def main():
    time=input("What time is it? ")
    Dtime=convert(time)

#Decide meal
    if 7.0<=Dtime<=8.0:
        print ("Breakfast time.")
    elif 12.0<=Dtime<=13.0:
        print("Lunch time.")
    elif 18.0<=Dtime<=19.0:
        print("Diner time.")
    else:
        print(" ")
    ...


def convert(time):
    #Divide hour into minutes and convert to float
    hour, minute = map(int, time.split(":"))
    Dminute=minute/60
    Dtime=hour+Dminute
    return(Dtime)

if __name__ == "__main__":
    main()
