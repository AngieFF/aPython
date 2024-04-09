name=input('Hello user. What`s your name? ')
name=name.strip().capitalize()
print('Hello, ', name)
print('If you want to stop this game please type "finish"')
print('Lets go! ')

#Ask the user to type something
def AskF():
    ask=str(input('Tell me something: '))
    return ask.replace(' ', '...')
#Replace blank for ...

    
def main(): #replace what user type and ask to type something more if typed is not "finish"
    while True:
        ask=AskF() #I only need to call AskF() at the beginning of the loop 
        if ask.lower()=='finish': #Only converts finish to end the loop
        
            print('See you again! ')
            break
        print(ask)
        #AskF() here does nothing
       

main()