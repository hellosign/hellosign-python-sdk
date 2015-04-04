from unittest import TestCase
from hellosign_sdk.utils import HSFormat
import os


class TestHSFormat(TestCase):
    ''' Testing for formatting utilities used in this wrapper '''

    def test_format_file_params(self):

        file1 = os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"
        file2 = os.path.dirname(os.path.realpath(__file__)) + "/docs/nda-text-tags.pdf"

        input_params = [file1, file2]
        output_name = 'file[0]'

        result = HSFormat.format_file_params(input_params)

        keys = result.keys()

        attribute = hasattr(result[keys[0]], 'read') #check if file (can be read)

        self.assertTrue(attribute)
        self.assertTrue(output_name in keys)

    def test_format_file_url_params(self):

        input_params = ['http://website.com/path/to/file/1.png', 'http://website.com/path/to/file/2.png', 'http://website.com/path/to/file/3.png']
        expected_result = {
            'file_url[0]': 'http://website.com/path/to/file/1.png',
            'file_url[1]': 'http://website.com/path/to/file/2.png',
            'file_url[2]': 'http://website.com/path/to/file/3.png'
        }

        result = HSFormat.format_file_url_params(input_params)

        self.assertEquals(result, expected_result)

    def test_format_param_list(self):

            input_params = ['angry', 'flappy', 'kiwi']
            expected_result = {
                'birds[0]': 'angry',
                'birds[1]': 'flappy',
                'birds[2]': 'kiwi'
            }

            result = HSFormat.format_param_list(input_params, 'birds')

            self.assertEquals(result, expected_result)

    def test_format_dict_list(self):

            input_params = [
                {'name': 'Cloud', 'weapon': 'sword', 'hp': 9000},
                {'name': 'Tifa', 'weapon': 'fists', 'hp': 7000},
                {'name': 'Aerith', 'weapon': 'staff', 'hp': 6589}
            ]

            label = 'team'

            expected_result = {
                'team[0][name]': 'Cloud',
                'team[0][weapon]': 'sword',
                'team[0][hp]': 9000,
                'team[1][name]': 'Tifa',
                'team[1][weapon]': 'fists',
                'team[1][hp]': 7000,
                'team[2][name]': 'Aerith',
                'team[2][weapon]': 'staff',
                'team[2][hp]': 6589
            }

            key = 'name'

            expected_result_with_key = {
                'team[Cloud][weapon]': 'sword',
                'team[Cloud][hp]': 9000,
                'team[Tifa][weapon]': 'fists',
                'team[Tifa][hp]': 7000,
                'team[Aerith][weapon]': 'staff',
                'team[Aerith][hp]': 6589
            }

            result = HSFormat.format_dict_list(input_params, label)

            self.assertEquals(result, expected_result)

            result = HSFormat.format_dict_list(input_params, label, key)

            self.assertEquals(result, expected_result_with_key)

    def test_format_single_dict(self):

        input_params = {
            'hotdog': 'relish',
            'bibimbap': 'kochujan'
        }

        label = 'fuds'

        expected_result = {
            'fuds[hotdog]': 'relish',
            'fuds[bibimbap]': 'kochujan'
        }

        result = HSFormat.format_single_dict(input_params, label)

        self.assertEquals(result, expected_result)

    def test_format_custom_fields(self):

        input_params = [{"level": 36, "class": "dragoon" }]

        expected_result = {
            'custom_fields[level]': 36,
            'custom_fields[class]': 'dragoon'
        }

        result = HSFormat.format_custom_fields(input_params)

        self.assertEquals(result, expected_result)

    def test_strip_none_values(self):

        input_params = {
            'param1': 'something',
            'param2': None,
            'param3': None
        }

        result = {}
        result = HSFormat.strip_none_values(input_params)
        numkeys = len(result.keys())

        self.assertEquals(numkeys, 1)