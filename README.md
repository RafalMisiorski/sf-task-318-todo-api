# Python Module

Simple Python module workspace.

## Structure
- Root: Your Python modules/scripts
- tests/: Test files (test_*.py)

## Running Tests
```bash
pytest tests/ -v
```

## Adding Tests
Create files named `test_*.py` in the tests/ directory.

Example:
```python
# tests/test_mymodule.py
from mymodule import my_function

def test_my_function():
    assert my_function(1, 2) == 3
```