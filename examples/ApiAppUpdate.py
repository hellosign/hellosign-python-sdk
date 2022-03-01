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

    white_labeling_options = models.SubWhiteLabelingOptions(
        primary_button_color="#00b3e6",
        primary_button_text_color="#ffffff",
    )

    custom_logo_file = open('./CustomLogoFile.png', 'rb')

    data = models.ApiAppUpdateRequest(
        name="New Name",
        callback_url="http://example.com/hellosign",
        white_labeling_options=white_labeling_options,
        custom_logo_file=custom_logo_file,
    )

    client_id = "0dd3b823a682527788c4e40cb7b6f7e9"

    try:
        response = api.api_app_update(client_id, data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
