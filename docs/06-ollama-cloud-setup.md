# Ollama Cloud Setup

**Date:** 2026-02-28
**Container:** 104 (sat-ai-tutor)

## Why Cloud Models?
| Factor | Local 8B | Cloud 20B+ |
|--------|----------|------------|
| Speed on CPU | 2-7 tokens/sec | Fast (runs on their servers) |
| Quality | Good | Excellent |
| RAM Usage | 6-8GB | None (offloaded) |
| 50 concurrent users | ❌ Impossible | ✅ Possible |

## Setup Process

### 1. Create Ollama Account
- Signed up at [ollama.com](https://ollama.com)
- Generated API key from account dashboard

### 2. Authentication in Container
ollama signin
# Followed browser authentication
### 3. Environment Variable
export OLLAMA_API_KEY="your-api-key-here"
echo 'export OLLAMA_API_KEY="your-api-key-here"' >> ~/.bashrc
