from fastapi.testclient import TestClient

from enterprise_demo_api.main import app


def test_health_reports_ok() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_delivery_status_requires_human_review() -> None:
    response = TestClient(app).get("/delivery-status")

    assert response.status_code == 200
    assert response.json() == {"status": "human-review-required"}
