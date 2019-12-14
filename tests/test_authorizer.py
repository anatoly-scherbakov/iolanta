import time

from iolanta.commits import CreateVertexCommit
from iolanta.authorizer import Authorizer


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
    assert Authorizer({
        'Alice': 'abc'
    }).verify(CreateVertexCommit(
        id='abc',
        previous_commit_id=None,
        name='James T. Kirk',
        user_id='Alice',
        timestamp=int(time.time()),
    )) is False


def test_verify_user_in_list_and_key_correct():
    assert Authorizer({
        'Alice': 'abc'
    }).verify(CreateVertexCommit(
        id='abc',
        previous_commit_id=None,
        name='James T. Kirk',
        user_id='Alice',
        timestamp=int(time.time()),
    )) is False

