# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Questions(object):

    """Implementation of the 'questions' model.

    TODO: type model description here.

    Attributes:
        text (str): TODO: type description here.
        position (int): TODO: type description here.
        answer (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "text": 'text',
        "position": 'position',
        "answer": 'answer'
    }

    _nullables = [
        'position',
    ]

    def __init__(self,
                 text=None,
                 position=None,
                 answer=None):
        """Constructor for the Questions class"""

        # Initialize members of the class
        self.text = text 
        self.position = position 
        self.answer = answer 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        text = dictionary.get("text") if dictionary.get("text") else None
        position = dictionary.get("position") if dictionary.get("position") else None
        answer = dictionary.get("answer") if dictionary.get("answer") else None
        # Return an object of this model
        return cls(text,
                   position,
                   answer)
