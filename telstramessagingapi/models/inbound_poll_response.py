# -*- coding: utf-8 -*-

"""
    telstramessagingapi.models.inbound_poll_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class InboundPollResponse(object):

    """Implementation of the 'InboundPollResponse' model.

    Poll for incoming messages returning the latest. Only works if no url was
    specified when provisioning a number.

    Attributes:
        destination_address (string): The phone number (recipient) that the
            message was sent to(in E.164 format).
        sender_address (string): The phone number (sender) that the message
            was sent from (in E.164 format).
        message (string): Text body of the message that was sent
        sent_timestamp (string): The date and time when the message was
            recieved by recipient.
        message_id (string): Optional message ID of the SMS you sent. Use this
            ID to viewthe message status or get responses.
        status (string): Message status from the server

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "destination_address" : "destinationAddress",
        "sender_address" : "senderAddress",
        "message" : "message",
        "sent_timestamp" : "sentTimestamp",
        "message_id" : "messageId",
        "status" : "status"
    }

    def __init__(self,
                 destination_address=None,
                 sender_address=None,
                 message=None,
                 sent_timestamp=None,
                 message_id=None,
                 status=None):
        """Constructor for the InboundPollResponse class"""

        # Initialize members of the class
        self.destination_address = destination_address
        self.sender_address = sender_address
        self.message = message
        self.sent_timestamp = sent_timestamp
        self.message_id = message_id
        self.status = status


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
        destination_address = dictionary.get("destinationAddress")
        sender_address = dictionary.get("senderAddress")
        message = dictionary.get("message")
        sent_timestamp = dictionary.get("sentTimestamp")
        message_id = dictionary.get("messageId")
        status = dictionary.get("status")

        # Return an object of this model
        return cls(destination_address,
                   sender_address,
                   message,
                   sent_timestamp,
                   message_id,
                   status)


