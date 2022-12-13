"""
Placeholder stubs
"""

from sqlalchemy.orm import session
from sqlalchemy import event, MetaData

print(f'\nsecurity_sys loaded\n')

@event.listens_for(SomeSessionClassOrObject, 'do_orm_execute')
def receive_do_orm_execute(orm_execute_state):
    "listen for the 'do_orm_execute' event"
    print(f'receive_do_orm_execute alive')
    print(f'boo ha')

    # ... (event handling logic) ...

def activate(session: session):
    event.listen(a_session, "before_flush", receive_do_orm_execute)

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