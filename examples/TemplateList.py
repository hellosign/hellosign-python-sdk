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
    api = apis.TemplateApi(api_client)

    account_id = "f57db65d3f933b5316d398057a36176831451a35"

    try:
        response = api.template_list(
            account_id=account_id,
        )
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
