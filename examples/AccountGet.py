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
    api = apis.AccountApi(api_client)

    try:
        response = api.account_get(email_address="jack@example.com")
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
