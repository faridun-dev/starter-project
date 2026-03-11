import typer
from src.prompts import ask_questions
from src.generator import create_project

app = typer.Typer()


@app.command()
def create():
    answers = ask_questions()
    create_project(answers)
