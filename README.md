# CS50P – Problem Set 5: Unit Tests

My solutions to **Problem Set 5** of [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python).

This problem set focuses on **writing tests** for previously implemented programs using `pytest`. Each problem reimplements a past solution with a testable structure and a corresponding test file.

---

## Running Tests

```bash
pip install pytest
python -m pytest test_twttr.py
python -m pytest test_bank.py
python -m pytest test_plates.py
python -m pytest test_fuel.py
```

---

## Problems

### 1. 🐦 Testing my twttr — `twttr.py` + `test_twttr.py`
**Problem:** [cs50.harvard.edu/python/psets/5/test_twttr](https://cs50.harvard.edu/python/psets/5/test_twttr/)

Reimplements `twttr.py` with a `shorten(word)` function that removes all vowels from a string. `test_twttr.py` tests it thoroughly.

**Tests cover:**
- All lowercase vowels removed
- All uppercase vowels removed
- Strings with no vowels (unchanged)
- Mixed case strings
- Empty string

**Run:**
```bash
python -m pytest test_twttr.py
```
**Example output:**
```
5 passed in 0.02s
```

---

### 2. 🏦 Back to the Bank — `bank.py` + `test_bank.py`
**Problem:** [cs50.harvard.edu/python/psets/5/test_bank](https://cs50.harvard.edu/python/psets/5/test_bank/)

Reimplements `bank.py` with a `value(greeting)` function. `test_bank.py` tests all greeting cases.

**Tests cover:**
- Lowercase `"hello"` → `$0`
- Lowercase `"h"` (not hello) → `$20`
- Other greetings → `$100`
- Uppercase versions of all above
- Mixed case versions
- Empty string

**Run:**
```bash
python -m pytest test_bank.py
```
**Example output:**
```
8 passed in 0.02s
```

---

### 3. 🚗 Re-requesting a Vanity Plate — `plates.py` + `test_plates.py`
**Problem:** [cs50.harvard.edu/python/psets/5/test_plates](https://cs50.harvard.edu/python/psets/5/test_plates/)

Reimplements `plates.py` with an `is_valid(s)` function. `test_plates.py` tests all validation rules.

**Tests cover:**
- Valid plate with no digits
- Valid plate with digits at end
- Invalid — digits in middle with letters after
- Invalid — first digit is `0`
- Invalid — too short (< 2 chars)
- Invalid — too long (> 6 chars)
- Invalid — special characters
- Invalid — doesn't start with two letters

**Run:**
```bash
python -m pytest test_plates.py
```
**Example output:**
```
8 passed in 0.02s
```

---

### 4. ⛽ Refueling — `fuel.py` + `test_fuel.py`
**Problem:** [cs50.harvard.edu/python/psets/5/test_fuel](https://cs50.harvard.edu/python/psets/5/test_fuel/)

Reimplements `fuel.py` with `convert(frac)` and `gauge(percent)` functions. `test_fuel.py` tests both functions including exception handling.

**Tests cover:**
- `ValueError` for negative numerator/denominator
- `ZeroDivisionError` for zero denominator
- `ValueError` for float inputs
- `ValueError` when numerator > denominator
- Correct percentage conversion
- `gauge()` returning `"E"` at or below 1%
- `gauge()` returning `"F"` at or above 99%
- `gauge()` returning percentage string otherwise

**Run:**
```bash
python -m pytest test_fuel.py
```
**Example output:**
```
6 passed in 0.02s
```

---

## What I Learned
- Writing unit tests with `pytest`
- `assert` statements for expected values
- `pytest.raises()` for testing exceptions — `ValueError`, `ZeroDivisionError`
- Structuring code with `if __name__ == "__main__"` to make it importable
- Test naming conventions — all test functions start with `test_`
- Thinking about edge cases — empty input, boundary values, invalid types
- Running tests with `python -m pytest`

---

## Course
**CS50's Introduction to Programming with Python**
Harvard University — [cs50.harvard.edu/python](https://cs50.harvard.edu/python)
