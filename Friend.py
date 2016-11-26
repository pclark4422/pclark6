# Friend class

class Friend:

    def __init__(self, name):
        self.name = name
        self.friends = []

    ### Return the name of the FaceBook user
    def name(self):
        return self.name


    ### Return the list of friends of this FaceBook user
    def friends(self):
        return self.friends


    ### Determines whether or not the FaceBook user self's name comes before
    ### the Facebook user other's name in the dictionary
    def __lt__(self, other):
        pass

 
    ### Determines whether or not the FaceBook user self's name is the same
    ### as the Facebook user other's name
    def __eq__(self, other):
        pass


    ### Return a list of names in alphabetical order of FaceBook user self's friends
    def getFriends(self):
        pass

      

    ### Add FaceBook user person to the list of self's friends
    def addFriend(self, person):
        self.friends.append(person)
        pass


    ### Remove FaceBook user person from self's list of friends
    def removeFriend(self, person):
        self.friends.remove(person)
        pass






