import json
# from abc import ABCMeta, abstractmethod


class Resource(object):

    ''' An abstract class to represent some objects used by our SDK such as
    Account, SignatureRequest, Template, Team, UnclaimedDraft, Embedded.
    These objects share the same way of storing data.

    Information and settings are stored physically in `self.json_data`, and
    can be retrieved by using the OOP way.

    '''

    # __metaclass__ = ABCMeta
    json_data = None

    def __init__(self, jsonstr=None, key=None):
        ''' Initialization of the object

        Args:
            jsonstr (str): a raw JSON string that is returned by a request.
                We store all the data in `self.json_data` and use `__getattr__`
                and `__setattr__` to make the data accessible like attributes
                of the object
            key (str): Optional key to use with jsonstr. If `key` exists, we'll
                load the data of `jsonstr[key]` instead of the whole `jsonstr`
        '''
        super(Resource, self).__init__()
        if jsonstr is not None:
            if key is not None:
                object.__setattr__(
                    self, 'json_data', json.loads(json.dumps(jsonstr))[key])
            else:
                object.__setattr__(
                    self, 'json_data', json.loads(json.dumps(jsonstr)))

    def __getattr__(self, name):
        if name != "json_data":
            if name in self.json_data:
                return self.json_data[name]
            raise AttributeError('%s has no attribute "%s"' % (self.__class__.__name__, name))

    def __setattr__(self, name, value):
        if name != "json_data":
            if name in self.json_data:
                self.json_data[name] = value
            else:
                raise AttributeError('%s has no attribute "%s"' % (self.__class__.__name__, name))
        else:
            self.__dict__["json_data"] = value
