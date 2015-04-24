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


class ResourceList(list):
    ''' A container to hold resource list items and paging information '''

    items_keys = {
        'SignatureRequest': 'signature_requests',
        'Template': 'templates'
    }

    page = 0
    num_pages = 0
    num_results = 0
    page_size = 0

    def __init__(self, item_cls, data):
        ''' Initialization of the list

        Args:
            item_cls (str): Object class matching the list items
            data (str or dict): A dictionary or raw JSON string that is returned by a request.
        '''
        super(ResourceList, self).__init__()
        if data is not None:

            data = json.loads(data) if type(data) is not dict else data
            paging = data['list_info']
            raw_items = data.get(self.items_keys[item_cls.__name__])

            if raw_items:

                # Wrap raw items in object containers
                for raw_item in raw_items:
                    self.append(item_cls(raw_item))

                # Paging info
                self.page = paging['page']
                self.num_pages = paging['num_pages']
                self.num_results = paging['num_results']
                self.page_size = paging['page_size']
