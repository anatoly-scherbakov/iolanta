import base64
from typing import Tuple

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import _RSAobj

LENGTH = 1024


def generate_random_keys() -> Tuple[_RSAobj, _RSAobj]:
    private_key = RSA.generate(LENGTH, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key


def sign(private_key: _RSAobj, data: str) -> str:
    return base64.b64encode(str(
        (private_key.sign(data.encode('utf-8'), ''))[0]
    ).encode())


def verify(public_key, data: str, signature: str) -> bool:
    return public_key.verify(data, (int(base64.b64decode(signature)),))
