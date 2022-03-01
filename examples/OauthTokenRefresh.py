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
    api = apis.OAuthApi(api_client)

    data = models.OAuthTokenRefreshRequest(
        refresh_token="hNTI2MTFmM2VmZDQxZTZjOWRmZmFjZmVmMGMyNGFjMzI2MGI5YzgzNmE3",
    )

    try:
        response = api.oauth_token_refresh(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
