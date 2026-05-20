from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.index import init_index_route
    from app.routes.revenue import init_revenue_route

    init_index_route(app)
    init_revenue_route(app)

    return app