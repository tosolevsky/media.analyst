# Media Analyst

Media Analyst is a FastAPI based service for AI‑assisted content generation and analysis. It integrates with Firebase for data storage and uses large language models to create short form text. The project exposes REST endpoints for authentication, bot responses and feedback collection.

## Setup

1. Install Python 3.11 or later.
2. Clone the repository and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file or export the required environment variables. When running in production you need `SERVICE_ACCOUNT_JSON` for Firebase credentials. You can set `JWT_SECRET_KEY` to override the default JWT signing key (`supersecretjwtkey`).
4. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Running Tests

The tests use mocked Firebase services and expect the `TESTING` environment variable to be set. Run:

```bash
TESTING=1 pytest
```
