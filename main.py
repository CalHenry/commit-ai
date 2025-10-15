import os
from scripts.helpers import get_diff_output, get_llm_response
from scripts.tui import EditableTextApp

###### Git ######
diff_output = get_diff_output()
# print(diff_output)

fake_repo_path = "./fake_repo"
os.chdir(fake_repo_path)

###### Ollama ######
model = "qwen2.5:3b"

prompt = f"""
rewrite the git commit message

{diff_output}
"""

llm_response = get_llm_response(model, prompt)


###### TUI ######
if __name__ == "__main__":
    app = EditableTextApp(llm_response)
    app.run()
