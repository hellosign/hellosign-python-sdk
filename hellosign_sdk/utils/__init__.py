from .exception import HSException
from .exception import NoAuthMethod
from .exception import HTTPError
from .exception import BadRequest
from .exception import Unauthorized
from .exception import PaymentRequired
from .exception import Forbidden
from .exception import NotFound
from .exception import MethodNotAllowed
from .exception import NotAcceptable
from .exception import RequestTimeout
from .exception import Conflict
from .exception import Gone
from .exception import RequestURITooLong
from .exception import UnsupportedMediaType
from .exception import RequestedRangeNotSatisfiable
from .exception import InternalServerError
from .exception import MethodNotImplemented
from .exception import BadGateway
from .exception import ServiceUnavailable
from .exception import GatewayTimeout

from .request import HSRequest
from .hsaccesstokenauth import HSAccessTokenAuth

from .hsformat import HSFormat

class api_resource:
    ''' Decorator that transforms response data into a Resource '''
    
    def __init__(self, obj_cls):
        self.obj_cls = obj_cls

    def __call__(self, f):
        def make_resource(*args, **kwargs):
            ''' Make a Resource instance '''

            obj = None
            json_response = f(*args, **kwargs)

            if json_response:
                key = self._uncamelize(self.obj_cls.__name__)
                if key not in json_response:
                    raise ValueError('"%s" is expected in the response' % key)
                obj_data = json_response[key]
                warnings = json_response.get('warnings')
                obj = self.obj_cls(obj_data, None, warnings)

            return obj
        make_resource.__name__ == f.__name__
        return make_resource

    def _uncamelize(self, s):
        ''' Convert a camel-cased string to using underscores '''
        res = ''
        if s:
            for i in range(len(s)): 
                if i > 0 and s[i].lower() != s[i]:
                    res += '_'
                res += s[i].lower()
        return res

__all__ = [HSException, NoAuthMethod, HTTPError, BadRequest, Unauthorized, PaymentRequired, Forbidden, NotFound, MethodNotAllowed,
           NotAcceptable, RequestTimeout, Conflict, Gone, RequestURITooLong, UnsupportedMediaType, RequestedRangeNotSatisfiable, 
           MethodNotImplemented, InternalServerError, BadGateway, ServiceUnavailable, GatewayTimeout, HSRequest, HSAccessTokenAuth, 
           HSFormat, api_resource]
