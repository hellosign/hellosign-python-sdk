from hellosign_sdk.models import EventCallbackRequest, EventCallbackRequestEventMetadata
import hmac
import hashlib


class EventCallbackHelper:
    EVENT_TYPE_ACCOUNT_CALLBACK = 'account_callback'

    EVENT_TYPE_APP_CALLBACK = 'app_callback'

    @classmethod
    def is_valid(cls, api_key, event_callback: EventCallbackRequest):  # noqa: E501
        """Verify that a callback came from HelloSign.com

        Args:
            api_key (string):
            event_callback (EventCallbackRequest):
        """
        hashed = hmac.new(
            bytes(api_key, 'utf-8'),
            bytes(f'{event_callback.event.event_time}{event_callback.event.event_type}', 'utf-8'),
            hashlib.sha256
        ).hexdigest()

        return event_callback.event.event_hash == hashed

    @classmethod
    def get_callback_type(cls, event_callback: EventCallbackRequest):
        """Identifies the callback type, one of "account_callback" or "app_callback".
        "app_callback" will always include a value for "reported_for_app_id"

        Args:
            event_callback (EventCallbackRequest):
        """
        metadata: EventCallbackRequestEventMetadata = event_callback.event.event_metadata

        if not metadata.reported_for_app_id:
            return cls.EVENT_TYPE_ACCOUNT_CALLBACK

        return cls.EVENT_TYPE_APP_CALLBACK
