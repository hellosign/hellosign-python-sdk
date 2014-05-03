Hellosign Python SDK
-------------------


An API wrapper written in Python to interact with HelloSign's API (http://www.hellosign.com/api)


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
from hellosign_sdk.hsclient import HSClient
````

Then create a HSClient object and pass authentication information to initialize it:

````python
# Initialize HSClient using email and password
client = HSClient(email="api_user@example.com", password="your_password")

# Initialize HSClient using api key
client = HSClient(api_key="your_api_key")

# Initialize HSClient using api token
client = HSClient(access_token="your_api_access_token", access_token_type="Bearer")
````
Note: In case you initialize the HSClient with all the above credentials, the priority order is as follow: access_token & access_token_type, api_key, then email and password.

## Usage

For more information about the API, please refer to this [link](http://hellosign-python-sdk.readthedocs.org/en/latest/)

### Account

#### Get current account information

````python
account = client.get_account_info()
````

The account information is also stored in `client.account`. For example, to print the `email_address` of your account:

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
signature_request_list = client.get_signature_request_list()

# Print out the name of the signers in every signature request
for signature_request in signature_request_list:
    print signature_request.signatures[0].signer_name
````

#### Send a Signature Request

````python
files = ["NDA.pdf", "AppendixA.pdf"]
signers = [
    {"name": "Jack", "email_address": "jack@example.com"}, 
    {"name": "Jill", "email_address": "jill@example.com"}
]
cc_email_addresses = ["lawyer@hellosign.com", "lawler@example.com"]

# Send a signature request with uploaded files
signature_request = client.send_signature_request(test_mode=True, files=None, file_urls=["http://www.example.com/download/sample.pdf"], title="NDA with Acme Co.", subject="The NDA we talked about", message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.", signing_redirect_url=None, signers=signers, cc_email_addresses=cc_email_addresses)

# Send a signature request with remote files
signature_request = client.send_signature_request(test_mode=True, files=files, file_urls=None, title="NDA with Acme Co.", subject="The NDA we talked about", message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.", signing_redirect_url=None, signers=signers, cc_email_addresses=cc_email_addresses)
````

#### Send a Signature Request with Reusable Form

````python
signers = [
    {"name": "Jack", "email_address": "jack@example.com"}, 
    {"name": "Jill", "email_address": "jill@example.com"}
]
cc_email_addresses = ["lawyer@hellosign.com", "lawler@example.com"]
ccs = [
    {'email_address': 'lawler@hellosign.com', 'role_name': 'Lawyer 1'},
    {'email_address': 'lawler@example.com', 'role_name': 'Lawyer 2'}
]
custom_fields = [
    {"Field 1": 'Value 1'}, 
    {'Field 2': 'Value 2'}
]

# Send a signature request with uploaded files
signature_request = client.send_signature_request_with_rf(test_mode=True, reusable_form_id="fa5c8a0b0f492d768749333ad6fcc214c111e967", title="NDA with Acme Co.", subject="The NDA we talked about", message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.", signing_redirect_url=None, signers=signers, ccs=ccs, custom_fields=custom_fields)
````
