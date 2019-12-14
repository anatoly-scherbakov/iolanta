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