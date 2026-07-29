from collections.abc import Sequence

import cyclopts
from cyclopts.types import ResolvedExistingPath

from source import Source
from transcription import transcribe_source

app = cyclopts.App()


@app.command
def find(query: str, paths: Sequence[ResolvedExistingPath]) -> None:
    for path in paths:
        if path.is_dir():
            # TODO: Skip dirs processing for now.
            continue

        source = Source.from_path(path)
        transcript = transcribe_source(source)

        if query in transcript.text:
            print(f"Found {query} in {transcript.file}!")


if __name__ == "__main__":
    app()
