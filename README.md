<div align="center">

# BRAMHASTRA v2

### LLM Security Evaluation Harness with Multi-Turn Attack Chains and OWASP LLM Top 10 Conformance Reporting

**Gemini Cloud · 34 Payloads · 5-Model Fallback Chain · Negation-Aware Detection**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![AI Security](https://img.shields.io/badge/AI-Security-DC2626?style=for-the-badge)](https://github.com/CalculusGuy/BRAMHASTRA)
[![OWASP LLM](https://img.shields.io/badge/OWASP-LLM_Top_10-7C3AED?style=for-the-badge)](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
[![License](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-059669?style=for-the-badge)](https://github.com/CalculusGuy/BRAMHASTRA)

**Created by [Nilanjan Chowdhury](https://github.com/CalculusGuy)**

</div>

---

## Overview

**BRAMHASTRA** is an industry-grade AI red-teaming framework designed to evaluate the security posture of Large Language Models. 

Unlike v1, which relied on heavy local model inference, **v2 is built for the cloud**. It tests LLM endpoints against a structured suite of adversarial payloads while requiring zero local GPU or CPU strain.

The harness fires **34 payloads** across 8 attack categories, classifies the model's behavior using a **negation-aware detection engine**, maps findings to the **OWASP LLM Top 10**, and generates a professional HTML/JSON report.

```text
Payload Suite (YAML)
       ↓
Orchestrator (Engine)
       ↓
Gemini Cloud Adapter (5-Model Fallback)
       ↓
Negation-Aware Detector
       ↓
OWASP LLM Top 10 Mapper
       ↓
HTML / JSON Report
