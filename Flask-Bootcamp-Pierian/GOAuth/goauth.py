import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["GOOGLE_OAUTH_CLIENT_ID"] = "491181022468-2370hviflbflmvcag972eo52r6rp8p95.apps.googleusercontent.com"
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = "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"
google_bp = make_google_blueprint(scope=["profile", "email"])
app.register_blueprint(google_bp, url_prefix="/login")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    # Return internal server error if not authorized
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]
    return render_template("welcome.html", email = email)

@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]
    return render_template("welcome.html", email = email)

if __name__ == "__main__":
    app.run(debug=False)