from typing import Dict

from .commits import BaseCommit


class Authorizer(Dict[str, str]):
    """
    Essentially a database of users' public keys. Can verify that given
    commit was indeed authored and signed by the user that it references.

    It is recommended to use a public blockchain as a backend for Authorizer.
    """
    def verify(self, commit: BaseCommit) -> bool:
        if commit.user_id not in self:
            return False

        return False
