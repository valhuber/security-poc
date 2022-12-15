from dotmap import DotMap

# **********************************
# authentication provider interface
# **********************************


def get_user(name):
    """
    Must return a row object with attributes name and role_list
    role_list is a list of row objects with attribute name

    row object is a DotMap or a SQLAlchemy row
    """
    return {}

