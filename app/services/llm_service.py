"""Wrapper utilities for LLM related calls."""

from __future__ import annotations

import os

from app.utils import openrouter_client


def call_openrouter(prompt: str) -> str:
    """Send ``prompt`` to the OpenRouter API using default credentials."""

    model = os.getenv("OPENROUTER_MODEL", "")
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    return openrouter_client.call_openrouter(prompt, model, api_key)
