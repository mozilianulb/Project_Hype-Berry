# This script contains TODO comments to trigger warnings in GitHub Actions

def process_data(data):
    # TODO: Handle edge cases where data is None
    if data is None:
        print("Warning: No data provided")
    
    # TODO: Improve error handling for invalid inputs
    try:
        return data.strip().lower()
    except AttributeError:
        return "Invalid data"

# TODO: Optimize this function for large datasets
def inefficient_loop(data_list):
    for item in data_list:
        print(item)

process_data(None)
inefficient_loop(["Item1", "Item2"])
