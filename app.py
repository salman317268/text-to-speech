from flask import Flask, render_template, request, send_file, jsonify, Response
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text", "").strip()
    language = request.form.get("language", "en")

    if not text:
        return jsonify({"error": "Please enter some text"}), 400

    if language not in ["bn", "en"]:
        return jsonify({"error": "Invalid language"}), 400

    try:
        audio = BytesIO()

        voice = gTTS(text=text, lang=language)
        voice.write_to_fp(audio)

        audio.seek(0)

        return send_file(
            audio,
            mimetype="audio/mpeg",
            as_attachment=False,
            download_name="voice.mp3"
        )

    except Exception:
        return jsonify({"error": "Voice generation failed"}), 500


# Google Sitemap
@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://text-to-speech-dv7n.onrender.com/</loc>
        </url>
    </urlset>
    """
    return Response(xml, mimetype="application/xml")


# Search Engine Robots
@app.route("/robots.txt")
def robots():
    content = """User-agent: *
Allow: /

Sitemap: https://text-to-speech-dv7n.onrender.com/sitemap.xml
"""
    return Response(content, mimetype="text/plain")


if __name__ == "_main_":
    app.run(debug=False)
