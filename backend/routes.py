from flask import jsonify

def register_routes(app):

    @app.route("/")
    def home():
        return "API Running"

    @app.route("/menu")
    def get_menu():
        data = [
            {"id": 1, "name": "Pizza", "price": 200},
            {"id": 2, "name": "Burger", "price": 100}
        ]
        return jsonify(data)