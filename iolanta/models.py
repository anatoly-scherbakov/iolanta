import dataclasses
from enum import Enum
from typing import Optional, Union, List

from uuid import uuid4


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
class Graph:
    name: str

    vertexes: List[Vertex] = dataclasses.field(default_factory=list)
    edges: List[Edge] = dataclasses.field(default_factory=list)
    commit_log: List[Commit] = dataclasses.field(default_factory=list)

    id: str = dataclasses.field(default_factory=uuid)

    def vertex_by_id(self, vertex_id: str):
        v, = [v for v in self.vertexes if v.id == vertex_id]
        return v

    def edge_by_id(self, edge_id: str):
        e, = [e for e in self.edges if e.id == edge_id]
        return e

    def adjacent_edges(self, vertex: Vertex):
        return [
            edge for edge in self.edges
            if (
                edge.start == vertex
                or edge.end == vertex
            )
        ]

    def add_vertex(self, name: str):
        self.vertexes.append(Vertex(name=name))

    def add_edge(self, name: str, start: Vertex, end: Vertex):
        assert start in self.vertexes
        assert end in self.vertexes
        self.edges.append(Edge(
            start=start,
            end=end,
            name=name
        ))

    def remove_edge(self, edge_id: str):
        edge, = filter(lambda e: e.id == edge_id, self.edges)
        self.edges.remove(edge)

    def remove_vertex(self, vertex_id: str):
        vertex = self.vertex_by_id(vertex_id)

        adjacent_edges = self.adjacent_edges(vertex)
        for edge in adjacent_edges:
            # FIXME we could provide the edge object itself
            self.remove_edge(edge.id)

        self.vertexes.remove(vertex)
