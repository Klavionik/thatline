import dataclasses
from pathlib import Path


@dataclasses.dataclass(frozen=True)
class Segment:
    id: int
    start: float
    end: float
    text: str


@dataclasses.dataclass(frozen=True)
class Transcript:
    file: Path
    text: str
    segments: list[Segment]
    language: str
