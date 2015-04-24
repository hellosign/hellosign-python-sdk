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


class HSFormat(object):
    ''' Authentication object using HelloSign's access token '''

    def __init__(self):
        ''' Initialziation of the object

        Args:

        '''

    @classmethod
    def fakef(self):
        return 'Hello'

    @staticmethod
    def format_file_params(files):
        '''
            Utility method for formatting file parameters for transmission
        '''
        files_payload = {}
        if files:
            for idx, filename in enumerate(files):
                files_payload["file[" + str(idx) + "]"] = open(filename, 'rb')
        return files_payload

    @staticmethod
    def format_file_url_params(file_urls):
        '''
            Utility method for formatting file URL parameters for transmission
        '''
        file_urls_payload = {}
        if file_urls:
            for idx, fileurl in enumerate(file_urls):
                file_urls_payload["file_url[" + str(idx) + "]"] = fileurl
        return file_urls_payload

    @staticmethod
    def format_param_list(listed_params, output_name):
        '''
            Utility method for formatting lists of parameters for api consumption
            Useful for email address lists, etc
            Args:
                listed_params (list of values) - the list to format
                output_name (str) - the parameter name to prepend to each key
        '''
        output_payload = {}
        if listed_params:
            for index, item in enumerate(listed_params):
                output_payload[str(output_name) + "[" + str(index) + "]" ] = item
        return output_payload

    @staticmethod
    def format_dict_list(list_of_dicts, output_name, key=None):
        '''
            Utility method for formatting lists of dictionaries for api consumption.
            Takes something like [{name: val1, email: val2},{name: val1, email: val2}] for signers
            and outputs:
            signers[0][name]  : val1
            signers[0][email] : val2
            ... 

            Args:
                list_of_dicts (list of dicts) - the list to format
                
                output_name (str) - the parameter name to prepend to each key
                
                key (str, optional) - Used for substituting a key present in the dictionaries for the index. The above might become signers['Lawyer']['name'] instead of using a numerical index if the key "role_name" was specified.

        '''
        output_payload = {}
        if list_of_dicts:
            for index, dictionary in enumerate(list_of_dicts):
                index_or_key = dictionary[key] if key else str(index)
                base_name = output_name + '[' + index_or_key + ']'
                for (param, value) in dictionary.items():
                    if param != key: #key params are stripped
                        output_payload[base_name + '[' + param + ']'] = value
        return output_payload

    @staticmethod
    def format_single_dict(dictionary, output_name):
        '''
            Currently used for metadata fields
        '''
        output_payload = {}
        if dictionary:
            for (k, v) in dictionary.items():
                output_payload[output_name + '[' + k + ']'] = v
        return output_payload

    @staticmethod
    def format_custom_fields(list_of_custom_fields):
        '''
            Custom fields formatting for submission
        '''
        output_payload = {}
        if list_of_custom_fields:
            # custom_field: {"name": value}
            for custom_field in list_of_custom_fields:
                for key, value in custom_field.items():
                    output_payload["custom_fields[" + key + "]"] = value
        return output_payload

    @staticmethod
    def strip_none_values(dictionary):
        if dictionary:
            return dict((key, value) for (key, value) in dictionary.items() if value)