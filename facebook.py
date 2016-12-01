## Philip Clark
## Created 25Nov2016

from Friend import *
from errors import *
import sys

def addUser(selection, users):
    print("addUser")
    try:
        ##Checks the number of arguments in selection
        if (len(selection) != 2):
            raise Args
        
        ##Checks to make sure the name argument isnt blank
        if(selection[1] == ''):
            raise ValueError
        
        person = Friend(selection[1])
              
        
        ##Checks if the name given is already in the list of users
        if selection[1] in users.keys():
            raise LookupError
        
        person = Friend(selection[1])
        users.update({person.name : person})
        print(person.name + " has been entered")
        
    except ValueError:                   
        print("ERROR: The P command requires exactly 1 name input.  Type 'M' to see menu options")
        pass
        
    except LookupError:
        print("ERROR: " + selection[1] + " is already a user")
        pass
    
    except Args:
        print("ERROR: The P command requires exactly 1 name input.  Type 'M' to see menu options")
        pass
        
##lists the user's friends
def listFriends(selection, users):
    print("listFirends")
    try:
        
        ##Checks to make sure there are only 2 arguements passed
        if (len(selection) != 2):
            raise Args
            
        person = Friend(selection[1])
        
        ##Checks if the name argument is blank
        if (selection[1] == ""):
            raise ValueError

        ##Checks if the user exists
        if selection[1] in users.keys():
            person = users[selection[1]]
        else:
            raise KeyError
            
        ##Checks if the user has any friends
        if (len(person.friends) == 0):
            raise IndexError
            
        print("Friends of " + person.name + " are")
        for buddy in person.getFriends():
            print(buddy.name)
   
    except ValueError:
        print("ERROR: The L command requires exactly 1 name input.  Type 'M' to see menu options")

    except Args:
        print("ERROR: The L command requires exactly 1 name input.  Type 'M' to see menu options")
                
    except KeyError:
        print("ERROR: " + person.name + " not in facebook")
                        
    except IndexError:
        print(selection[1] + " has no friends") 

##Displays the main menu of the program
def menu(): 
    print("WELCOME TO FACEBOOK")
    print("\n")
    print("To display this screen, type M for menu")
    print("\n")
    print("P *name* - Create a new person. NOTE: Only a single instance of each name is allowed")        
    print("F *name1* *name2* - Record that the two people are friends")
    print("U *name1* *name2* - Record that the two people are no longer friends")
    print("L *name* - Prints all of the frineds of the specified person")
    print("Q *name1 *name2* - Check if the two people are friends")
    print("X - Exit the program")
    
    pass

def makeFriends(selection, users, friends):
    print("makeFriends")
    try:
        ##Cehcks to make sure the correct number of arguments are given
        if (len(selection) != 3):
            raise Args
        
        ##Checks if any name arguments are blank
        if (selection[1] == "" or selection[2] ==""):
            raise ValueError
        
        ##Checks if trying to friend self
        if (selection[1] == selection[2]):
            raise Self
        
        ##Checks to make sure both names are in registered users
        if (selection[1] not in users.keys()):
            print(selection[1] + " is not in users")
            raise LookupError
        if (selection[2] not in users.keys()):
            print(selection[2] + " is not in users")
            raise LookupError
        
        ##Checks to make sure the two users aren't already friends
        if(areFriends(selection, users, friends) == True):
            raise Friends
        
        person1 = users[selection[1]]
        person2 = users[selection[2]]
        
        dictString = ""
        if(person1 < person2):
            dictString = person1.name + "*" + person2.name
        else:
            dictString = person2.name + "*" + person1.name
        friends.update({dictString : True})
        
        person1.addFriend(person2)
        person2.addFriend(person1)
        
        print(person1.name + " and " + person2.name + " are now friends")

        
    except Args:
        print("ERROR: The F command requires exactly 2 name inputs.  Type 'M' to see menu options")

    
    except ValueError:
        print("ERROR: The F command requires exactly 2 name inputs.  Type 'M' to see menu options")

    
    except LookupError:
        return
    
    except Friends:
        print("ERROR: " + selection[1] + " and " + selection[2] + " are already friends")
        
    except Self:
        print("ERROR: You cannot friend yourself")
    
    pass

def unfriend(selection, users, friends):
    print("unfriend")
    try:
        ##Cehcks to make sure the correct number of arguments are given
        if (len(selection) != 3):
            raise Args
        
        ##Checks if any name arguments are blank
        if (selection[1] == "" or selection[2] ==""):
            raise ValueError
        
        ##Checks if trying to unfriend self
        if(selection[1] == selection[2]):
            raise Self

        ##Checks to make sure both names are in registered users
        if (selection[1] not in users.keys()):
            print(selection[1] + " is not in users")
            raise LookupError
        if (selection[2] not in users.keys()):
            print(selection[2] + " is not in users")
            raise LookupError
        
        ##Checks to make sure the two users are friends
        if(areFriends(selection, users, friends) == False):
            raise Friends
        
        person1 = users[selection[1]]
        person2 = users[selection[2]]
        
        person1.removeFriend(person2)
        person2.removeFriend(person1)

        dictString = ""
        if(person1 < person2):
            dictString = person1.name + "*" + person2.name
        else:
            dictString = person2.name + "*" + person1.name
			
        friends.pop(dictString, True)
        
        print(person1.name + " and " + person2.name + " are no longer friends")
        
    except Args:
        print("ERROR: The f command requires exactly 2 name inputs.  Type 'M' to see menu options")
 
    except ValueError:
        print("ERROR: The L command requires exactly 2 name inputs.  Type 'M' to see menu options")
    
    except LookupError:
        return
    
    except Friends:
        print("ERROR: " + selection[1] + " and " + selection[2] + " are not friends")
    
    except Self:
        print("ERROR: You cannot unfriend yourself")
    
    pass

##Checks to see if the two users are friends
def areFriends(selection, users, friends):
    print("areFriends")
    errorString = "blah"
    print(selection)
    print(users.keys())
    print(friends.keys())
    try:
    ##Checks to make sure both names are in registered users
        print(selection[1] + " " + selection[2])
        if (selection[1] not in users.keys()):
            errorString = selection[1] + " is not a user"
            raise LookupError
        elif(selection[2] not in users.keys()):
            errorString = selection[2] + " is not a user" 
            raise LookupError		
        person1 = users[selection[1]]
        person2 = users[selection[2]]
            
        dictString = "blag"
        print("berofer compare")
        if(person1 < person2):
            dictString = person1.name + "*" + person2.name
        else:
            dictString = person2.name + "*" + person1.name
        
        print(dictString)
        print(dictString in friends.keys())
        return(dictString in friends.keys())
        ##if(dictString in friends.keys()):
          ##  print("in true")
            ##return True
        ##else:
          ##  print("in else")
            ##return False
    
    except LookupError:
        print("in lookup error")
        return errorString
		
    return False

## main body of the program
def main():
    selection = [" "]
    menuitems = "pPfFuUlLqQxXmMcC"
    users = {}  
    friends = {}
    
    menu()
    print("\n")    
        
    while(selection[0] != "x" and selection[0] !="X"):
        selection = raw_input().split(" ")
        try:
            ##Checks if the number of arguments is in range
            if (selection[0] == "" or len(selection) > 3):
                raise Args

            ##Checks if the first arguement is in the list of available functions
            if (selection[0] not in (menuitems)):
                raise ValueError
        
            ## Case switch statement
            ##Prints the menu
            if(selection [0] in "mM"):
                menu()
                
            ##Creates a new Friend object
            elif(selection[0] in "pP"):
                addUser(selection, users)
                
            
            ##Displays the given persons list of friends
            elif(selection[0] in "lL"):
                listFriends(selection, users) 
                    
            ##Makes the two people friends
            elif(selection[0] in "fF"):
                makeFriends(selection, users, friends)
                
            ##Makes two people no longer friends
            elif(selection[0] in "uU"):
                unfriend(selection, users, friends)
            
            ##Checks if two people are friends
            elif(selection[0] in "qQ"):
                print(areFriends(selection, users, friends))
                print("areFriends selected")
            
            elif(selection[0] in "cC"):
                print(users)
                                     
        
        except ValueError:
            print("ERROR " + selection[0] + " is not a valid input.  Press 'M' to see menu options")
        
        except Args:
            print("ERROR: Arguments out of range. Press 'M' to see menu options") 
        
        print("\n")
    
    print("Exiting facebook")
    pass

main()
        