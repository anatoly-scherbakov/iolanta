import dataclasses
from enum import Enum
from typing import Optional, Union, List, Set

from uuid import uuid4


class MissingVertex(Exception):
    def __init__(self, vertex_id: str):
        self.vertex_id = vertex_id

    def __str__(self):
        return f'Vertex with id {self.vertex_id} not found.'


class MissingEdge(Exception):
    def __init__(self, edge_id: str):
        self.edge_id = edge_id

    def __str__(self):
        return f'Edge with id {self.edge_id} not found.'


def uuid():
    return uuid4().hex


class Operation(str, Enum):
    CREATE = 'create'
    DELETE = 'delete'


@dataclasses.dataclass(frozen=True)
class Vertex:
    name: str
    id: str = dataclasses.field(default_factory=uuid)


@dataclasses.dataclass(frozen=True)
class Edge:
    name: str

    start: Vertex
    end: Vertex

    id: str = dataclasses.field(default_factory=uuid)


@dataclasses.dataclass(frozen=True)
class Commit:
    previous_commit: Optional['Commit']
    content: Union[Vertex, Edge]
    operation: Operation = Operation.CREATE

    id: str = dataclasses.field(default_factory=uuid)


@dataclasses.dataclass(frozen=True)
class Space:
    name: str = 'Untitled Space'

    vertexes: List[Vertex] = dataclasses.field(default_factory=list)
    edges: List[Edge] = dataclasses.field(default_factory=list)
    commit_log: List[Commit] = dataclasses.field(default_factory=list)

    id: str = dataclasses.field(default_factory=uuid)

    def vertex_by_id(self, vertex_id: str):
        try:
            v, = [v for v in self.vertexes if v.id == vertex_id]
        except ValueError as err:
            raise MissingVertex(vertex_id) from err
        else:
            return v

    def edge_by_id(self, edge_id: str):
        try:
            e, = [e for e in self.edges if e.id == edge_id]
        except ValueError as err:
            raise MissingEdge(edge_id) from err
        else:
            return e

    def adjacent_edges(self, vertex: Vertex) -> Set[Vertex]:
        return {
            edge for edge in self.edges
            if (
                edge.start == vertex
                or edge.end == vertex
            )
        }

    def add_vertex(self, name: str) -> Vertex:
        vertex = Vertex(name=name)
        self.vertexes.append(vertex)
        return vertex

    def add_edge(self, start: Vertex, end: Vertex, name: str) -> Edge:
        assert start in self.vertexes
        assert end in self.vertexes

        edge = Edge(start=start, end=end, name=name)
        self.edges.append(edge)

        return edge

    def remove_edge(self, edge_id: str):
        edge = self.edge_by_id(edge_id)
        self.edges.remove(edge)

    def remove_vertex(self, vertex_id: str):
        vertex = self.vertex_by_id(vertex_id)

        adjacent_edges = self.adjacent_edges(vertex)
        for edge in adjacent_edges:
            # FIXME we could provide the edge object itself
            self.remove_edge(edge.id)

        self.vertexes.remove(vertex)
