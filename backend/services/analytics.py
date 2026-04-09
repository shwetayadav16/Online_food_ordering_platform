def most_ordered(items):
    freq = {}

    for item in items:
        name = item["name"]
        freq[name] = freq.get(name, 0) + 1

    return max(freq, key=freq.get) if freq else None