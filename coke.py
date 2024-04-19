valid_coins=[25,10, 5]   #list of aceppted coins
coin_sum=0 

while coin_sum<50:   
    prize=int(input("Insert coin: "))
    if prize in valid_coins:
        coin_sum+=prize
    else:
        print("Invalid coin. Please insert 25, 10, 5. ")

    #Tells the user how much he ows
    amount=50-coin_sum
    if amount>0:
        print("Amount Due: ", amount)
     

#calculates change
if coin_sum>50:
    change=coin_sum-50
    print("Change: ", change)
else:
    print("Change: 0")
 

