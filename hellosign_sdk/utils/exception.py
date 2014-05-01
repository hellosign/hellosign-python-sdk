class HSException(Exception):
    ''' General HelloSign exception

    We use this object to raise exceptions when none of its child classes is
    suitable for use.

    '''

    def __init__(self, message):
        self.message = message
        self.type = self.__class__.__name__

    def __str__(self):
        return self.message


class NoAuthMethod(HSException):
    ''' No authentication data '''

class HTTPError(HSException):
    ''' General HTTP error '''

    def __init__(self, message, http_code=None):
        super(HTTPError, self).__init__(message)
        self.http_code = http_code

class BadRequest(HTTPError):
    ''' Bad request data '''

class Unauthorized(HTTPError):
    ''' Bad authentication data '''

class PaymentRequired(HTTPError):
    ''' Payment/upgrade required to proceed '''

class Forbidden(HTTPError):
    ''' Not authorized to proceed '''

class NotFound(HTTPError):
    ''' Resource not found '''

class MethodNotAllowed(HTTPError):
    ''' HTTP method not supported '''

class NotAcceptable(HTTPError):
    ''' Accept header conflicts with the returned resource type '''

class RequestTimeout(HTTPError):
    ''' Request timeout '''

class Conflict(HTTPError):
    ''' Request correctly formulated but unable to proceed due to a conflict '''

class Gone(HTTPError):
    ''' Resource deleted '''

class RequestURITooLong(HTTPError):
    ''' Request URI too long '''

class UnsupportedMediaType(HTTPError):
    ''' Unsupported media type '''

class RequestedRangeNotSatisfiable(HTTPError):
    ''' Invalid resource data chunk requested '''

class InternalServerError(HTTPError):
    ''' Server error '''

class MethodNotImplemented(HTTPError):
    ''' Not implemented '''

class BadGateway(HTTPError):
    ''' Bad gateway '''

class ServiceUnavailable(HTTPError):
    ''' Service unavailable '''

class GatewayTimeout(HTTPError):
    ''' Gateway timeout '''
