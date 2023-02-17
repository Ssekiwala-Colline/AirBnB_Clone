#!/usr/bin/python3
from models.base_model import BaseModel
"""Class that
represent
the review"""


class Review(BaseModel):

    """Initialize review class
    instance
    of basemodel class"""
    place_id = ''
    user_id = ''
    text = ''
