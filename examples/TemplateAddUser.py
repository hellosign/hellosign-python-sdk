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
    api = apis.TemplateApi(api_client)

    data = models.TemplateAddUserRequest(
        email_address="george@hellosign.com",
    )

    template_id = "f57db65d3f933b5316d398057a36176831451a35"

    try:
        response = api.template_add_user(template_id, data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
