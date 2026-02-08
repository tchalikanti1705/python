# Accessing and Modifying Data:
# 2. The Pythonic way: use the @property decorator to create getter and setter methods. 
# This way we can access and modify the data fields like regular attributes without having to call the getter and setter methods explicitly.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.password = password

    @property
    def email(self):
        return self._email #one question that might arise is why we are using _email instead of email in the getter method.
        # the reason is that we are using the @property decorator to create a getter method for the email data field, and we want to avoid a naming conflict between the getter method and the data field.
        # by convention, we use an underscore before the name of the data field to indicate that it is a private data field that should not be accessed directly from outside the class.
        #and also email is the name of the getter method that we are creating using the @property decorator, so we cannot use the same name for the data field.
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Invalid email address")


'''
to summarize, in the above code we have created a class User 
with a private email data field and used the @property decorator to 
create getter and setter methods for the email data field.
This allows us to access and modify the email data field 
like a regular attribute while still having control over 
the data through the getter and setter methods.
'''