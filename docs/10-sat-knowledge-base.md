# SAT Knowledge Base Creation

**Date:** 2026-02-28
**Knowledge Base Name:** SAT Materials

## Purpose
Create a searchable repository of SAT materials that the AI will use exclusively for answering questions. This ensures:
- Answers are grounded in official materials
- No hallucinations about non-SAT topics
- Citations can be provided to students

## Materials Uploaded
| File Type | Description | Quantity |
|-----------|-------------|----------|
| 

## Knowledge Base ID
in .env

## How to Use in Chat
1. Select cloud model (e.g., `gpt-oss:20b-cloud`)
2. Click paperclip icon
3. Choose "SAT Master Material"
4. Ask questions - answers will come only from uploaded materials

## Testing Results
| Test Question | Source Found? | Response Quality |
|---------------|---------------|------------------|
||

## API Integration Note
When making API calls, include:
```json
"files": [{"type": "collection", "id": "your-knowledge-base-id"}]
