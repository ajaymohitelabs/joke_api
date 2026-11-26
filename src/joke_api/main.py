"""FastAPI application and routes."""

from fastapi import FastAPI, HTTPException, Query

from joke_api import __version__
from joke_api.llm import JokeGenerationError, generate_joke

app = FastAPI(title="Groq Joke API", version=__version__)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/joke")
def get_joke(
    topic: str = Query(..., min_length=1, description="Topic for the joke"),
) -> dict[str, str]:
    try:
        joke = generate_joke(topic)
    except JokeGenerationError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return {"topic": topic, "joke": joke}
