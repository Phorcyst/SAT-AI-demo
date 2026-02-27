# OpenWebUI Installation

**Date:** 2026-02-28
**Container:** 104 (sat-ai-tutor)

## Installation Command
```bash
docker run -d \
  --name open-webui \
  --restart always \
  -p 3000:8080 \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  -e WEBUI_SECRET_KEY="$(openssl rand -hex 32)" \
  -e JWT_EXPIRES_IN="30d" \
  ghcr.io/open-webui/open-webui:main
