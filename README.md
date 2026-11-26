# joke_api

A FastAPI service that generates a short joke on any topic using the [Groq](https://groq.com) LLM API.

## Project structure

```
joke_api/
├── src/joke_api/
│   ├── __init__.py     # package version
│   ├── __main__.py     # entry point (starts uvicorn)
│   ├── config.py       # settings loaded from .env
│   ├── llm.py          # Groq client wrapper
│   └── main.py         # FastAPI app and routes
├── tests/
│   └── test_api.py
├── .env.sample
├── pyproject.toml
└── README.md
```

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- A Groq API key

## Setup

```bash
uv sync
cp .env.sample .env
# edit .env and set GROQ_API_KEY
```

| Variable       | Default              | Description          |
|----------------|----------------------|----------------------|
| `GROQ_API_KEY` | (required)           | Your Groq API key    |
| `GROQ_MODEL`   | `openai/gpt-oss-20b` | Groq model to use    |
| `HOST`         | `127.0.0.1`          | Server bind address  |
| `PORT`         | `8000`               | Server port          |

## Run

```bash
uv run joke-api
```

Then open:

- http://127.0.0.1:8000/joke?topic=python
- http://127.0.0.1:8000/docs (interactive API docs)
- http://127.0.0.1:8000/health

## Test

```bash
uv run pytest
```

## Build

```bash
uv build   # creates a wheel and sdist in dist/
```

## API

### `GET /joke?topic=<topic>`

```json
{ "topic": "python", "joke": "..." }
```

Returns `422` if `topic` is missing and `502` if the LLM call fails.

### `GET /health`

```json
{ "status": "ok" }
```
