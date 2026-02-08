class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}
        : Hi {user.username}, this is {self.username}!")

user1 = User("Alice", "alice@gmail.com", "password123")
user2 = User("Bob", " bob@gmail.com", "password456")

user1.say_hi_to_user(user2)
Output: Sending message to Bob: Hi Bob, this is Alice!

'''
here in the above code we have created a class User with a 
method **say_hi_to_user that takes another user object** as an 
argument and prints a greeting message to that user. 
We then create two user objects, user1 and user2, and call 
the say_hi_to_user method on user1, passing user2 as an 
argument. 
This results in a greeting message being printed to user2 
from user1.
'''

'''
lets look at how we can modify or update the data within an object.

'''


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}
        : Hi {user.username}, this is {self.username}!")

user1 = User("Alice", "alice@gmail.com", "password123")

#accessing the data fields of the user1 object
print(user1.username)  # Output: Alice
print(user1.email)  # Output: alice@gmail.com

# now we can assign new value to the email 
user1.email = "newemail@gmail.com"
print(user1.email)  # Output: newemail@gmail.com

'''
the problem with this approach is that we can directly modify 
the data fields of the object without any restrictions or validations.
to avoid this problem we can use getter and setter methods to 
access and modify the data fields of the class.

the get and set like read and modify the data.
'''