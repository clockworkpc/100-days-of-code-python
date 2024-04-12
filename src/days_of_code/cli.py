"""Console script for days_of_code."""
import days_of_code

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for days_of_code."""
    console.print("Replace this message by putting your code into "
               "days_of_code.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
