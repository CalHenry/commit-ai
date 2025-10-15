import subprocess
import ollama


###### Git utils ######
def get_diff_output():
    return subprocess.check_output(["git", "diff"], text=True)


###### Ollama utils ######
def get_llm_response(model: str, prompt: str):
    return ollama.generate(model, prompt, stream=False)
