# SAT AI Tutor - Project Overview

**Date:** 2026-02-28
#Build an AI-powered SAT tutor:
- Only answers from uploaded SAT materials (PDFs, practice tests)
- Provides citations showing source material
- Integrates via API
- Serves ~50 concurrent user

#Steps:
- Set up AI infrastructure (OpenWebUI + Ollama)
- Create SAT knowledge base with RAG
- Provide secure API access to backend team
- Document everything for handoff

my first time doin funni business;D

## Architecture Overview
Student Website (Frontend) ←→ Backend API ←→ My OpenWebUI Server ←→ Ollama Models



## Repository Structure
sat-ai-tutor/
├── docs/ # All documentation
├── infrastructure/ # Server setup scripts/configs
├── api-client/ # Python client for backend team
├── notes/ # Personal notes, troubleshooting
└── README.md # Project overview
