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

    signer_1 = models.SubSignatureRequestEmbeddedTemplateSigner(
        role="Client",
        email_address="jack@example.com",
        name="Jack",
    )

    signing_options = models.SubSigningOptions(
        draw=True,
        type=True,
        upload=True,
        phone=True,
        default_type="draw",
    )

    data = models.SignatureRequestCreateEmbeddedWithTemplateRequest(
        client_id="ec64a202072370a737edf4a0eb7f4437",
        template_ids=["c26b8a16784a872da37ea946b9ddec7c1e11dff6"],
        subject="Purchase Order",
        message="Glad we could come to an agreement.",
        signers=[signer_1],
        signing_options=signing_options,
        test_mode=True,
    )

    try:
        response = api.signature_request_create_embedded_with_template(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
