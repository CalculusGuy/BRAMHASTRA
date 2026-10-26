import os
import requests
import time

class GeminiAdapter:
    def __init__(self, model=None):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing.")
        
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
        
        # The Fallback Chain
        self.model_chain = [
            "gemini-3.8-flash",
            "gemini-flash-latest",
            "gemini-3.5-flash",
            "gemini-3.5-flash-lite",
            "gemini-flash-lite-latest"
        ]
        
        if model:
            self.model_chain.insert(0, model)

    def _send_single(self, prompt: str, model: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(self.base_url, headers=headers, json=data, timeout=20)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        
        raise Exception(f"HTTP {response.status_code}")

    def send(self, prompt: str) -> str:
        last_error = "Unknown error"
        
        for model in self.model_chain:
            for attempt in range(2): # 2 attempts per model
                try:
                    return self._send_single(prompt, model)
                except requests.exceptions.Timeout:
                    last_error = f"{model}: Timeout"
                    time.sleep(2) # Backoff
                except requests.exceptions.ConnectionError:
                    last_error = f"{model}: Connection Error"
                    time.sleep(2)
                except Exception as e:
                    last_error = f"{model}: {str(e)}"
                    break # Move to next model on 404/400 errors
        
        return f"ALL_MODELS_FAILED: {last_error}"
