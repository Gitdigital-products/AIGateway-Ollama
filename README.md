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
https://img.shields.io/badge/Architecture-AI%20Gateway-blue?style=flat
https://img.shields.io/badge/Cloud-None-important?style=flat
https://img.shields.io/badge/AI-Local--Only-success?style=flat
https://img.shields.io/badge/Ollama-Powered-000000?style=flat&logo=llama&logoColor=white
![Ollama Powered](https://img.shields.io/badge/Ollama-Powered-000000?style=flat&logo=llama&logoColor=white)
![Local AI Only](https://img.shields.io/badge/AI-Local--Only-success?style=flat)
![No Cloud Dependency](https://img.shields.io/badge/Cloud-None-important?style=flat)
![Gateway Architecture](https://img.shields.io/badge/Architecture-AI%20Gateway-blue?style=flat)
https://img.shields.io/badge/Models-Agnostic-lightgrey?style=flat
https://img.shields.io/badge/Outputs-Deterministic-informational?style=flat
![Prompt Orchestrated](https://img.shields.io/badge/Prompts-Orchestrated-blueviolet?style=flat)
![Role Based AI](https://img.shields.io/badge/AI-Role%20Based-ff69b4?style=flat)
![Deterministic Outputs](https://img.shields.io/badge/Outputs-Deterministic-informational?style=flat)
![Model Agnostic](https://img.shields.io/badge/Models-Agnostic-lightgrey?style=flat)
https://img.shields.io/badge/Security-First-critical?style=flat
https://img.shields.io/badge/PQC-Ready-yellow?style=flat
https://img.shields.io/badge/Crypto-Quantum--Safe%20Design-9cf?style=flat
![Quantum Safe Design](https://img.shields.io/badge/Crypto-Quantum--Safe%20Design-9cf?style=flat)
![Post Quantum Ready](https://img.shields.io/badge/PQC-Ready-yellow?style=flat)
![Security First](https://img.shields.io/badge/Security-First-critical?style=flat)
https://img.shields.io/badge/Coupling-Loose-success?style=flat
https://img.shields.io/badge/System-Composable-blue?style=flat
https://img.shields.io/badge/Module-Micro-lightblue?style=flat
![Modular Design](https://img.shields.io/badge/Design-Modular-brightgreen?style=flat)
![Micro Module](https://img.shields.io/badge/Module-Micro-lightblue?style=flat)
![Composable System](https://img.shields.io/badge/System-Composable-blue?style=flat)
![Loose Coupling](https://img.shields.io/badge/Coupling-Loose-success?style=flat)
https://img.shields.io/badge/Design-Modular-brightgreen?style=flat
https://img.shields.io/badge/Status-Early%20Development-orange?style=flathttps://img.shields.io/badge/Stage-Experimental-yellow?style=flathttps://img.shields.io/badge/Research-Open-lightgrey?style=flat![Early Development](https://img.shields.io/badge/Status-Early%20Development-orange?style=flat)
![Experimental](https://img.shields.io/badge/Stage-Experimental-yellow?style=flat)
![Open Research](https://img.shields.io/badge/Research-Open-lightgrey?style=flat)
https://img.shields.io/badge/Status-Early%20Development-orange?style=flat
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
