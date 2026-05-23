from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from api.routes.index import init_index_route
    from api.routes.revenue import init_revenue_route
    from api.routes.demand import init_demand_route
    from api.routes.bundling import init_bundling_route

    init_index_route(app)
    init_revenue_route(app)
    init_demand_route(app)
    init_bundling_route(app)

    return app