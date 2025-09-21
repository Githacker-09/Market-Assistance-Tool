from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔥 allow frontend to access backend

@app.route("/generate_strategy", methods=["POST"])
def generate_strategy():
    data = request.json
    business = data.get("business")
    location = data.get("location")
    goal = data.get("goal")

    strategy = {
        "roadmap": [
            f"Set up initial ad campaign for {business}",
            f"Target local customers in {location}",
            f"Focus on goal: {goal}"
        ],
        "social": {
            "captions": [f"Best {business} in {location}!"],
            "hashtags": ["#localbusiness", "#supportsmall", "#growth"]
        },
        "local_ads": [
            f"Distribute flyers in {location}",
            f"Contact local print shops in {location}"
        ]
    }
    return jsonify(strategy)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
