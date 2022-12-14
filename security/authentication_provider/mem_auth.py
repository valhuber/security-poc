
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
        return(f'User[{self.name} has roles: {self.roles}')

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


sam = User("Sam", ("sa", "dev"))
client1 = User("Client1", ("tenant", "manager"))
client2 = User("Client2", ("rentor", "manager"))
sam_row = Users.row("Sam")
print(f'Sam: {sam}')
