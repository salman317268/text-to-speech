from flask import Flask, render_template, request, send_file, jsonify
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


if __name__ == "__main__":
    app.run(debug=False)