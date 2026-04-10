def calculate_total(items):
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    # discount
    if total > 500:
        total *= 0.9

    return total