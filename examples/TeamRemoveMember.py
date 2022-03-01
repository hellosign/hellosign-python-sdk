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
    api = apis.TeamApi(api_client)

    data = models.TeamRemoveMemberRequest(
        email_address="teammate@hellosign.com",
        new_owner_email_address="new_teammate@hellosign.com",
    )

    try:
        response = api.team_remove_member(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
