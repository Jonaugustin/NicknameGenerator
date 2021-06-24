
import random 

firstname = input("ENTER FIRSTNAME: ")
lastname = input("ENTER LASTNAME: ")
nicknames = ["King", "Ace", "Boss"]
menu = """ 
Main Menu ({} {})
1. Change Name
2. Display a Random Nickname
3. Display All Nicknames
4. Add a Nickname
5 Remove a nickname
6. Exit
"""


def changeName():
    global firstname
    global lastname
    firstname = input("ENTER FIRSTNAME: ")
    lastname = input("ENTER LASTNAME: ")
    print("Name changed to: ")
    print(firstname, lastname)
    callInput()

def randNickname():
    txt = "{} \"{}\" {}"
    print(txt.format(firstname, nicknames[random.randint(0,len(nicknames))], lastname))
    callInput()

def allNickname():
    txt = "{} \"{}\" {}"
    for x in nicknames:
        print(txt.format(firstname, x, lastname))
    callInput()
def addNickname():
    nicknames.append(input("ENTER NEW NICKNAME: "))
    txt = "New nickname \"{}\" was added."
    print(txt.format(nicknames[len(nicknames)-1]))
    callInput()

def removeNickname(): 
    removal = input("ENTER NICKNAME THAT SHOULD BE REMOVED: ")
    for x in nicknames:
        if removal == x:
            nicknames.remove(x)
    callInput()

def callInput():
    print(menu.format(firstname, lastname))
    option = int(input("Please choose an option from 1 to 6: "))        
    if option == 1:
        changeName()
    elif option == 2:
        randNickname()
    elif option == 3:
        allNickname()
    elif option == 4:
        addNickname()
    elif option == 5:
        removeNickname()
    elif option == 6:
        exit()
    else: 
        print("Please enter a number from 1 to 6 again.") 

callInput()

