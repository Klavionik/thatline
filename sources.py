import dataclasses
import enum
from pathlib import Path
from typing import Self


class SourceKind(enum.StrEnum):
    VIDEO = enum.auto()
    AUDIO = enum.auto()


@dataclasses.dataclass(frozen=True)
class Source:
    path: Path
    kind: SourceKind

    @classmethod
    def from_path(cls, path: Path) -> Self:
        last_suffix = path.suffixes[-1]
        extension = last_suffix.lstrip(".")

        match extension:
            case "wav" | "aac" | "mp3":
                return cls(path, SourceKind.AUDIO)
            case "mp4" | "mkv" | "avi" | "webm":
                return cls(path, SourceKind.VIDEO)
            case _:
                msg = f"Unsupported file extension {extension}."
                raise ValueError(msg)
