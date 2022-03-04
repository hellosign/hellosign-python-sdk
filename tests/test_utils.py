import os
import json


def get_base_path():
    return os.path.realpath('') + f'/../oas/test_fixtures'


def get_fixture_data(filename):
    path = get_base_path() + f'/{filename}.json'

    file = open(path, 'r')
    fixture_data = json.load(file)
    file.close()

    return fixture_data
