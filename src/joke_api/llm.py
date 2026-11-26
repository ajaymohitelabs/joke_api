"""Groq LLM client wrapper for generating jokes."""

import logging

from groq import Groq

from joke_api.config import get_settings

logger = logging.getLogger(__name__)


class JokeGenerationError(Exception):
    """Raised when the LLM fails to return a usable joke."""


def generate_joke(topic: str) -> str:
    settings = get_settings()
    if not settings.groq_api_key:
        raise JokeGenerationError("Missing GROQ_API_KEY in environment")

    client = Groq(api_key=settings.groq_api_key)
    completion = client.chat.completions.create(
        model=settings.groq_model,
        messages=[
            {"role": "system", "content": "You are a concise joke writer."},
            {"role": "user", "content": f"Write one short, funny joke about {topic}."},
        ],
        temperature=0.8,
        max_tokens=300,
    )
    logger.debug("Groq completion: %s", completion)

    if not completion.choices:
        raise JokeGenerationError("LLM returned no choices")

    content = completion.choices[0].message.content
    if not content or not content.strip():
        raise JokeGenerationError("LLM returned empty content")

    return content.strip()
