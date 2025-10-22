def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def calculate_sum(numbers):
    return sum(numbers)
