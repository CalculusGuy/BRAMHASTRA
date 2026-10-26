import argparse
import sys
import os
from dotenv import load_dotenv

from adapters.gemini_adapter import GeminiAdapter
from core.engine import load_payloads, run_single_shot
from core.html_reporter import generate_html_report

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="BRAMHASTRA v2 — LLM Red Teaming Framework")
    parser.add_argument("--suite", default="all", choices=["single_shot", "multi_turn", "tool_call", "all"], help="Which payload suite to run")
    parser.add_argument("--report", action="store_true", help="Generate HTML report")
    args = parser.parse_args()

    print("\n" + "="*50)
    print(" ⚔ BRAMHASTRA v2 — AI RED TEAMING FRAMEWORK")
    print("="*50 + "\n")

    try:
        adapter = GeminiAdapter()
        print("[+] Gemini Adapter initialized.")
    except Exception as e:
        print(f"[-] Error initializing adapter: {e}")
        sys.exit(1)

    suites_to_run = ["single_shot", "multi_turn", "tool_call"] if args.suite == "all" else [args.suite]
    all_payloads = []
    
    for suite in suites_to_run:
        path = f"payloads/{suite}.yaml"
        if os.path.exists(path):
            payloads = load_payloads(path)
            all_payloads.extend(payloads)
        else:
            print(f"[-] Warning: {path} not found.")
    
    print(f"[+] Loaded {len(all_payloads)} payloads.")
    print(f"[*] Firing payloads against GEMINI...\n")

    results = run_single_shot(adapter, all_payloads)

    vuln_count = 0
    for r in results:
        color = "\033[91m" if r["verdict"] == "vulnerable" else ("\033[92m" if r["verdict"] == "likely_safe" else "\033[93m")
        reset = "\033[0m"
        
        if r["verdict"] == "vulnerable":
            vuln_count += 1
            
        print(f"{color}[{r['verdict'].upper()}]{reset} {r['id']} ({r['category']}) - Conf: {r['confidence']}")
        if r["verdict"] == "vulnerable":
            print(f"    -> Response: {r['response'][:80]}...")
    
    print("\n" + "="*50)
    print(f" [+] Scan Complete. Found {vuln_count} vulnerabilities.")
    
    if args.report:
        report_path = "bramhastra_report.html"
        generate_html_report(results, "Gemini 3.8 Flash", report_path)
        print(f" [+] HTML Report saved to: {report_path}")

if __name__ == "__main__":
    main()
