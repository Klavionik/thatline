# Thatline
Thatline is a tool that lets you search across your video and audio files for specific
words and sentences you vaguely remember. Anything to find that line from that series!

## Requirements
* Python 3.13

## Installation
### pipx
Run `pipx install thatline[cli]` to install the backend and the CLI tool.

## Usage
`thatline` has two modes: exact search and semantic search. The first one, as the name
implies, searches for the exact word or sentence. The second one handles cases where
you're not sure you remember the exact words, but you're pretty sure you remember the
meaning.

### Exact search in a file
```shell
thatline find "I don't need a team... I need a friend!" house.mp4
```

### Semantic search in a file
```shell
thatline find --semantic "Master Yoda, you are alive." episode3.mp4
```

### Exact search, German, in a directory
```shell
thatline find --lang de "Der Ball ist rund." /home/user/movies
```

### Semantic search, Italian, in a directory, video files only
```shell
thatline find --lang it --video-only "Miscusi, miscusi!" /home/user/
```

## How exactly does it work?
First, you specify a file or a directory of files to process, the query, and the
language of the search (or leave it for the tool to detect). The tool reads each file and
decides whether it's a video or audio file. If it's a video, it extracts the audio track
in the corresponding language and transcribes it into text. If it's an audio file, then it
just gets transcribed.

This transcript then gets processed depending on the chosen mode.

### Exact mode
In this mode, the tool searches the transcript for a substring that matches the query.
It ignores punctuation and performs case-insensitive search.

### Semantic mode
In this mode, the transcript gets vectorized and searched by the meaning of the query.
