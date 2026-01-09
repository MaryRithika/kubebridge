from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "DevOps GKE + Argo CD is LIVE 🚀"

@app.route("/healthz")
def health():
    return "ok"

@app.route("/readyz")
def ready():
    return "ready"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
