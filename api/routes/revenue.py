from flask import request, jsonify
from api.services.revenue import predict

def init_revenue_route(app):
    @app.route("/predict/revenue", methods=["POST"])
    def predict_revenue():
        req = request.get_json()
        revenues = req.get("revenues")

        result = predict(revenues)

        return jsonify({
            "revenue": result
        })