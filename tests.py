from pathlib import Path

import pytest

from source import Source, SourceKind


@pytest.mark.parametrize("filename", ("audio.wav", "audio.aac", "audio.mp3"))
def test_audio_ext_returns_audio_kind(filename: str) -> None:
    source = Source.from_path(Path(filename))

    assert source.kind == SourceKind.AUDIO


@pytest.mark.parametrize("filename", ("video.mp4", "video.mkv", "video.avi", "video.webm"))
def test_video_ext_returns_video_kind(filename: str) -> None:
    source = Source.from_path(Path(filename))

    assert source.kind == SourceKind.VIDEO


def test_unsupported_ext_raises() -> None:
    with pytest.raises(ValueError, match=r"Unsupported file extension txt."):
        Source.from_path(Path("document.txt"))


def test_no_ext_raises() -> None:
    with pytest.raises(ValueError, match=r"Path doesn't contain any suffixes."):
        Source.from_path(Path("no_extension"))


def test_saves_original_path() -> None:
    path = Path("path/to/file.mp4")

    source = Source.from_path(path)

    assert source.path == path


def test_uses_last_suffix_if_multiple_suffixes() -> None:
    source = Source.from_path(Path("video.backup.mp4"))

    assert source.kind == SourceKind.VIDEO


def test_multiple_suffixes_if_last_unsupported_raises() -> None:
    with pytest.raises(ValueError, match="Unsupported file extension bak"):
        Source.from_path(Path("video.mp4.bak"))


def test_ext_match_is_case_insensitive() -> None:
    source = Source.from_path(Path("video.MP4"))

    assert source.kind == SourceKind.VIDEO
