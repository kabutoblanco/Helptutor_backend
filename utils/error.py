"""Django custom exceptions."""


# Django
from django.utils.encoding import force_text

# rest_framework
from rest_framework import status
from rest_framework.exceptions import APIException


class ValidationError(APIException):
    """ValidationError define custom errors."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "detail"

    def __init__(self, detail):
        if detail is not None:
            self.detail = detail
        else:
            self.detail = {'detail': force_text(self.default_detail)}
