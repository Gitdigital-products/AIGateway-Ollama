![Last Commit](https://img.shields.io/github/last-commit/RickCreator87/aigateway-ollama)Repo Size

![Repo Size](https://img.shields.io/github/repo-size/RickCreator87/aigateway-ollama)
# AIGateway-Ollama

![CI](https://github.com/Gitdigital-products/AIGateway-Ollama/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/Gitdigital-products/AIGateway-Ollama)
![Last Commit](https://img.shields.io/github/last-commit/Gitdigital-products/AIGateway-Ollama)
![Version](https://img.shields.io/github/v/release/Gitdigital-products/AIGateway-Ollama)

# AI Gateway for Ollama

An OpenAI API–compatible gateway that proxies requests to a local Ollama instance.

This project lets you run local LLMs via Ollama while keeping compatibility with tools and SDKs built for the OpenAI API.

---

## What This Does

- Exposes OpenAI-style endpoints (`/v1/chat/completions`)
- Forwards requests to Ollama
- Uses API keys to select models and behavior
- Runs locally via Docker or directly with Python

If a client works with `api.openai.com`, it should work here with minimal or zero changes.

---

## Architecture (High Level)
