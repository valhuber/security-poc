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

@event.listens_for(session, 'do_orm_execute')
def receive_do_orm_execute(orm_execute_state):
    "listen for the 'do_orm_execute' event"
    if (
        orm_execute_state.is_select
        and not orm_execute_state.is_column_load
        and not orm_execute_state.is_relationship_load
    ):            
        # print(f'receive_do_orm_execute alive')
        mapper = orm_execute_state.bind_arguments['mapper']
        table = mapper.persist_selectable   # mapper.mapped_table.fullname disparaged
        if table.fullname == "Category":
            orm_execute_state.statement = orm_execute_state.statement.options(
                with_loader_criteria(database.models.Category, database.models.Category.Id == 1))
    # print(f'boo ha')


class Grant:

    """Invoke these functions to declare Role Permissions.

    Use code completion to discover models.
    """

    @staticmethod
    def access(on_entity: any, to_role: any = None, where: str = ""):
        """
        Derive parent column as sum of designated child column, optional where

        Example:

        """
        return None


class User:

    @staticmethod
    def roles():
        return None
    
    @staticmethod
    def row():
        """ returns the user row """
        return None