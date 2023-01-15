from datetime import datetime
from typing import Dict, Optional

from .errors import *

errors: Dict[str, SlackExceptions] = {
    "invalid_auth": TokenTypeException("Some aspect of authentication cannot be validated."),
    "missing_args": ClientException("An app-level token wasn't provided."),
    "missing_scope": "",
    "internal_error": SlackException("The server could not complete your operation(s) without encountering an error"),
    "forbidden_team": ForbiddenException("The authenticated team cannot use."),
    "not_authed": TokenTypeException("No authentication token provided."),
    "account_inactive": TokenTypeException("Authentication token is for a deleted user or workspace when using a bot "
                                           "token."),
    "token_revoked": ClientException("Authentication token is for a deleted user or workspace or the app has been "
                                     "removed when using a user token."),
    "invalid_blocks": InvalidArgumentException("Blocks submitted with this message are not valid"),
    "invalid_blocks_format": InvalidArgumentException("The blocks is not a valid JSON object or doesn't match the "
                                                      "Block Kit syntax.")
}


def ts2time(time: Union[str, int, float, None]) -> Optional[datetime]:
    if time is None:
        return None
    return datetime.fromtimestamp(float(time))


def parse_exception(event_name: str, **kwargs):
    if event_name == "missing_scope":
        needed = kwargs.get("needed", "").split(",")
        provided = kwargs.get("provided", "").split(",")
        raise ClientException("missing_scope: {}, provided: {}".format(", ".join(needed), ", ".join(provided)))
    exc = errors.get(event_name)
    if exc is None:
        exc = SlackException(event_name)

    raise exc
