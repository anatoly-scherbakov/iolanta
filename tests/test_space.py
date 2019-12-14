import pytest

from iolanta.models import Space, MissingVertex, MissingEdge


def test_create_vertex_id():
    assert Space().add_vertex('Kitty').id is not None


def test_create_vertex_name():
    assert Space().add_vertex('Kitty').name == 'Kitty'


def test_create_edge():
    trek = Space()
    captain = trek.add_vertex('Captain')
    kirk = trek.add_vertex('James Kirk')

    rank = trek.add_edge(kirk, captain, 'has_rank')

    assert rank.start == kirk
    assert rank.end == captain
    assert rank.name == 'has_rank'
    assert rank.id is not None


def test_find_vertex_by_id():
    trek = Space()
    kirk = trek.add_vertex(name='James T. Kirk')
    assert trek.vertex_by_id(kirk.id) == kirk


def test_find_edge_by_id():
    trek = Space()
    kirk = trek.add_vertex(name='James T. Kirk')
    captain = trek.add_vertex('Captain')
    rank = trek.add_edge(kirk, captain, 'has_rank')
    assert trek.edge_by_id(rank.id) == rank


def test_missing_vertex():
    with pytest.raises(MissingVertex):
        Space().vertex_by_id('abc')


def test_missing_edge():
    with pytest.raises(MissingEdge):
        Space().edge_by_id('abc')


def test_adjacent_edges():
    trek = Space()
    captain = trek.add_vertex('Captain')

    kirk = trek.add_vertex(name='James T. Kirk')
    pike = trek.add_vertex(name='Christopher Pike')

    edges = set()
    for person in [kirk, pike]:
        edges.add(trek.add_edge(person, captain, 'has_rank'))

    assert trek.adjacent_edges(captain) == edges


def test_remove_edge():
    trek = Space()
    captain = trek.add_vertex('Captain')
    kirk = trek.add_vertex(name='James T. Kirk')
    rank = trek.add_edge(kirk, captain, 'has_rank')

    trek.remove_edge(rank.id)

    with pytest.raises(MissingEdge):
        trek.edge_by_id(rank.id)


def test_remove_vertex():
    trek = Space()
    captain = trek.add_vertex('Captain')

    kirk = trek.add_vertex(name='James T. Kirk')
    pike = trek.add_vertex(name='Christopher Pike')

    edges = []
    for person in [kirk, pike]:
        edges.append(trek.add_edge(person, captain, 'has_rank'))

    trek.remove_vertex(captain.id)

    for edge in edges:
        with pytest.raises(MissingEdge):
            trek.edge_by_id(edge.id)

    assert trek.vertex_by_id(kirk.id) == kirk
    assert trek.vertex_by_id(pike.id) == pike
