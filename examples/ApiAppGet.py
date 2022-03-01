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
    api = apis.ApiAppApi(api_client)

    client_id = "0dd3b823a682527788c4e40cb7b6f7e9"

    try:
        response = api.api_app_get(client_id)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
