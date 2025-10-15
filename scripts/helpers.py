import subprocess
import ollama


###### Git utils ######
def get_diff_output() -> str:
    return subprocess.check_output(["git", "diff"], text=True)


###### Ollama utils ######
def get_llm_response(model: str, prompt: str):
    return ollama.generate(
        model,
        prompt,
        system="you write top level git commit messages",
        # template="{{ .System }}\n\n{{ .Prompt }}",
        options={"num_ctx": 16000},
        format="json",
        stream=False,
    )
