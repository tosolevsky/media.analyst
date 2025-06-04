# Media Analyst

Media Analyst is a FastAPI based service for AI‑assisted content generation and analysis. It integrates with Firebase for data storage and uses large language models to create short form text. The project exposes REST endpoints for authentication, bot responses and feedback collection.

The service currently supports OpenAI, Anthropic and OpenRouter models for text generation.

## Setup

1. Install Python 3.11 or later.
2. Clone the repository and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file or export the required environment variables:
   - `SERVICE_ACCOUNT_JSON` – Firebase credentials needed in production.
   - `JWT_SECRET_KEY` – secret value used for signing JWT access tokens.
   - `OPENROUTER_MODEL` – default OpenRouter model for guideline generation.
   - `OPENROUTER_API_KEY` – API key for calling OpenRouter.
4. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Running Tests

The tests use mocked Firebase services and expect the `TESTING` environment variable to be set. Run:

```bash
TESTING=1 pytest
```
