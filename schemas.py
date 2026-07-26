from pydantic import BaseModel, field_validator


class Segment(BaseModel):
    id: int
    text: str
    start: float
    end: float

    @field_validator("start", "end")
    @classmethod
    def round_start_and_end(cls, value: float) -> float:
        return round(value, 2)


class WhisperTranscript(BaseModel):
    text: str
    segments: list[Segment]
    language: str
