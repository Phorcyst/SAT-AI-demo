# Docker Network Fix: Connecting Open WebUI to Ollama

**Date:** 2026-02-28

## The Problem
Open WebUI was trying to connect to `host.docker.internal:11434`, which doesn't work on Linux Docker (only Windows/Mac).

Error in logs:
Connection error: Cannot connect to host host.docker.internal:11434
[Name or service not known]


## The Fix

### 1. Find Docker Gateway IP

docker network inspect bridge | grep Gateway
# Output: "Gateway": "172.17.0.1"

###2. Recreate Open WebUI with Correct URL

docker stop open-webui
docker rm open-webui

docker run -d \
  --name open-webui \
  --restart always \
  -p 3000:8080 \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://172.17.0.1:11434 \
  -e WEBUI_SECRET_KEY="your-secret-key" \
  -e JWT_EXPIRES_IN="30d" \
  ghcr.io/open-webui/open-webui:main

###3. Verify Connection

docker logs open-webui --tail 50 | grep -i ollama
# No more connection errors
    Docker containers use the gateway IP (usually 172.17.0.1) to reach services on the host

    Ollama is running on the host and listening on all interfaces (thanks to our OLLAMA_HOST=0.0.0.0 setting)

    Open WebUI can now communicate with Ollama
