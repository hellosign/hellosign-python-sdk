from hellosign_sdk.models import EventCallbackRequestEvent
import hmac
import hashlib


class EventCallbackHelper:
    @classmethod
    def is_valid(cls, api_key, event):  # noqa: E501
        """Verify that a callback came from HelloSign.com

        Args:
            api_key (string):
            event (EventCallbackRequestEvent):
        """
        hashed = hmac.new(
            bytes(api_key, 'utf-8'),
            bytes(f'{event.event_time}{event.event_type}', 'utf-8'),
            hashlib.sha256
        ).hexdigest()

        return event.event_hash == hashed
