# Ollama Installation

**Date:** 2026-02-28
**Container:** 104 (sat-ai-tutor)

## Installation
```bash
curl -fsSL https://ollama.com/install.sh | sh

Configuration for Docker Access

By default, Ollama only listens on localhost. Docker containers need access, so we configured it to listen on all interfaces:
bash

# Create override
mkdir -p /etc/systemd/system/ollama.service.d
cat > /etc/systemd/system/ollama.service.d/override.conf << 'EOF'
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
EOF

systemctl daemon-reload
systemctl restart ollama

Models Downloaded
Model	        Size	Purpose
ollama cloud    non     non
phi3:mini	2.2GB	Backup/test

ollama list
# Shows both models

ss -tulpn | grep 11434
# Shows *:11434 (listening on all interfaces)
