# Enterprise AI Demo Python API

Minimal FastAPI baseline used by the enterprise AI development pipeline for
repository-backed candidate generation. It exposes a health endpoint and a
matching test so later pipeline stages have an immutable, inspectable Python
repository base.

## Local setup

```bash
python -m venv .venv
.venv/bin/pip install -e ".[test]"
.venv/bin/pytest
```
