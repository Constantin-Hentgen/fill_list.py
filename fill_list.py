liste = []
value = ""
print("Welcome to the 'fill the list' program")

while value != "stop":
    try:
        value = int(input('Enter a value : '))
        liste.append(value)
        print(liste)
    except:
        print("The value enter is not a number, enter stop if you want to quit")  
        value = input('Enter a value : ')
