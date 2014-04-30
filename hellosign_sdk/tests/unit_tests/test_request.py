from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.utils.request import HSRequest
from hellosign_sdk.utils.exception import BadRequest
import tempfile
import os


class Request(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_get(self):
        request = HSRequest(self.client.auth)
        response = request.get(url='http://httpbin.org/get',
                               headers={'Custom-Header': 'Nothing'},
                               parameters={'param': 'Nothing'},
                               get_json=False)
        self.assertEquals(response.status_code, 200)
        response = request.get(url='http://httpbin.org/get',
                               get_json=True)
        self.assertEquals(isinstance(response, dict), True)

    def test_get_https(self):
        request = HSRequest(self.client.auth)
        response = request.get(url='https://httpbin.org/get',
                               headers={'Custom-Header': 'Nothing'},
                               parameters={'param': 'Nothing'},
                               get_json=False)
        self.assertEquals(response.status_code, 200)
        response = request.get(url='https://httpbin.org/get',
                               get_json=True)
        self.assertEquals(isinstance(response, dict), True)

        try:
            response = request.get(url='https://www.hellosign.com/oauth/token',
                                   get_json=True)
        except BadRequest, e:
            self.assertEquals('400 error' in str(e), True)

    def test_post(self):
        request = HSRequest(self.client.auth)
        response = request.post(url='http://httpbin.org/post',
                                data={"test": "None"}, get_json=False,
                                headers={'Custom-Header': 'Nothing'}
                                )
        self.assertEquals(response.status_code, 200)
        response = request.post(url='http://httpbin.org/post',
                                data={"test": "None"}, get_json=True
                                )

    def test_post_https(self):
        request = HSRequest(self.client.auth)
        response = request.post(url='https://httpbin.org/post',
                                data={"test": "None"}, get_json=False,
                                headers={'Custom-Header': 'Nothing'}
                                )
        self.assertEquals(response.status_code, 200)
        response = request.post(url='https://httpbin.org/post',
                                data={"test": "None"}, get_json=True
                                )

    def test_get_file(self):
        request = HSRequest(self.client.auth)
        f = tempfile.NamedTemporaryFile(delete=True)
        temp_filename = f.name
        f.close()
        response = request.get_file(url='http://httpbin.org/robots.txt',
                                    headers={'Custom-Header': 'Nothing'},
                                    filename=temp_filename)
        os.unlink(temp_filename)
        self.assertEquals(response, True)

        response = request.get_file(url='http://httpbin.org/robots.txt',
                                    headers={'Custom-Header': 'Nothing'},
                                    filename='')
        self.assertEquals(response, False)

    def test_get_file_https(self):
        request = HSRequest(self.client.auth)
        f = tempfile.NamedTemporaryFile(delete=True)
        temp_filename = f.name
        f.close()

        response = request.get_file(url='https://httpbin.org/robots.txt',
                                    headers={'Custom-Header': 'Nothing'},
                                    filename=temp_filename)
        os.unlink(temp_filename)
        self.assertEquals(response, True)

        response = request.get_file(url='https://httpbin.org/robots.txt',
                                    headers={'Custom-Header': 'Nothing'},
                                    filename='')
        self.assertEquals(response, False)
