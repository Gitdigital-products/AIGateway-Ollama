<!-- Security Badges -->
![Security Foundational](https://img.shields.io/badge/security-foundational-blue)
![Security Scanning](https://img.shields.io/badge/security-scanning-active-green)

<!-- Activity Badges -->
![Last Commit](https://img.shields.io/badge/commit-current-brightgreen)
![Issues Health](https://img.shields.io/badge/issues-healthy-brightgreen)
![Release Cadence](https://img.shields.io/badge/releases-active-brightgreen)

<!-- Maturity Badges -->
![CI Status](https://img.shields.io/badge/CI-passing-brightgreen)
![Versioning](https://img.shields.io/badge/versioning-semver-blue)

<!-- Technology Badges -->
![Primary Language](https://img.shields.io/badge/language-JavaScript-yellow)
![Containerized](https://img.shields.io/badge/containerized-Docker-blue)

<!-- Quality Badges -->
![Linting](https://img.shields.io/badge/linting-passing-brightgreen)
![Documentation](https://img.shields.io/badge/docs-complete-brightgreen)

<!-- Community Badges -->
![Contributors](https://img.shields.io/badge/contributors-2-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)


<a href="https://qlty.sh/gh/RickCreator87/projects/AIGateway-Ollama"><img src="https://qlty.sh/gh/RickCreator87/projects/AIGateway-Ollama/coverage.svg" alt="Code Coverage" /></a>
![CI](https://github.com/RickCreator87/aigateway-ollama/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/RickCreator87/aigateway-ollama)
![Stars](https://img.shields.io/github/stars/RickCreator87/aigateway-ollama)
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
