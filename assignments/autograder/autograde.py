from grader import autograde, commit_and_push
from glob import glob
import typer

app = typer.Typer()

@app.command()
def run(path: str, summarize: bool=False, commit: bool=False, push: bool=False, root=None, grader=None, public=None, private=None):
    grades = autograde(path, plot_it=summarize, root=root, grading_repo=grader, public_checks_dir=public, private_checks_dir=private)
    
    if commit:
        commit_and_push(path, grades.index.to_list(), debug=(not push))

if __name__ == "__main__":
    app()