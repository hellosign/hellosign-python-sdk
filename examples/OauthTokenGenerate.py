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

    data = models.OAuthTokenGenerateRequest(
        state="900e06e2",
        code="1b0d28d90c86c141",
        client_id="cc91c61d00f8bb2ece1428035716b",
        client_secret="1d14434088507ffa390e6f5528465",
    )

    try:
        response = api.oauth_token_generate(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
