# -*- coding: utf-8 -*-

"""
    telstramessagingapi.models.provision_number_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class ProvisionNumberRequest(object):

    """Implementation of the 'ProvisionNumberRequest' model.

    TODO: type model description here.

    Attributes:
        active_days (int): TODO: type description here.
        notify_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_days" : "activeDays",
        "notify_url" : "notifyURL"
    }

    def __init__(self,
                 active_days=None,
                 notify_url=None):
        """Constructor for the ProvisionNumberRequest class"""

        # Initialize members of the class
        self.active_days = active_days
        self.notify_url = notify_url


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        active_days = dictionary.get("activeDays")
        notify_url = dictionary.get("notifyURL")

        # Return an object of this model
        return cls(active_days,
                   notify_url)


