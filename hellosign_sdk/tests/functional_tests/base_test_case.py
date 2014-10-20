from unittest import TestCase
from hellosign_sdk import HSClient
from hellosign_sdk.tests import test_helper

class BaseTestCase(TestCase):
    ''' Base for all test cases '''

    warned = False

    def setUp(self):
        params = {
            'api_key': test_helper.api_key
        }
        try:
            params['env'] = test_helper.env
        except AttributeError:
            params['env'] = 'production'
        self.client = HSClient(**params)
        self.client_id = test_helper.client_id
        self.client_secret = test_helper.client_secret

        if params['env'] == 'production' and not BaseTestCase.warned:
            BaseTestCase.warned = True
            print("\n\n")
            print(" ==================================================================")
            print(" = WARNING: We advise against running those tests against your    =")
            print(" = personal account as it performs destructive actions            =")
            print(" ==================================================================")
            while True:
                resp = raw_input(' > Continue (type yes or hit Ctrl+C to exit)?')
                if resp == 'yes':
                    # Continue to tests
                    break
                elif resp == 'no':
                    # Stop here
                    import sys
                    sys.exit()
                else:
                    # Ask question again
                    pass 
            print

        print
