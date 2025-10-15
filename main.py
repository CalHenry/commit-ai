import os
from scripts.helpers import get_diff_output, get_llm_response
from scripts.tui import EditableTextApp
from test_commits import long_gitdiff, complex_gitdiff, mixed_gitdiff, ml_gitdiff

# Test different kind of git diffs:
long_gitdiff = long_gitdiff
complex_gitdiff = complex_gitdiff
mixed_gitdiff = mixed_gitdiff
ml_gitdiff = ml_gitdiff


def main():
    ###### Git ######

    fake_repo_path = "./fake_repo"
    os.chdir(fake_repo_path)

    diff_output = get_diff_output()

    ###### Ollama ######
    model = "qwen2.5:7b"

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

    git diff output:
    {diff_output}
    """

    llm_response = get_llm_response(model, prompt)
    llm_response = str(llm_response["response"])

    print(llm_response)

    ###### TUI ######
    # app = EditableTextApp(llm_response)
    # app.run()


if __name__ == "__main__":
    main()
