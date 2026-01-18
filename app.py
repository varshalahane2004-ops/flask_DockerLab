from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    with open("/logs/app.log", "a") as f:
        f.write(str(datetime.datetime.now()) + " - App Visited\n")
    return "Flask App Running with Volume Logging!"

app.run(host="0.0.0.0", port=5000)