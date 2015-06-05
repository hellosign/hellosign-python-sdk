import json

#
# The MIT License (MIT)
# 
# Copyright (C) 2014 hellosign.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

class Resource(object):

    ''' An abstract class to represent some objects used by our SDK such as
    Account, SignatureRequest, Template, Team, UnclaimedDraft, Embedded.
    These objects share the same way of storing data.

    Information and settings are stored physically in `self.json_data`, and
    can be retrieved by using the OOP way.

    '''

    INTERNALS = ['json_data', 'warnings']

    json_data = None
    warnings = None

    def __init__(self, jsonstr=None, key=None, warnings=None):
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
        self.warnings = warnings
        if jsonstr is not None:
            data = json.loads(json.dumps(jsonstr))
            if key is not None:
                object.__setattr__(self, 'json_data', data[key])
            else:
                object.__setattr__(self, 'json_data', data)

    def __getattr__(self, name):
        if name not in self.INTERNALS:
            if name in self.json_data:
                return self.json_data[name]
            raise AttributeError('%s has no attribute "%s"' % (self.__class__.__name__, name))

    def __setattr__(self, name, value):
        if name not in self.INTERNALS:
            if name in self.json_data:
                self.json_data[name] = value
            else:
                raise AttributeError('%s has no attribute "%s"' % (self.__class__.__name__, name))
        else:
            self.__dict__[name] = value

    def get_warnings(self):
        ''' Return the list of warnings associated with this object, or None if there aren't any '''
        if self.warnings and len(self.warnings) > 0:
            return self.warnings
