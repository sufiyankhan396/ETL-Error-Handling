class DataValidationError(Exception):
    """Custom exception for data validation errors."""
    pass

def process_data(data):
    try:
        if not isinstance(data, list):
            raise DataValidationError("Data must be a list.")
        
        if len(data) == 0:
            raise DataValidationError("Data list is empty.")

        # Simulate processing
        print("Processing data...")
    
    except DataValidationError as e:
        print(f"Data validation error: {e}")
    
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Test cases
process_data("string_instead_of_list")
process_data([])
process_data([1, 2, 3])
