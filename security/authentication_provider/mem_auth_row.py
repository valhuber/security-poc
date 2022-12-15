from dotmap import DotMap

# **********************
# in mem auth provider
# **********************

users = {}

def add_user(name: str, role_list):
    user = DotMap()
    user.name = name
    user.role_list = []
    for each_role in role_list:
        r = DotMap()
        r.name = each_role
        user.role_list.append(r)
    users[name] = user

def get_user(name):
    return users[name]

add_user("Sam", ("sa", "dev"))
add_user("Client1", ("tenant", "manager"))
add_user("Client2", ("renter", "manager"))

sam_row = get_user("Sam")
print(f'Sam: {sam_row}')

"""
this is a super-simplistic auth_provider ( a STUB)
will typically user provider for sql
"""