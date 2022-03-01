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

    data = models.TemplateRemoveUserRequest(
        email_address="george@hellosign.com",
    )

    template_id = "21f920ec2b7f4b6bb64d3ed79f26303843046536"

    try:
        response = api.template_remove_user(template_id, data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
