"""HTTP entry point for the enterprise AI demo API."""

from fastapi import FastAPI

app = FastAPI(title="Enterprise AI Demo API")


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the service is available."""
    return {"status": "ok"}
