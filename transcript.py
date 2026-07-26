import dataclasses
from pathlib import Path


@dataclasses.dataclass(frozen=True)
class Segment:
    id: int
    text: str
    start: float
    end: float


@dataclasses.dataclass(frozen=True)
class Transcript:
    file: Path
    text: str
    segments: list[Segment]
    language: str
