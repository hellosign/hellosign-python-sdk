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
    api = apis.SignatureRequestApi(api_client)

    signer_1 = models.SubSignatureRequestSigner(
        role="Client",
        email_address="george@example.com",
        name="George",
    )

    cc_1 = models.SubCC(
        role="Accounting",
        email_address="accounting@example.com",
    )

    custom_field_1 = models.SubCustomField(
        name="Cost",
        value="$20,000",
        editor="Client",
        required=True,
    )

    signing_options = models.SubSigningOptions(
        draw=True,
        type=True,
        upload=True,
        phone=False,
        default_type="draw",
    )

    data = models.SignatureRequestSendWithTemplateRequest(
        template_ids=["c26b8a16784a872da37ea946b9ddec7c1e11dff6"],
        subject="Purchase Order",
        message="Glad we could come to an agreement.",
        signers=[signer_1],
        ccs=[cc_1],
        custom_fields=[custom_field_1],
        signing_options=signing_options,
        test_mode=True,
    )

    try:
        response = api.signature_request_send_with_template(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
