from flask import request, jsonify
from services.order_service import calculate_total
from database import get_db

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
    @app.route("/order", methods=["POST"])
    def place_order():
        data = request.json

        if not data or "items" not in data:
            return jsonify({"error": "Invalid request"}), 400

        items = data["items"]
        total = calculate_total(items)

        conn = get_db()
        cursor = conn.cursor()

        # Insert order
        cursor.execute(
            "INSERT INTO orders (total) VALUES (?)",
            (total,)
        )
        order_id = cursor.lastrowid

        # Insert items
        for item in items:
            cursor.execute(
                "INSERT INTO order_items (order_id, name, price, quantity) VALUES (?, ?, ?, ?)",
                (order_id, item["name"], item["price"], item["quantity"])
            )

        conn.commit()
        conn.close()

        return jsonify({
            "message": "Order placed successfully",
            "order_id": order_id,
            "total": total
        })

    # Get Orders
    @app.route("/orders", methods=["GET"])
    def get_orders():
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result.append({
                "id": row["id"],
                "total": row["total"]
            })

        conn.close()
        return jsonify(result)
    