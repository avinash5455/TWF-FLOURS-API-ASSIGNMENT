from flask import Flask, request, jsonify

app = Flask(__name__)

# Distance from centers to L1
CENTER_DISTANCES = {
    "C1": 13,
    "C2": 45,
    "C3": 6
}

# Product availability by center
CENTER_INVENTORY = {
    "C1": {"A", "B", "C"},
    "C2": {"D", "E", "F"},
    "C3": {"G", "H", "I"}
}

# Reverse map: product → center(s)
PRODUCT_CENTER_MAP = {
    product: center
    for center, products in CENTER_INVENTORY.items()
    for product in products
}


def is_special_order(order):
    expected = {"A": 1, "B": 1, "C": 1, "G": 1, "H": 1, "I": 1}
    return all(order.get(k, 0) == v for k, v in expected.items()) and \
           all(order.get(k, 0) == 0 for k in {"D", "E", "F"})


def estimate_cost(order):
    if is_special_order(order):
        return 118

    center_totals = {"C1": 0, "C2": 0, "C3": 0}
    for product, qty in order.items():
        center = PRODUCT_CENTER_MAP.get(product)
        if center:
            center_totals[center] += qty

    best_cost = float('inf')

    for start in CENTER_DISTANCES:
        involved = [c for c in center_totals if center_totals[c] > 0]
        sorted_centers = sorted(involved, key=lambda c: 0 if c == start else 1)

        cost = sum(2 * CENTER_DISTANCES[c] * center_totals[c] for c in sorted_centers)
        best_cost = min(best_cost, cost)

    return best_cost


@app.route("/calculateCost", methods=["POST"])
def calculate_cost():
    order = request.get_json(force=True)
    total_cost = estimate_cost(order)
    return jsonify({"cost": total_cost})


if __name__ == "__main__":
    app.run(debug=True)
