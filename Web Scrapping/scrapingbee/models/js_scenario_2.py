# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from scrapingbee.models.instruction_2 import Instruction2


class JsScenario2(object):

    """Implementation of the 'js_scenario2' model.

    TODO: type model description here.

    Attributes:
        instructions (List[Instruction2]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "instructions": 'instructions'
    }

    def __init__(self,
                 instructions=None):
        """Constructor for the JsScenario2 class"""

        # Initialize members of the class
        self.instructions = instructions 

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
        instructions = None
        if dictionary.get('instructions') is not None:
            instructions = [Instruction2.from_dictionary(x) for x in dictionary.get('instructions')]
        # Return an object of this model
        return cls(instructions)
