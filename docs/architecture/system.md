# System Architecture

## Purpose

This repository is the minimal FastAPI target used to verify governed repository-backed
engineering. Changes should remain small, explicit, and easy to validate.

## Current Structure

- `src/enterprise_demo_api/main.py` owns the FastAPI application and its HTTP endpoints.
- `tests/` owns externally observable endpoint tests through `TestClient`.
- `.enterprise-ai/validation.json` and the protected GitHub workflows own validation and release
  checks; application changes do not redefine those controls.

The current application has no database, external service, background worker, or provider SDK.
Do not introduce a new layer, dependency, network integration, or persistence boundary unless an
approved requirement needs it and the change includes corresponding architecture and test proof.

## Change Rules

- Preserve existing endpoint behavior unless the approved requirement explicitly changes it.
- Keep HTTP responses typed, deterministic, and represented by stable JSON objects.
- Place runtime code under `src/` and matching automated coverage under `tests/`.
- Prefer a small endpoint function over ceremonial services, repositories, factories, or managers
  when no meaningful dependency boundary exists.
- Keep validation, security, workflow, dependency, and repository-protection decisions outside
  ordinary endpoint implementation authority.

Pull requests must pass the repository's current automated checks and remain subject to human
review. Passing application tests alone does not authorize merge or deployment.
