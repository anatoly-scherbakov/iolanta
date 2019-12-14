import base64
import binascii
import logging
from typing import Dict

from Crypto.PublicKey import RSA

from iolanta.commits import BaseCommit


logger = logging.getLogger(__name__)


class Authorizer(Dict[str, str]):
    """
    Essentially a database of users' public keys. Can verify that given
    commit was indeed authored and signed by the user that it references.

    It is recommended to use a public blockchain as a backend for Authorizer.
    """
    def verify(self, commit: BaseCommit) -> bool:
        if commit.user_id not in self:
            return False

        try:
            decoded_id = base64.b64decode(commit.id)
        except binascii.Error as err:
            logger.exception(err)
            return False

        public_key = RSA.importKey(self[commit.user_id])

        data = commit.signed_data().encode('utf-8')

        return public_key.verify(data, (int(decoded_id),))
