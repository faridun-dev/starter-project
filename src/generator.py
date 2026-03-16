import shutil
import subprocess
from pathlib import Path


def create_project(config):
    template = config["template"].lower().replace(" ", "_")
    project_name = config["name"]

    src = Path("templates") / template
    dst = Path(project_name)

    shutil.copytree(src, dst)

    print(f"Project '{project_name}' created!")

    if config["git"]:
        command = f"cd {project_name} & git init"
        subprocess.run(command, shell=True)
