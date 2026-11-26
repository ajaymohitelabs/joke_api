from fastapi.testclient import TestClient

from joke_api import main
from joke_api.llm import JokeGenerationError

client = TestClient(main.app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_joke_success(monkeypatch):
    monkeypatch.setattr(main, "generate_joke", lambda topic: f"a joke about {topic}")
    resp = client.get("/joke", params={"topic": "cats"})
    assert resp.status_code == 200
    assert resp.json() == {"topic": "cats", "joke": "a joke about cats"}


def test_joke_llm_error(monkeypatch):
    def boom(topic):
        raise JokeGenerationError("nope")

    monkeypatch.setattr(main, "generate_joke", boom)
    resp = client.get("/joke", params={"topic": "cats"})
    assert resp.status_code == 502


def test_joke_requires_topic():
    assert client.get("/joke").status_code == 422
