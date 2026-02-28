"""
SAT Tutor AI Client
For backend team integration

Installation:
    pip install requests python-dotenv

Usage:
    from sat_tutor_client import SATTutorClient

    client = SATTutorClient()
    response = client.ask("What is the quadratic formula?")
    print(response["answer"])
    print("Sources:", response["sources"])
"""

import os
import requests
from dotenv import load_dotenv
from typing import Optional, Dict, List, Generator
import json

# Load environment variables from .env file
load_dotenv()

class SATTutorClient:
    """
    Client for the SAT Tutoring AI API.

    Credentials are loaded from environment variables:
    - OPENWEBUI_URL: Your OpenWebUI server URL
    - OPENWEBUI_API_KEY: Your API key
    - KNOWLEDGE_BASE_ID: ID of your SAT materials
    - MODEL: Model to use (default: gpt-oss:20b-cloud)
    """

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        knowledge_base_id: Optional[str] = None,
        model: Optional[str] = None
    ):
        """Initialize the client with credentials from env vars or parameters."""
        self.url = url or os.getenv("OPENWEBUI_URL")
        self.api_key = api_key or os.getenv("OPENWEBUI_API_KEY")
        self.knowledge_base_id = knowledge_base_id or os.getenv("KNOWLEDGE_BASE_ID")
        self.model = model or os.getenv("MODEL", "gpt-oss:20b-cloud")

        # Validate required credentials
        if not self.url:
            raise ValueError("OPENWEBUI_URL must be set in .env or passed to constructor")
        if not self.api_key:
            raise ValueError("OPENWEBUI_API_KEY must be set in .env or passed to constructor")
        if not self.knowledge_base_id:
            raise ValueError("KNOWLEDGE_BASE_ID must be set in .env or passed to constructor")

        # Set up headers for API requests
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def ask(self, question: str, stream: bool = False) -> Dict:
        """
        Send a question to the SAT tutor.

        Args:
            question: The student's question
            stream: Whether to stream the response

        Returns:
            Dictionary with 'answer', 'sources', and 'model'
        """
        # Prepare the request payload
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": question}],
            "files": [{"type": "collection", "id": self.knowledge_base_id}],
            "stream": stream
        }

        # Send the request to OpenWebUI
        response = requests.post(
            f"{self.url}/api/chat/completions",
            headers=self.headers,
            json=payload
        )

        # Check for errors
        response.raise_for_status()

        # Parse the response
        data = response.json()

        # Return clean result
        return {
            "answer": data["choices"][0]["message"]["content"],
            "sources": data.get("citations", []),
            "model": data["model"]
        }

    def ask_stream(self, question: str) -> Generator[str, None, None]:
        """
        Stream the response token by token (for chat UI).

        Args:
            question: The student's question

        Yields:
            JSON strings containing response chunks
        """
        # Prepare the request payload
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": question}],
            "files": [{"type": "collection", "id": self.knowledge_base_id}],
            "stream": True
        }

        # Send the request with streaming enabled
        with requests.post(
            f"{self.url}/api/chat/completions",
            headers=self.headers,
            json=payload,
            stream=True
        ) as response:
            # Process each line of the stream
            for line in response.iter_lines():
                if line and line.startswith(b"data: "):
                    # Remove the "data: " prefix and decode
                    yield line[6:].decode('utf-8')

    def get_models(self) -> List[str]:
        """List available models."""
        response = requests.get(
            f"{self.url}/api/models",
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json()
        return [model["id"] for model in data.get("data", [])]


# Example usage
if __name__ == "__main__":
    # This will load from .env file
    client = SATTutorClient()

    # Test the connection
    try:
        print("Testing connection...")
        models = client.get_models()
        print(f"✅ Connected! Available models: {models}")

        print("\nAsking test question...")
        response = client.ask("What is the quadratic formula?")
        print(f"Answer: {response['answer'][:200]}...")
        print(f"Sources: {response['sources']}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Check your .env file credentials")
