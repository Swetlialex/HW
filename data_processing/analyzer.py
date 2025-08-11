# data_processing/analyzer.py

def calculate_average(data):
    """Изчислява средната стойност на даден списък."""
    if not data:
        return 0
    return sum(data) / len(data)
