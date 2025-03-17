def read_file(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError as e:
        print(f"Error: File not found! Details: {e}")
    except Exception as e:
        print(f"Unexpected error! Details: {e}")
    finally:
        print("Closing file (if it was opened)...")
        try:
            file.close()
        except:
            pass

# Test cases
read_file("existing_file.txt")  # Replace with a real file if testing
read_file("non_existing_file.txt")
