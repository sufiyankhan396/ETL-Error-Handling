
---

## Error Handling Examples

### 1. Simple Try-Except

**File:** `error_handling_examples/simple_try_except.py`

```python
def divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero! Details: {e}")
    except Exception as e:
        print(f"Unexpected error occurred! Details: {e}")

# Test cases
divide(10, 2)
divide(5, 0)
