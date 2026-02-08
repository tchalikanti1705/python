# There are 2 different ways to create getters and setters in Python. 
# 1. The tradiotional way: make the data fields private and create getter and setter methods to access and modify the data fields.


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # we are making the email data field private by adding an underscore before the name of the data field.
        self.password = password
    
    # getter method for email
    def get_email(self):
        return self._email

    # setter method for email
    def set_email(self, new_email):
        # we can add some validation here to check if the new email is valid or not before updating the email data field.
        if "@" in new_email:
            self._email = new_email
        else:
            print("Invalid email address")
    