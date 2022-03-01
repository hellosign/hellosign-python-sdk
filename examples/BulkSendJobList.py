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
    api = apis.BulkSendJobApi(api_client)

    page = 1
    page_size = 20

    try:
        response = api.bulk_send_job_list(
            page=page,
            page_size=page_size,
        )
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
