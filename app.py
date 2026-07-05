from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SITE_KEY = os.getenv("TURNSTILE_SITE_KEY")


@app.route("/")
def home():
    return render_template(
        "verify.html",
        site_key=SITE_KEY
    )


if __name__ == "__main__":
    app.run()
