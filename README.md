# SAT-AI-demo

This repository contains the infrastructure and API client for the SAT tutoring AI service.

## Purpose
- AI backend that answers SAT questions using ONLY authorized study materials (RAG-based)

## 📦 Components
- **OpenWebUI Server**: Hosts the AI models and RAG knowledge base
- **Ollama**: Runs local LLMs (llama3:8b, etc.)
- **Python Client**: Ready-to-use client for backend integration
- **Documentation**: Complete setup and API guides

## Infrastructure
- Hosted on Proxmox LXC container (Ubuntu 24.04)
- 4 CPU cores, 8GB RAM (configurable)
- Docker + OpenWebUI + Ollama stack

## Security
- API key authentication
- HTTPS required
- Rate limiting enabled
- JWT token expiration (30 days)

## Knowledge Base
- Adding later

## For Backend Team
See `/api-client` directory for the Python client and integration examples.
