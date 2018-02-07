# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

bio = {}

bio["name"] = "Jack"
bio["age"] = "32"
bio["birth country"] = "The United States"
bio["favorite language"] = "Python"

print bio

def Biographical():
    print "My name is {}".format(bio["name"])
    print "My age is {}".format(bio["age"])
    print "My country of birth is {}".format(bio["birth country"])
    print "My favorite language is {}".format(bio["favorite language"])

Biographical()
