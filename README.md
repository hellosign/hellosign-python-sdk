Hellosign Python SDK
-------------------
[![Build Status](https://travis-ci.org/minhdanh/hellosign-python-sdk.png?branch=master)](https://travis-ci.org/minhdanh/hellosign-python-sdk)
[![Coverage Status](https://coveralls.io/repos/minhdanh/hellosign-python-sdk/badge.png)](https://coveralls.io/r/minhdanh/hellosign-python-sdk)
[![Code Health](http://landscape.io/github/minhdanh/hellosign-python-sdk/master/landscape.png)](http://landscape.io/github/minhdanh/hellosign-python-sdk/master)
[![Latest Version](https://pypip.in/v/hellosign-python-sdk/badge.png)](https://pypi.python.org/pypi/hellosign-python-sdk/)
[![Downloads](https://pypip.in/d/hellosign-python-sdk/badge.png)](https://pypi.python.org/pypi/hellosign-python-sdk/)
[![Dependency Status](https://gemnasium.com/minhdanh/hellosign-python-sdk.png)](https://gemnasium.com/minhdanh/hellosign-python-sdk)



An API wrapper written in Python to interact with HelloSign's API (http://www.hellosign.com)

Note: This is not the final Readme, and the package is not ready yet. It will be ready when it's ready (of course).

## Installation

Install using `easy_install`:

````sh
easy_install hellosign-python-sdk
````

Install using `pip`:

````sh
pip install hellosign-python-sdk
````

## Configuration

In your application, import `HSClient`:

````python
from hellosign.hsclient import HSClient
````

Then create a HSClient object and pass authentication information to initialize it:

````python
# Initialize HSClient using email and password
client = HSClient(api_email="api_user@example.com", api_password="your_password")

# Initialize HSClient using api key
client = HSClient(api_key="your_api_key")

# Initialize HSClient using api token
client = HSClient(api_accesstoken="your_api_access_token", api_accesstokentype="your_api_access_token_type")
````
Note: In case you initialize the HSClient with all the above credentials, the priority order is as follow: api_accesstoken & api_accesstokentype, api_key, then api_email and api_password

## Usage

For more information about the API, please refer to this [link](http://hellosign-python-sdk.readthedocs.org/en/latest/)

### Account

#### Get current account information

````python
client.get_account_info()
````

The account information is then stored in `client.account`. For example, to print the `email_address` of your account:

````python
print client.account.email_address
````

#### Update your account information

````python
client.account.callback_url = "https://www.example.com/callback"
client.update_account_info()
````

#### Create a new HelloSign account

````python
new_account = client.create_account("new_user@example.com", "aL0ngL0ngPa55w0rd")
````


### Signature Request


#### Get a Signature Request

````python
sr = client.get_signature_request("fa5c8a0b0f492d768749333ad6fcc214c111e967")
print sr.requester_email_address
print sr.signature_request_id
````

#### Get a list of your Signature Requests

````python
sr_list = client.get_signature_request_list()

# Print out the name of the signers in every signature request
for sr in sr_list:
    print sr.signatures[0]['signer_name']
````

#### Send a Signature Request

````python
files = ["NDA.pdf", "AppendixA.pdf"]
signers = [{"name": "Jack", "email_address": "jack@example.com"}, {"name": "Jill", "email_address": "jill@example.com"}]
cc_email_addresses = ["lawyer@hellosign.com", "lawler@example.com"]

# Send a signature request with uploaded files
signature_request = client.send_signature_request(test_mode="1", files=None, file_urls=["http://www.example.com/download/sample.pdf"], title="NDA with Acme Co.", subject="The NDA we talked about", message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.", signing_redirect_url="", signers=signers, cc_email_addresses=cc_email_addresses)

# Send a signature request with remote files
signature_request = client.send_signature_request(test_mode="1", files=files, file_urls=None, title="NDA with Acme Co.", subject="The NDA we talked about", message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.", signing_redirect_url="", signers=signers, cc_email_addresses=cc_email_addresses)
````

#### Send a Signature Request with Reusable Form

````python
signers = [{"name": "Jack", "email_address": "jack@example.com"}, {"name": "Jill", "email_address": "jill@example.com"}]
cc_email_addresses = ["lawyer@hellosign.com", "lawler@example.com"]
ccs = [{'email_address': 'lawler@hellosign.com', 'role_name': 'Lawyer 1'},
 {'email_address': 'lawler@example.com', 'role_name': 'Lawyer 2'}]
custom_fields = [{"Field 1": 'Value 1'}, {'Field 2': 'Value 2'}]

# Send a signature request with uploaded files
signature_request = client.send_signature_request_with_rf(test_mode="1", reusable_form_id="fa5c8a0b0f492d768749333ad6fcc214c111e967", title="NDA with Acme Co.", subject="The NDA we talked about", message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.", signing_redirect_url="", signers=signers, ccs=ccs, custom_fields=custom_fields)
````