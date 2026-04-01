"""Utility functions for data processing."""

def process_data(items: list) -> dict:
    """Process a list of items and return summary statistics."""
    if not items:
        return {"count": 0, "sum": 0, "avg": 0}
    
    total = sum(items)
    count = len(items)
    return {
        "count": count,
        "sum": total,
        "avg": total / count,
        "min": min(items),
        "max": max(items)
    }

def filter_outliers(data: list, threshold: float = 2.0) -> list:
    """Remove outliers from data using standard deviation."""
    import statistics
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    return [x for x in data if abs(x - mean) <= threshold * stdev]
# Staging bot test v2 - Wed Apr  1 14:49:55 EDT 2026
def hello(): return 'world' # Wed Apr  1 15:25:21 EDT 2026
def greet(name): return f'Hello {name}'
