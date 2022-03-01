from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis, models

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.SignatureRequestApi(api_client)
    
    data = models.SignatureRequestUpdateRequest(
        email_address = "john@example.com",
        signature_id = "78caf2a1d01cd39cea2bc1cbb340dac3",
    )
    
    signature_request_id = "2f9781e1a8e2045224d808c153c2e1d3df6f8f2f"

    try:
        response = api.signature_request_update(signature_request_id, data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
