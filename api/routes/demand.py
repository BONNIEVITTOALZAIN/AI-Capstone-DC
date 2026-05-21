from flask import request, jsonify
from api.services.demand import predict

def init_demand_route(app):
    @app.route("/predict/demand", methods=["POST"])
    def predict_demand():
        req = request.get_json()
        demands = req.get("demands")
        stock = req.get("stock")

        result = predict(demands, stock)

        return jsonify({
            "lasting_day": result[0],
            "total_demand": result[1]
        })