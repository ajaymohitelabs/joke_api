"""Entry point: `uv run joke-api` or `python -m joke_api`."""

import uvicorn

from joke_api.config import get_settings


def main() -> None:
    settings = get_settings()
    uvicorn.run("joke_api.main:app", host=settings.host, port=settings.port)


if __name__ == "__main__":
    main()
