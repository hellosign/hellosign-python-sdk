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
    api = apis.ApiAppApi(api_client)

    oauth = models.SubOAuth(
        callback_url="https://example.com/oauth",
        scopes=["basic_account_info" "request_signature"],
    )

    white_labeling_options = models.SubWhiteLabelingOptions(
        primary_button_color="#00b3e6",
        primary_button_text_color="#ffffff",
    )

    custom_logo_file = open('./CustomLogoFile.png', 'rb')

    data = models.ApiAppCreateRequest(
        name="My Production App",
        domains=["example.com"],
        oauth=oauth,
        white_labeling_options=white_labeling_options,
        custom_logo_file=custom_logo_file,
    )

    try:
        response = api.api_app_create(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
