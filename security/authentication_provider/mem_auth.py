
# **********************
# in mem auth provider
# **********************

class User():
    name = ""
    roles = []

    def __init__(self, name, roles):
        self.name = name
        self.roles = roles
        Users.add(self)
    
    def __str__(self):
        return(f'User[{self.name}] has roles: {self.roles}')

class Users:
    users = {}

    @staticmethod
    def add(user):
        Users.users[user.name] = user

    def roles(self):
        return self.roles
    
    @staticmethod
    def row(name):
        """ returns the user row """
        return Users.users[name]


User("Sam", ("sa", "dev"))
User("Client1", ("tenant", "manager"))
User("Client2", ("renter", "manager"))

sam_row = Users.row("Sam")
print(f'Sam: {sam_row}')

"""
this is a super-simplistic auth_provider ( a STUB)
will typically user provider for sql
"""