from security.security_sys import Grant, User
from database import models
import safrs
import sqlalchemy
import logging

db = safrs.DB         # Use the safrs.DB, not db!
session = db.session  # sqlalchemy.orm.scoping.scoped_session

Grant.access(
        on_entity = models.Customer,  # need way to say "any"
        to_role = "standard_role",
        where = session.query(models.Order).
                filter(models.Order.Id == User.row.ParticipantId))