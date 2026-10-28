from flask import Flask, render_template, request, redirect, abort
from pathlib import Path
import csv
import os
import re

app = Flask(__name__, template_folder="templates")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

PAGES = {"index.html", "about.html", "works.html", "contact.html", "thankyou.html"}
DATA_PATH = Path(os.environ.get("CONTACT_DATA_PATH", "contact-submissions.csv"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    if page_name not in PAGES:
        abort(404)
    return render_template(page_name)


@app.route("/favicon.ico")
def favicon():
    return "", 204


def validate_contact_form(data):
    email = data.get("email", "").strip()
    subject = data.get("subject", "").strip()
    message = data.get("message", "").strip()
    if not (3 <= len(email) <= 254 and re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email)):
        return None
    if not (1 <= len(subject) <= 150 and 1 <= len(message) <= 3000):
        return None
    return email, subject, message


@app.route("/submit_form", methods=["POST"])
def submit_form():
    fields = validate_contact_form(request.form)
    if fields is None:
        return "Please provide a valid email, subject, and message.", 400

    # Store submissions outside the repository and do not log personal messages.
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with DATA_PATH.open("a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(fields)
    return redirect("/thankyou.html", code=303)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
