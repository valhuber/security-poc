from security.security_sys import Grant, User
from database import models
import safrs
import sqlalchemy
import logging

db = safrs.DB         # Use the safrs.DB, not db!
session = db.session  # sqlalchemy.orm.scoping.scoped_session

Grant( on_entity = models.Category,    # need way to say "any"
        to_role = "public",             # need code completion
        filter = models.Category.Id == 1)  #  e.g., User.row.ParticipantId)

Grant.access(  # nah
        on_entity = models.Category,    # need way to say "any"
        to_role = "public",             # need code completion
        filter = models.Category.Id == 1)  #  e.g., User.row.ParticipantId)

