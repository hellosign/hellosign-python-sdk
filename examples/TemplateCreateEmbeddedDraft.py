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

    role_1 = models.SubTemplateRole(
        name="Client",
        order=0,
    )

    role_2 = models.SubTemplateRole(
        name="Witness",
        order=1,
    )

    merge_field_1 = models.SubMergeField(
        name="Full Name",
        type="text",
    )

    merge_field_2 = models.SubMergeField(
        name="Is Registered?",
        type="checkbox",
    )

    field_options = models.SubFieldOptions(
        date_format="DD - MM - YYYY",
    )

    data = models.TemplateCreateEmbeddedDraftRequest(
        client_id="37dee8d8440c66d54cfa05d92c160882",
        file=[open("example_signature_request.pdf", "rb")],
        title="Test Template",
        subject="Please sign this document",
        message="For your approval",
        signer_roles=[role_1, role_2],
        cc_roles=["Manager"],
        merge_fields=[merge_field_1, merge_field_2],
        field_options=field_options,
        test_mode=True,
    )

    try:
        response = api.template_create_embedded_draft(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
