import sys
import typer

from .helpers import (
    get_diff_output,
    load_config,
    get_prompt,
    get_llm_response,
    validate_llm_response,
    finalize_commit,
)
from .tui import EditableTextApp

typer_app = typer.Typer()


@typer_app.command()
def main():
    ###### Git diff ######
    diff_output = get_diff_output()

    if not diff_output.strip():
        print("No changes to commit. Stage your changes with 'git add' first.")
        sys.exit(0)
        
    ###### Ollama ######
    config = load_config()
    MODEL_NAME = config["model_name"]
    prompt = get_prompt(diff_output)

    llm_response_str = get_llm_response(MODEL_NAME, prompt)
    llm_commit_message = validate_llm_response(llm_response_str)

    ###### TUI ######
    app = EditableTextApp(llm_commit_message.format())
    final_message = app.run()

    if final_message is None:
        print("Commit cancelled.")
        sys.exit(0)

    ###### Git Commit ######
    finalize_commit(final_message)


if __name__ == "__main__":
    typer_app()
