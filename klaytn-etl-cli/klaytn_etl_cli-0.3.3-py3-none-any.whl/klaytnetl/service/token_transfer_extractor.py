# MIT License
#
# Copyright (c) 2019 Jettson Lim, jettson.lim@groundx.xyz
# Modifications Copyright (c) klaytn authors
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import logging
from builtins import map

from klaytnetl.mixin.enrichable_mixin import EnrichableMixin
from klaytnetl.domain.token_transfer import KlaytnRawTokenTransfer, KlaytnTokenTransfer
from klaytnetl.domain.receipt_log import KlaytnRawReceiptLog, KlaytnReceiptLog
from klaytnetl.utils import chunk_string, hex_to_dec, to_normalized_address

from typing import Union

# https://ethereum.stackexchange.com/questions/12553/understanding-logs-and-log-blooms
TRANSFER_EVENT_TOPIC = (
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
)
logger = logging.getLogger(__name__)


class KlaytnTokenTransferExtractor(EnrichableMixin):
    def __init__(self, enrich=False):
        super(KlaytnTokenTransferExtractor, self).__init__(enrich=enrich)

    def extract_transfer_from_log(
        self, receipt_log: Union[KlaytnRawReceiptLog, KlaytnReceiptLog]
    ) -> Union[KlaytnRawTokenTransfer, KlaytnTokenTransfer, None]:
        # Validate topic list
        topics = receipt_log.topics
        if topics is None or len(topics) < 1:
            logger.warning(
                "Topic list is empty in log {} of transaction {}".format(
                    receipt_log.log_index, receipt_log.transaction_hash
                )
            )
            return None

        # Filter only Transfer event
        if topics[0] != TRANSFER_EVENT_TOPIC:
            return None

        # Handle unindexed event fields
        topics_with_data = topics + split_to_words(receipt_log.data)
        # if the number of topics and fields in data part != 4, then it's a weird event
        if len(topics_with_data) != 4:
            logger.warning(
                "The number of topics and data parts is not equal to 4 in log {} of transaction {}".format(
                    receipt_log.log_index, receipt_log.transaction_hash
                )
            )
            return None

        if self.enrich and not isinstance(receipt_log, KlaytnReceiptLog):
            logger.warning(
                "Cannot extract enrich token transfer from raw receipt log. "
                "It will return raw token transfer."
            )

        token_transfer = KlaytnRawTokenTransfer()
        token_transfer.token_address = to_normalized_address(receipt_log.address)
        token_transfer.from_address = word_to_address(topics_with_data[1])
        token_transfer.to_address = word_to_address(topics_with_data[2])
        token_transfer.value = hex_to_dec(topics_with_data[3])
        token_transfer.log_index = receipt_log.log_index
        token_transfer.transaction_hash = receipt_log.transaction_hash
        token_transfer.transaction_index = receipt_log.transaction_index
        token_transfer.block_number = receipt_log.block_number
        token_transfer.block_hash = receipt_log.block_hash

        return (
            token_transfer
            if not self.enrich or not isinstance(receipt_log, KlaytnReceiptLog)
            else KlaytnTokenTransfer.enrich(
                raw_token_transfers=token_transfer,
                block_timestamp=receipt_log.block_timestamp,
                transaction_receipt_status=receipt_log.transaction_receipt_status,
            )
        )


def split_to_words(data):
    if data and len(data) > 2:
        data_without_0x = data[2:]
        words = list(chunk_string(data_without_0x, 64))
        words_with_0x = list(map(lambda word: "0x" + word, words))
        return words_with_0x
    return []


def word_to_address(param):
    if param is None:
        return None
    elif len(param) >= 40:
        return to_normalized_address("0x" + param[-40:])
    else:
        return to_normalized_address(param)
