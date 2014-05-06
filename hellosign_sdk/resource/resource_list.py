import json

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
