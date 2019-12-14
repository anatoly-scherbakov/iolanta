import json

import iolanta.commits
from iolanta import models


def test_create_vertex():
    assert iolanta.commits.CreateVertexCommit(
        id=...,
        name='John T. Kirk',
        previous_commit_id=None,
        timestamp=0,
        user_id='Alice'
    ).signed_data() == json.dumps({
        'user_id': 'Alice',
        'previous_commit_id': None,
        'timestamp': 0,
        'name': 'John T. Kirk'
    })


def test_create_edge():
    assert iolanta.commits.CreateEdgeCommit(
        id=...,
        name='John T. Kirk',
        previous_commit_id=None,
        timestamp=0,
        user_id='Alice',
        start_id='abc',
        end_id='xyz'
    ).signed_data() == json.dumps({
        'user_id': 'Alice',
        'previous_commit_id': None,
        'timestamp': 0,
        'name': 'John T. Kirk',
        'start_id': 'abc',
        'end_id': 'xyz',
    })


def test_remove_vertex():
    assert iolanta.commits.RemoveVertexCommit(
        id=...,
        previous_commit_id='123',
        timestamp=0,
        user_id='Alice',
        vertex_id='abc',
    ).signed_data() == json.dumps({
        'user_id': 'Alice',
        'previous_commit_id': '123',
        'timestamp': 0,
        'vertex_id': 'abc',
    })


def test_remove_edge():
    assert iolanta.commits.RemoveEdgeCommit(
        id=...,
        previous_commit_id='123',
        timestamp=0,
        user_id='Alice',
        edge_id='abc',
    ).signed_data() == json.dumps({
        'user_id': 'Alice',
        'previous_commit_id': '123',
        'timestamp': 0,
        'edge_id': 'abc',
    })


def test_merge():
    assert iolanta.commits.MergeCommit(
        id=...,
        previous_commit_id='123',
        timestamp=0,
        user_id='Alice',
        merged_commit_id='abc'
    ).signed_data() == json.dumps({
        'user_id': 'Alice',
        'previous_commit_id': '123',
        'timestamp': 0,
        'merged_commit_id': 'abc',
    })
