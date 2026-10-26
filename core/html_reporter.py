import html
from datetime import datetime

def generate_html_report(results, target_model, output_path):
    vuln_count = sum(1 for r in results if r["verdict"] == "vulnerable")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BRAMHASTRA v2 Report</title>
        <style>
            body {{ background-color: #0a0a0f; color: #e8e8f0; font-family: 'Courier New', monospace; padding: 40px; }}
            h1 {{ color: #00ff9d; border-bottom: 1px solid #222232; padding-bottom: 10px; }}
            .summary {{ background: #13131c; border: 1px solid #222232; padding: 20px; margin-bottom: 30px; display: flex; gap: 40px; }}
            .card {{ border-left: 4px solid #222232; background: #13131c; padding: 20px; margin-bottom: 20px; }}
            .vuln {{ border-left-color: #ff4444; }}
            .safe {{ border-left-color: #00ff9d; }}
            .uncertain {{ border-left-color: #ffaa33; }}
            .tag {{ background: #222232; padding: 2px 8px; font-size: 12px; border-radius: 3px; }}
            .prompt {{ color: #888; margin: 10px 0; }}
            .response {{ background: #06060b; padding: 15px; border: 1px solid #222232; white-space: pre-wrap; font-size: 14px; }}
            .reason {{ color: #00d4ff; font-size: 13px; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <h1>⚔ BRAMHASTRA v2 — LLM Security Evaluation Report</h1>
        <div class="summary">
            <div><strong>Target Model:</strong> {target_model}</div>
            <div><strong>Tests Run:</strong> {len(results)}</div>
            <div><strong>Vulnerabilities Found:</strong> <span style="color:#ff4444">{vuln_count}</span></div>
            <div><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        </div>
    """
    
    for r in results:
        status_class = "vuln" if r["verdict"] == "vulnerable" else ("safe" if r["verdict"] == "likely_safe" else "uncertain")
        html_content += f"""
        <div class="card {status_class}">
            <h3>{r['id']} - {r['category'].upper()} <span class="tag">{r.get('owasp', 'N/A')}</span></h3>
            <p><strong>Verdict:</strong> {r['verdict'].upper()} (Confidence: {r['confidence']})</p>
            <div class="prompt"><strong>Payload:</strong><br>{html.escape(str(r.get('prompt', 'Multi-turn Chain (See Response)'))) }</div>
            <div class="response"><strong>Response:</strong><br>{html.escape(str(r.get('response', 'No response')))}</div>
            <div class="reason"><strong>Reasoning:</strong> {html.escape(r['reason'])}</div>
        </div>
        """
        
    html_content += "</body></html>"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return output_path
