import dataclasses
import json
from typing import Optional


@dataclasses.dataclass(frozen=True)
class BaseCommit:
    # Who is committing?
    user_id: str

    # Hash of this commit
    id: str

    previous_commit_id: Optional[str]

    timestamp: int

    def signed_data(self) -> str:
        data = dataclasses.asdict(self)
        del data['id']
        return json.dumps(data)


@dataclasses.dataclass(frozen=True)
class CreateVertexCommit(BaseCommit):
    name: str


@dataclasses.dataclass(frozen=True)
class CreateEdgeCommit(BaseCommit):
    name: str
    start_id: str
    end_id: str


@dataclasses.dataclass(frozen=True)
class RemoveVertexCommit(BaseCommit):
    vertex_id: str


@dataclasses.dataclass(frozen=True)
class RemoveEdgeCommit(BaseCommit):
    edge_id: str


@dataclasses.dataclass(frozen=True)
class RenameVertexCommit(BaseCommit):
    vertex_id: str
    name: str


@dataclasses.dataclass(frozen=True)
class RenameEdgeCommit(BaseCommit):
    edge_id: str
    name: str


@dataclasses.dataclass(frozen=True)
class MergeCommit(BaseCommit):
    """Merge two branches of Commit Log and create one coherent head."""
    merged_commit_id: str
