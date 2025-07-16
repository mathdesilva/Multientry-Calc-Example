# multicalc/api.py

from fastapi import FastAPI, Query
from multicalc.core.calculator import Calculator

app = FastAPI(
    title="MultiCalc Example API",
    description="A demo REST API for the modular calculator example.",
)

calc = Calculator()

@app.get("/")
def root():
    return {"message": "Welcome to MultiCalc API!"}

@app.get("/add")
def add(a: float = Query(...), b: float = Query(...)):
    """Add two numbers."""
    return {"result": calc.add(a, b)}

@app.get("/subtract")
def subtract(a: float = Query(...), b: float = Query(...)):
    """Subtract b from a."""
    return {"result": calc.subtract(a, b)}

@app.get("/multiply")
def multiply(a: float = Query(...), b: float = Query(...)):
    """Multiply two numbers."""
    return {"result": calc.multiply(a, b)}

@app.get("/divide")
def divide(a: float = Query(...), b: float = Query(...)):
    """Divide a by b."""
    try:
        result = calc.divide(a, b)
        return {"result": result}
    except ZeroDivisionError as e:
        return {"error": str(e)}

@app.get("/power")
def power(a: float = Query(...), b: float = Query(...)):
    """Raise a to the power of b."""
    return {"result": calc.power(a, b)}


def start():
    import uvicorn
    uvicorn.run("multicalc.api:app", host="127.0.0.1", port=8000, reload=True)
