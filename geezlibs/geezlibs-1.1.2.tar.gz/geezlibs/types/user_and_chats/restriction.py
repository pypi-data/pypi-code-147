#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from geezlibs import raw
from ..object import Object


class Restriction(Object):
    """A restriction applied to bots or chats.

    Parameters:
        platform (``str``):
            The platform the restriction is applied to, e.g. "ios", "android"

        reason (``str``):
            The restriction reason, e.g. "porn", "copyright".

        text (``str``):
            The restriction text.
    """

    def __init__(self, *, platform: str, reason: str, text: str):
        super().__init__(None)

        self.platform = platform
        self.reason = reason
        self.text = text

    @staticmethod
    def _parse(restriction: "raw.types.RestrictionReason") -> "Restriction":
        return Restriction(
            platform=restriction.platform,
            reason=restriction.reason,
            text=restriction.text
        )
