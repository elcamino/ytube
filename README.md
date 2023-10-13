# Youtube video transcription using the Whisper API

## Installation

```shell
python -m venv venv
. ./venv/bin/activate
pip3 install openai flask pytube
```

## Running it

```shell
. ./venv/bin/activate
env OPENAI_API_KEY=your-api-key-goes-here ./ui.py
```

## Use it

open http://localhost:5000 in your browser. Enter the URL to the Youtube video you'd like to transcribe and hit "Transcribe".

Wait for a minute until the transcript is ready.
