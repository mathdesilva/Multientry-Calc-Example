import typer
from multicalc.core.calculator import Calculator

app = typer.Typer()
calc = Calculator()

@app.command()
def add(a: float, b: float):
    """Add two numbers."""
    typer.echo(calc.add(a, b))

@app.command()
def subtract(a: float, b: float):
    """Subtract b from a."""
    typer.echo(calc.subtract(a, b))

@app.command()
def multiply(a: float, b: float):
    """Multiply two numbers."""
    typer.echo(calc.multiply(a, b))

@app.command()
def divide(a: float, b: float):
    """Divide a by b."""
    try:
        typer.echo(calc.divide(a, b))
    except ZeroDivisionError as e:
        typer.echo(f"Error: {e}")

@app.command()
def power(a: float, b: float):
    """Raise a to the power of b."""
    typer.echo(calc.power(a, b))

if __name__ == "__main__":
    app()
