from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows requests from frontend / Postman

# Sample local advertiser data
local_advertisers = {
    "jaipur": [
        "Pink City Printers – Flyers & Posters",
        "Jaipur Radio 101 FM – Local Ads",
        "Johari Bazaar Billboard Service"
    ],
    "delhi": [
        "Connaught Place Print Hub",
        "Delhi Metro Ads",
        "Delhi Times Newspaper"
    ]
}

# Temporary GET route to test server
@app.route("/", methods=["GET"])
def home():
    return "Flask server is running!"

# POST route for marketing strategy
@app.route("/generate_strategy", methods=["POST"])
def generate_strategy():
    data = request.json
    business = data.get("business", "Your Business")
    location = data.get("location", "Your City")
    goal = data.get("goal", "Get Started")

    # Simple roadmap logic
    roadmap = [
        f"Create social pages for {business}.",
        f"Post about your product in {location}.",
        "Engage with local customers via social media."
    ]

    social = {
        "captions": [f"Check out {business} in {location}!", "Support local businesses!"],
        "hashtags": ["#SupportLocal", f"#{location}Crafts", f"#{business.replace(' ', '')}"]
    }

    local_ads = local_advertisers.get(location.lower(), ["Use local print shops, fairs, or community boards."])

    return jsonify({
        "roadmap": roadmap,
        "social": social,
        "local_ads": local_ads
    })

if __name__ == "__main__":
    # host=0.0.0.0 ensures Postman can connect
    app.run(host="0.0.0.0", port=5050, debug=True)
