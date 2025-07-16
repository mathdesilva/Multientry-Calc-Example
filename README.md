
# Multientry-Calc-Example

An example project of modular Python architecture, featuring a reusable core and multiple entry points: CLI, REST API, and import. This is a demonstration project for learning and testing purposes.

## Installation

Install the core library:

```bash
pip install .
```

Install with CLI support:

```bash
pip install .[cli]
```

Install with REST API support:

```bash
pip install .[api]
```

## Usage via CLI

After installing with `[cli]`, run:

```bash
multicalc add 2 3
multicalc subtract 5 2
multicalc multiply 4 6
multicalc divide 8 2
```

## Usage via REST API

After installing with `[api]`, start the server:

```bash
multicalc-serve
```

Access Swagger docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

Example endpoints:

- `GET /add?x=2&y=3`
- `GET /subtract?x=5&y=2`
- `GET /multiply?x=4&y=6`
- `GET /divide?x=8&y=2`

## Usage as a Library (Import)

Import and use the core calculator in Python:

```python
from multicalc import Calculator

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.subtract(5, 2))   # 3
print(calc.multiply(4, 6))   # 24
print(calc.divide(8, 2))     # 4.0
```

---
This project is for demonstration and educational purposes only.

