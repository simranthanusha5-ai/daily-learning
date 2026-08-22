# Day 72: Dataclasses
from dataclasses import dataclass, field

@dataclass(frozen=True)
class CommitRecord:
    hash_id: str
    message: str
    author: str
    tags: tuple[str, ...] = field(default_factory=tuple)

commit = CommitRecord("c764ac5", "Day 1", "Thanusha simran", ("git", "init"))
print("Commit record:", commit)
