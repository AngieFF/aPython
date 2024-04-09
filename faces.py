print("Hello 🙂")

def convert():
    face=str(input("How are you today? "))
    return face

def main():
    face=convert()
    #Create a dictionary so each emoji has it`s own value. this is an item.
    emoji={
        ":)":"🙂",
        ":(":"🙁"
    }
    #when for loop starts, python asings :) to texFace and the emoji to emojiFace.
    #Then, for loop search in the dictionary ultil it finds a suitable value.
    for texFace, emojiFace in emoji.items():
        face=face.replace(texFace, emojiFace) #Replace :) for the emoji
    
    print(face)

main()