import subprocess
import ollama
import json
from pathlib import Path
from .models import CommitMessage


###### Git utils ######
def get_diff_output() -> str:
    return subprocess.check_output(["git", "diff"], text=True)


def finalize_commit(commit_message):
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        # Commit with message from the app
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Commit's done!")
    except subprocess.CalledProcessError as e:
        print(f"Error finalizing commit: {e}")


###### Ollama utils ######
def load_config():
    package_dir = Path(__file__).parent
    config_path = package_dir / "config.json"

    with open(config_path, "r") as f:
        return json.load(f)


def get_prompt(diff_output):
    schema = CommitMessage.model_json_schema()

    prompt = f"""
    Write a **clear, concise, and structured** Git commit message for the following changes.
    Follow these **strict guidelines**:
    - **Subject**: 50 chars max, imperative mood  ("Add" not "Added"), capitalize first word, no period.
    - **Types**: Use one or more of these prefixes: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`. For multiple types, combine with & (e.g., feat & fix).
    - **Body**: Explain *what* and *why* (not *how*), wrap at 72 chars.

    Always include a body unless the change is trivial (e.g., typo fix).
    For complex changes, use bullet points to separate logical units.

    Respond with valid JSON matching this exact schema:
    {json.dumps(schema, indent=2)}

    git diff output:
    {diff_output}
    """

    return prompt


def get_llm_response(model: str, prompt: str):
    llm_response = ollama.generate(
        model,
        prompt,
        system="you write top level git commit messages",
        # template="{{ .System }}\n\n{{ .Prompt }}",
        options={"num_ctx": 16000},
        format="json",
        stream=False,
        keep_alive=1,
    )
    return llm_response["response"]


def validate_llm_response(llm_response_json):
    llm_commit_message = json.loads(llm_response_json)

    return CommitMessage(**llm_commit_message)
