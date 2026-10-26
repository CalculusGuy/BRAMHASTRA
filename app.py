# app.py — Minimal FastAPI wrapper for Render health check
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="BRAMHASTRA v2")

@app.get("/")
def root():
    return {"status": "online", "service": "BRAMHASTRA v2", "message": "CLI tool. Run locally for full scans."}

@app.get("/health")
def health():
    return {"status": "healthy"}
