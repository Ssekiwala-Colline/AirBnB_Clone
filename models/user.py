#!/usr/bin/python3
from models.base_model import BaseModel

"""Class that
represent
the user"""


class User(BaseModel):
    """Initialize user class
    instance
    of basemodel class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
