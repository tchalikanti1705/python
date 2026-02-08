'''
static attributes 

A static attribute (sometimes called a class attribute) is an 
attribute that belongs to the class itself rather than to 
any specific instance of the class.

The static attributes are shared among all the instaces of the 
class, which means that if we change the value of a static 
attribute, it will affect all the instances of the class that 
are using that static attribute.

static attributes are defined within the class but outside 
of any method, and they are accessed using the class name 
rather than an instance of the class.


'''

class Users:
    #static attribute
    users_counts = 0 #this is a static attribute that will keep track of the number of users created.

    def __init__(self):
        # the static attribues are accessed using the class name rather than an instance of the class.
        Users.users_counts += 1 #every time a new user is created, we will increment the users_counts static attribute by 1 to keep track of the number of users created.

user1 = Users()
print(Users.users_counts) # Output: 1   
user2 = Users()
print(Users.users_counts) # Output: 2           
user3 = Users()
print(Users.users_counts) # Output: 3
user4 = Users()
print(Users.users_counts) # Output: 4

'''
when to use static and when to use instance attributes?
we use static attributes when we want to store data that is shared among all the instances of the class, such as a count of the number of instances created, or a common configuration setting that applies to all instances.
we use instance attributes when we want to store data that is specific to each instance of the class, such as the name or age of a user, or the color and model of a car.
'''