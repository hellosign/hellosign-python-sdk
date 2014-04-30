class HSException(Exception):
    """General exception class

    We use this object to raise exceptions when none of its child classes is
    suitable for use.

    """

    def __init__(self, message):
        self.message = message
        self.type = self.__class__.__name__

    def __str__(self):
        return self.message


class NoAuthMethod(HSException):
    """Exception when no authentication information found"""


class HTTPError(HSException):
    """Exception when an HTTP error found"""

    def __init__(self, message, http_code=None):
        super(HTTPError, self).__init__(message)
        self.http_code = http_code


class BadRequest(HTTPError):
    """docstring for BadRequest"""


class Unauthorized(HTTPError):
    """docstring for Unthorized"""


class PaymentRequired(HTTPError):
    """docstring for PaymentRequired"""


class Forbidden(HTTPError):
    """docstring for Forbidden"""


class NotFound(HTTPError):
    """docstring for NotFound"""


class MethodNotAllowed(HTTPError):
    """docstring for MethodNotAllowed"""


class NotAcceptable(HTTPError):
    """docstring for NotAcceptable"""


class RequestTimeout(HTTPError):
    """docstring for RequestTimeout"""


class Conflict(HTTPError):
    """docstring for Conflict"""


class Gone(HTTPError):
    """docstring for Gone"""


class RequestURITooLong(HTTPError):
    """docstring for RequestURITooLong"""


class UnsupportedMediaType(HTTPError):
    """docstring for UnsupportedMediaType"""


class RequestedRangeNotSatisfiable(HTTPError):
    """docstring for RequestedRangeNotSatisfiable"""


class InternalServerError(HTTPError):
    """docstring for InternalServerError"""


class MethodNotImplemented(HTTPError):
    """docstring for NotImplemented"""


class BadGateway(HTTPError):
    """docstring for BadGateway"""


class ServiceUnavailable(HTTPError):
    """docstring for ServiceUnavailable"""


class GatewayTimeout(HTTPError):
    """docstring for GatewayTimeout"""
