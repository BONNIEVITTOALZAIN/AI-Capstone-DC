from flask import request, jsonify
from app.services.revenue import predict

def init_revenue_route(app):
    @app.route("/predict/revenue", methods=["POST"])
    def predict_revenue():
        req = request.get_json()
        data = req.get("revenues")

        result = predict(data)

        return jsonify({
            "prediction": result
        })