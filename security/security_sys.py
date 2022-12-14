"""
Placeholder stubs
"""

from sqlalchemy.orm import session
from sqlalchemy import event, MetaData
import safrs
import database.models

print(f'\nsecurity_sys loaded via api_logic_server_run.py -- import \n')

db = safrs.DB         # Use the safrs.DB, not db!
session = db.session  # sqlalchemy.orm.scoping.scoped_session

from sqlalchemy import event, MetaData
from sqlalchemy.orm import with_loader_criteria


def get_current_user():
    """ stand-in for authorization """
    return Users.row("Sam")


class Grants():  # nah
    """
    store grants, by entity
    """
    def __init__(self):
        self.grants = {}  # entity, RolePermissions()


class Grant:

    """Invoke these to declare Role Permissions.

    Use code completion to discover models.
    """

    grants = {}

    def __init__(self, on_entity: object, to_role: object = None, filter: object = None):
        if (to_role not in self.grants):
            self.grants[to_role] = []
        self.grants[to_role].append( (on_entity, filter) )

    @staticmethod
    def exec_grants(orm_execute_state):
        user = get_current_user()
        for each_role in user.roles:
            grants_for_role = Grant.grants[each_role]
            for each_permission in grants_for_role:
                mapper = orm_execute_state.bind_arguments['mapper']
                table = mapper.persist_selectable   # mapper.mapped_table.fullname disparaged
                if table.fullname == "Category":
                    orm_execute_state.statement = orm_execute_state.statement.options(
                        with_loader_criteria(database.models.Category, database.models.Category.Id == 1))



    @staticmethod
    def access(on_entity: object, to_role: object = None, filter: object = None):  # nah
        """
        each grant winds up executing:
            orm_execute_state.statement = orm_execute_state.statement.options(
                with_loader_criteria(database.models.Category, database.models.Category.Id == 1))
                    sqlalchemy.sql.elements.BinaryExpression

        example:
            TBD

        args:
            on_entity: mapped class
            to_role: role
            filter: sqlalchemy.sql.elements.BinaryExpression, e.g. database.models.Category.Id == 1
        """
        # if (on_entity not in grants_singleton.grants):

        return None


# **********************
# stand-in for db users
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
client1 = User("Client1", "tenant")
sam_row = Users.row("Sam")
print(f'Sam: {sam}')

@event.listens_for(session, 'do_orm_execute')
def receive_do_orm_execute(orm_execute_state):
    "listen for the 'do_orm_execute' event"
    if (
        orm_execute_state.is_select
        and not orm_execute_state.is_column_load
        and not orm_execute_state.is_relationship_load
    ):            
        # print(f'receive_do_orm_execute alive')
        use_grant_class = True
        if use_grant_class:
            Grant.exec_grants(orm_execute_state)
        else:
            mapper = orm_execute_state.bind_arguments['mapper']
            table = mapper.persist_selectable   # mapper.mapped_table.fullname disparaged
            if table.fullname == "Category":
                orm_execute_state.statement = orm_execute_state.statement.options(
                    with_loader_criteria(database.models.Category, database.models.Category.Id == 1))
    # print(f'boo ha')
