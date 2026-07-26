import dataclasses
import enum
from pathlib import Path


type Ext = str


class SourceKind(enum.StrEnum):
    VIDEO = enum.auto()
    AUDIO = enum.auto()


@dataclasses.dataclass(frozen=True)
class Source:
    name: str
    ext: str
    path: Path
    kind: SourceKind


def parse_source(path: Path) -> Source:
    last_suffix = path.suffixes[-1]
    extension = last_suffix.lstrip(".")

    match extension:
        case "wav" | "aac" | "mp3":
            return Source(path.name, extension, path, SourceKind.AUDIO)
        case "mp4" | "mkv" | "avi" | "webm":
            return Source(path.name, extension, path, SourceKind.VIDEO)
        case _:
            msg = f"Unsupported file extension {extension}."
            raise ValueError(msg)
