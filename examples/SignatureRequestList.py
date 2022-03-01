from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.SignatureRequestApi(api_client)

    account_id = None
    page = 1

    try:
        response = api.signature_request_list(
            account_id=account_id,
            page=page,
        )
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
