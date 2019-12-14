import time

from iolanta.commits import CreateVertexCommit
from iolanta.authorizer import Authorizer


PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQCmdMzxYt7jx/wfmK6Q1zyEiyszyK/81bdhk7TS/0twIB75jaxz
mFsXt74pIo5xtDCzn2lUPj4QSk0br9tQI47DBliUEZzpMhrYbzdPBYqxQyeDH47n
XtWkj2BEiTBlx8Feb44XCpk6GsvW6OGiCb+772cBsqdba3My2k+5+ZO25QIDAQAB
AoGAZ6HcXoRxxFqjy4AhXqfCU7rZYNoXR1A/ZY6yS5MKAnrdDf14WleGjxOkXrPW
/09x6sLarso5labMruojnpckr5+0VDhR8DnyIb1NfBcRHeIstgBMbS2uNFPREUqq
PmH0a7Ar815dt7EDNTAELXZycE/TCbm1DeEFuY46eq/9rkECQQC1TMAddMxhXA8g
Z5yiLbjx8SyZxb4iEP12Q0b+B8naJ4FlVQ6xXvDTGV4MdI2QRHezFCtIvYt/oGQG
MS/ZFxRtAkEA6wpfcA8DJ5csSxBwF2mjTmXOt6m7CV+wLtnTCzfPqfj+wPervUTw
ghESwnE8nOs3+WT8QUoMaqPfjk/zDb/xWQJAYjFCb/G9bBG3I57aZ8AJxggQVuyR
kNPQ40eG4LkJKz1wSJirz4cTOdIobOiHb5aVmgkXdFssfaA57FyhhJuKdQJAGXaa
OE2oDdX22nsBacfsBUZKSuN8e9t9/tViY8i8GrH7B3TNike5tp2a5q3V3zosajxi
h8A58COoyIYo0siEoQJAOrdSBntz/p0YWsAxdNNHXwM7gbwrRNOVoMexNa7rD+fB
GOmOt0d++M+U6t906s1nccM4ACKLtYfJX0/jKb42mw==
-----END RSA PRIVATE KEY-----'''


PUBLIC_KEYS = {
    'Alice': (
'''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmdMzxYt7jx/wfmK6Q1zyEiysz
yK/81bdhk7TS/0twIB75jaxzmFsXt74pIo5xtDCzn2lUPj4QSk0br9tQI47DBliU
EZzpMhrYbzdPBYqxQyeDH47nXtWkj2BEiTBlx8Feb44XCpk6GsvW6OGiCb+772cB
sqdba3My2k+5+ZO25QIDAQAB
-----END PUBLIC KEY-----'''
    )
}


def test_verify_false():
    assert Authorizer().verify(CreateVertexCommit(
        id='abc',
        previous_commit_id=None,
        name='James T. Kirk',
        user_id='Alice',
        timestamp=int(time.time()),
    )) is False


def test_verify_user_not_in_list():
    assert Authorizer({
        'Alice': 'abc'
    }).verify(CreateVertexCommit(
        id='abc',
        previous_commit_id=None,
        name='James T. Kirk',
        user_id='Bob',
        timestamp=int(time.time()),
    )) is False


def test_verify_user_in_list_but_key_wrong():
    assert Authorizer(
        **PUBLIC_KEYS
    ).verify(CreateVertexCommit(
        id='abc',
        previous_commit_id=None,
        name='James T. Kirk',
        user_id='Alice',
        timestamp=int(time.time()),
    )) is False


def test_verify_user_in_list_and_key_correct():
    commit = CreateVertexCommit(
        id=(
            'NTE1MjA1MjUwNzQ5NDk2MjI1OTE5NTQ5NTE3MzA2ODk4MDYwNDIwOTQ1NjY0MTgyND'
            'I3MzE1Njk4MTE0OTE1MDAzNTM2MzIxNjg4NjkxNTgzNDQ0OTEwNTg2MTE5MjcxODUy'
            'OTkxMTE0NjYwNTM4OTI2NDE4MjUzNzU1OTYzNjY5NTQ2MDgxMzMxMTI0NDM5ODA2OT'
            'g5MDc2NDUwNDI1OTA5OTY2MjM0NTQ3NDQyOTM5MjAyNTMxMjAxOTA2NDEwNjk2MzMz'
            'NTEwMzkxMzUyOTI1MDYyNzExOTgwMzM1MjU0OTAwMTExOTczOTQ2NjI1ODEwNTc4OT'
            'c0MzYyMzUxMTA4MTg5MTE3NjMwNzczNTEyMjM1OTU4MDU5Nzk4MzcwMjgwMDYxMDk0'
            'OTY1OTk1MjQxNTA='
        ),
        previous_commit_id=None,
        name='James T. Kirk',
        user_id='Alice',
        timestamp=1576350570,
    )

    assert Authorizer(**PUBLIC_KEYS).verify(commit) is True
