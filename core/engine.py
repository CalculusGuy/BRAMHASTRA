import yaml
from .detector import score_response

def load_payloads(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def run_single_shot(adapter, payloads):
    results = []
    for p in payloads:
        # Check if it's a multi-turn chain
        if p.get("turns"):
            # Join the turns with a newline to simulate the conversation
            prompt = "\n".join([turn["text"] for turn in p["turns"]])
        else:
            prompt = p.get("text", "")
            
        response = adapter.send(prompt)
        score = score_response(p, response)
        
        results.append({
            "id": p.get("id"),
            "category": p.get("category"),
            "owasp": p.get("owasp_mapping"),
            "prompt": prompt,
            "response": response,
            "verdict": score["verdict"],
            "confidence": score["confidence"],
            "reason": score["reason"]
        })
    return results
