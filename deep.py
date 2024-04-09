answer=input("What`s the Answer to the Great Question of Life, the Universe, and Everything? ")

#The simpliest way of coding this this a match case
match answer: 
    case "42"|"forty-two"|"forty two":
        print("Yes🙂")
    case _:
        print("No🙁")