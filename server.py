from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/get_details", methods=["GET"])
def get_details():
    titles, directors = util.get_titles_and_directors()
    return jsonify({
        "titles": titles,
        "directors": directors
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        result = util.predict_movie_success(data)
        return jsonify({
            "prediction": result
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)
