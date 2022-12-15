from dotmap import DotMap  # a dict, but you can say aDict.name instead of aDict['name']... like a row

# **********************
# in mem auth provider
# **********************

users = {}

def get_user(name):
    """
    Must return a row object with attributes name and UserRoleList (others as required)
    role_list is a list of row objects with attribute name

    row object is a DotMap (as here) or a SQLAlchemy row
    """
    return users[name]

def add_user(name: str, role_list):
    user = DotMap()
    user.name = name
    user.UserRoleList = []
    for each_role in role_list:
        r = DotMap()
        r.name = each_role
        user.UserRoleList.append(r)
    users[name] = user

add_user("Sam", ("sa", "dev"))
add_user("Client1", ("tenant", "manager"))
add_user("Client2", ("renter", "manager"))

sam_row = get_user("Sam")
print(f'Sam: {sam_row}')

"""
this is a super-simplistic auth_provider ( a STUB)
will typically user provider for sql
"""