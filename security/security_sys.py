"""
Placeholder stubs
"""

from sqlalchemy.orm import session
from sqlalchemy import event, MetaData
import safrs
import database.models
# import security.authentication_provider.mem_auth_row as authentication_provider  # TODO: your provider here
import security.authentication_provider.db_auth as authentication_provider  # TODO: your provider here
from sqlalchemy import event, MetaData
from sqlalchemy.orm import with_loader_criteria

print(f'\nsecurity_sys loaded via api_logic_server_run.py -- import \n')

db = safrs.DB         # Use the safrs.DB, not db!
session = db.session  # sqlalchemy.orm.scoping.scoped_session



class Security:

    """
    CurrentUser = Security.current_user()  # TODO - how to do this??
    Returns user rows, with UserRoleList
    """
    
    @classmethod
    def current_user(cls):
        """ STUB for authorization """
        # return authentication_provider.Users.row("Client1")
        return authentication_provider.get_user("aneu")


    @staticmethod
    @classmethod
    def current_user_has_role(role_name: str) -> bool: 
        '''
        If user has role xyz, then for update authorization he/she can... 
        '''
        result = False
        for each_role in __class__.current_user.UserRoleList:
            if role_name == each_role.name:
                result = True
                break
        return result
    

class Grant:
    """
    Invoke these to declare Role Permissions.

    Use code completion to discover models.
    """

    grants_by_table = {}
    '''
    Dict keyed by Table name, value is a (role,filter)
    '''

    def __init__(self, on_entity: object, to_role: object = None, filter: object = None):
        '''
        Create grant for <on_entity> / <to_role>

        Example
        =======
        Grant(  on_entity = models.Category,  # use code completion
                to_role = Roles.tenant,
                filter = models.Category.Id == Security.current_user().client_id)  # User table attributes
        
        Args
        ----
            on_entity: a class from models.py
            to_role: valid role name from Authentication Provider
            filter: where clause to be added
        
        per calls from declare_security.py
        '''
        self.class_name = on_entity._s_class_name
        self.role_name = to_role
        self.filter = filter
        self.table_name = on_entity.__tablename__  # TODO verify
        if (self.table_name not in self.grants_by_table):
            Grant.grants_by_table[self.table_name] = []
        Grant.grants_by_table[self.table_name].append( self )

    @staticmethod
    def exec_grants(orm_execute_state):
        '''
        SQLAlchemy select event for current user's roles, append that role's grant filter to the SQL before execute 
        '''
        user = Security.current_user()
        mapper = orm_execute_state.bind_arguments['mapper']   # TODO table vs class (!!)
        table_name = mapper.persist_selectable.fullname   # mapper.mapped_table.fullname disparaged
        if table_name in Grant.grants_by_table:
            for each_grant in Grant.grants_by_table[table_name]:
                for each_user_role in user.UserRoleList:
                    if each_grant.role_name == each_user_role.name:
                        print(f'Execute Permission for class / role: {table_name} / {each_grant.role_name} - {each_grant.filter}')
                        orm_execute_state.statement = orm_execute_state.statement.options(
                            with_loader_criteria(database.models.Category, each_grant.filter))


@event.listens_for(session, 'do_orm_execute')
def receive_do_orm_execute(orm_execute_state):
    "listen for the 'do_orm_execute' event from SQLAlchemy"
    if (
        orm_execute_state.is_select
        and not orm_execute_state.is_column_load
        and not orm_execute_state.is_relationship_load
    ):            
        # print(f'receive_do_orm_execute alive')
        use_grant_class = True
        if use_grant_class:
            mapper = orm_execute_state.bind_arguments['mapper']   # TODO table vs class (!!case sensitive if names differ)
            table_name = mapper.persist_selectable.fullname   # mapper.mapped_table.fullname disparaged
            if table_name == "User":
                pass  # TODO bypass authorization when rules are running
                # print(f'avoid recursion on User table')
            else:
                Grant.exec_grants(orm_execute_state) # SQL read check grants
        else:  # old code (disabled)
            mapper = orm_execute_state.bind_arguments['mapper']
            table = mapper.persist_selectable   # mapper.mapped_table.fullname disparaged
            if table.fullname == "Category":
                orm_execute_state.statement = orm_execute_state.statement.options(
                    with_loader_criteria(database.models.Category, database.models.Category.Id == 1))
