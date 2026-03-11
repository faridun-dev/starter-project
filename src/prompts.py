import questionary


def ask_questions():
    name = questionary.text("Project name:").ask()

    template = questionary.select(
        "Choose template:",
        choices=["FastAPI", "Aiogram"],
    ).ask()

    git = questionary.confirm("Initialize git?").ask()

    return {"name": name, "template": template, "git": git}
