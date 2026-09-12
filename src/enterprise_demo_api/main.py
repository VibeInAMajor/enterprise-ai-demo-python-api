"""HTTP entry point for the enterprise AI demo API."""

from fastapi import FastAPI

app = FastAPI(title="Enterprise AI Demo API")


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the service is available."""
    return {"status": "ok"}


@app.get("/delivery-status")
def delivery_status() -> dict[str, str]:
    """Expose the review handoff state for the demo."""
    return {"status": "human-review-required"}


@app.get("/ready")
def ready() -> dict[str, bool]:
    """Report readiness status."""
    return {"ready": True}
