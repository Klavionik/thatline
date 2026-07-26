import os
import tempfile
from pathlib import Path


from schemas import WhisperTranscript
from sources import Source, SourceKind
from transcript import Transcript


def transcribe_source(source: Source) -> Transcript:
    match source.kind:
        case SourceKind.AUDIO:
            return _transcribe_audio(source.path)
        case SourceKind.VIDEO:
            return _transcribe_video(source.path)


def _transcribe_audio(audio: os.PathLike[str] | str) -> Transcript:
    import whisper

    path = Path(audio)
    model = whisper.load_model("small")
    whisper_result = whisper.transcribe(model, str(path))
    whisper_transcript = WhisperTranscript.model_validate(whisper_result)
    return Transcript(
        path, whisper_transcript.text, whisper_transcript.segments, whisper_transcript.language
    )


def _transcribe_video(video: os.PathLike[str] | str) -> Transcript:
    import ffmpeg

    path = Path(video)

    with tempfile.NamedTemporaryFile(mode="wb", suffix=".mp3") as temp_audio:
        cmd = ffmpeg.input(path).output(filename=temp_audio.name, vn=True, acodec="mp3")
        cmd.run()

        return _transcribe_audio(temp_audio.name)
