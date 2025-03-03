## Écrivez votre code ici !

def square(number):
    try:
        square = number*number
        return square
    except:
        print("Le paramètre doit être un nombre !")
        return None

print(square("e"))
