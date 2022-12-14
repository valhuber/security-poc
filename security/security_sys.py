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
    return Users.row("Client1")


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

    grants_by_class = {}

    def __init__(self, on_entity: object, to_role: object = None, filter: object = None):
        table_name = on_entity._s_class_name
        if (table_name not in self.grants_by_class):
            self.grants_by_class[table_name] = []
        self.grants_by_class[table_name].append( (to_role, filter) )

    @staticmethod
    def exec_grants(orm_execute_state):
        user = get_current_user()
        user_roles = user.roles
        mapper = orm_execute_state.bind_arguments['mapper']   # TODO table vs class (!!)
        table_name = mapper.persist_selectable.fullname   # mapper.mapped_table.fullname disparaged
        grants_debug = Grant
        grants_for_class = Grant.grants_by_class[table_name]  # list of tuples: role, filter

        for each_grant_role, each_grant_filter in grants_for_class:
            if each_grant_role in user_roles:
                print('Permission for user.role: {each_role}')
                orm_execute_state.statement = orm_execute_state.statement.options(
                    with_loader_criteria(database.models.Category, each_grant_filter))


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
client1 = User("Client1", ("tenant", "manager"))
client2 = User("Client2", ("rentor", "manager"))
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

