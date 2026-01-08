from flask import Flask, jsonify
import os, time

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(service="devops-k8s-platform", version=os.getenv("APP_VERSION", "local"))

@app.get("/healthz")
def healthz():
    return "ok", 200

@app.get("/readyz")
def readyz():
    return "ready", 200

@app.get("/work")
def work():
    start = time.time()
    x = 0
    while time.time() - start < 0.25:
        x += 1
    return jsonify(done=True, loops=x)
