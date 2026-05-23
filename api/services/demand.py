import numpy as np
from tensorflow.keras.layers import TFSMLayer
import joblib

model = TFSMLayer("api/models/demand/", call_endpoint="serving_default")
scaler = joblib.load("api/models/scaler/demand_scaler.pkl")

WINDOW_SIZE=3

def predict(data):
    result = []

    for product in data.keys():
        demands = data[product]["demands"]
        stock = data[product]["stock"]

        total_demand = 0
        lasting_day = 0

        demands = np.array(demands).reshape(-1, 1)
        scaled_demands = scaler.fit_transform(demands)

        while total_demand <= stock:
            input = scaled_demands.reshape(1, WINDOW_SIZE, 1)

            scaled_prediction = model(input)
            scaled_prediction = list(scaled_prediction.values())[0]
            
            prediction = scaler.inverse_transform(scaled_prediction)
            prediction = int(prediction[0][0])

            total_demand += prediction
            lasting_day += 1

            demands = np.append(demands, prediction)
            demands = demands[1:]
            demands = np.array(demands).reshape(-1, 1)

            scaled_demands = scaler.transform(demands)

        result.append({
            "product": product,
            "lasting_day": lasting_day,
            "total_demand": total_demand
        })
    
    result = sorted(
        result,
        key=lambda x: (x["lasting_day"], -x["total_demand"]),
    )

    top_n = 5 if len(result) > 5 else len(result)
    
    return result[:top_n]