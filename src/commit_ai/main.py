import sys
import typer

from .helpers import (
    get_diff_output,
    load_config,
    get_llm_response,
    parse_llm_response,
    finalize_commit,
)
from .tui import EditableTextApp

typer_app = typer.Typer()


@typer_app.command()
def main():
    ###### Git diff ######

    diff_output = get_diff_output()

    ###### Ollama ######

    config = load_config()
    MODEL_NAME = config["model_name"]

    prompt = f"""
    Write a **clear, concise, and structured** Git commit message for the following changes.
    Follow these **strict guidelines**:
    - **Subject**: 50 chars max, imperative mood  ("Add" not "Added"), capitalize first word, no period.
    - **Types**: Use one or more of these prefixes: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`. For multiple types, combine with & (e.g., feat & fix).
    - **Body**: Explain *what* and *why* (not *how*), wrap at 72 chars.

    **Template:**
        <type>: <subject>

        <body>


    Always include a body unless the change is trivial (e.g., typo fix).
    For complex changes, use bullet points to separate logical units.
    Respond in JSON format with a key for type, subject and body

    git diff output:
    {diff_output}
    """

    llm_response = get_llm_response(MODEL_NAME, prompt)
    llm_response = str(llm_response["response"])

    llm_commit_message = parse_llm_response(llm_response)

    ###### TUI ######
    app = EditableTextApp(llm_commit_message)
    final_message = app.run()

    if final_message is None:
        print("Commit cancelled.")
        sys.exit(0)

    ###### Git Commit ######
    finalize_commit(final_message)


if __name__ == "__main__":
    typer_app()
