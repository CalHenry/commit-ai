import subprocess
import ollama
import json
from pathlib import Path


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


def get_llm_response(model: str, prompt: str):
    return ollama.generate(
        model,
        prompt,
        system="you write top level git commit messages",
        # template="{{ .System }}\n\n{{ .Prompt }}",
        options={"num_ctx": 16000},
        format="json",
        stream=False,
        keep_alive=1,
    )


def parse_llm_response(llm_response_json):
    llm_commit_message = json.loads(llm_response_json)

    return llm_commit_message
