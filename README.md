# HealthWatch Application

Starter application for the Day 2 DevOps portfolio project.

## Application

HealthWatch is a small Flask application exposing:

- `/` - application information
- `/health` - health endpoint
- `/version` - running application version

## Environment Variables

| Variable | Default | Purpose |
|---|---|---|
| `APP_NAME` | `HealthWatch` | Application name |
| `APP_VERSION` | `1.0.0` | Application version |
| `SIMULATE_FAILURE` | `false` | Simulates an unhealthy application |
| `SIMULATE_DELAY` | `0` | Adds response delay in seconds |

## Run locally

```bash
python -m venv venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

The application runs on port 5000.

## Test

```bash
pytest
```

## Docker

Build and run the application using Docker.

The DevOps pipeline, monitoring system, AI integration, deployment configuration,
rollback mechanism, and infrastructure are intentionally NOT included.

Those are part of the Day 2 challenge.
