from security.security_sys import Grant, Security
from database import models
import safrs

db = safrs.DB         # Use the safrs.DB, not db!
session = db.session  # sqlalchemy.orm.scoping.scoped_session


class Roles():
    """ Define Roles here, use for code completion """
    tenant = "tenant"
    renter = "renter"

debug_security = Security.current_user().id
print(f'debug_security: {debug_security}')

Grant(  on_entity = models.Category,    # need way to say "any"
        to_role = Roles.tenant,
        filter = models.Category.Id == Security.current_user().id)  #  e.g., CurrentUser.ParticipantId)

Grant(  on_entity = models.Category,    # need way to say "any"
        to_role = Roles.renter,
        filter = models.Category.Id == 2)  #  e.g., User.row.ParticipantId)
