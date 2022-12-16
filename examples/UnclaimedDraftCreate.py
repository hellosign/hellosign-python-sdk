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
    api = apis.UnclaimedDraftApi(api_client)

    signer_1 = models.SubUnclaimedDraftSigner(
        email_address="jack@example.com",
        name="Jack",
        order=0,
    )

    signer_2 = models.SubUnclaimedDraftSigner(
        email_address="jill@example.com",
        name="Jill",
        order=1,
    )

    signing_options = models.SubSigningOptions(
        draw=True,
        type=True,
        upload=True,
        phone=False,
        default_type="draw",
    )

    field_options = models.SubFieldOptions(
        date_format="DD - MM - YYYY",
    )

    data = models.UnclaimedDraftCreateRequest(
        subject="The NDA we talked about",
        type="request_signature",
        message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
        signers=[signer_1, signer_2],
        cc_email_addresses=[
            "lawyer@hellosign.com",
            "lawyer@example.com",
        ],
        file=[open("example_signature_request.pdf", "rb")],
        metadata={
            "custom_id": 1234,
            "custom_text": "NDA #9",
        },
        signing_options=signing_options,
        field_options=field_options,
        test_mode=True,
    )

    try:
        response = api.unclaimed_draft_create(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
