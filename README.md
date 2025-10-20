# AI agent to write better commit messages
----

AI commit messages writer from a single command line.

Use a LLM that runs locally to do a first draft of the git commit message. Editable or discardable.

How it works:
1. gather informations about the changes (git diff)
2. pass this information to the llm (runs with ollama)
3. AI creates a commit message
4. message is validated by Pydantic
5. message is displayed in a TUI and is editable
  - **ctrl-s** to accept --> do the commit
  - **escape** --> do nothing and quit

## Installation

1. Install [**uv**](https://docs.astral.sh/uv/)

Unix:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Windows:
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install as a tool using uv
```sh
uv tool install git+https://github.com/CalHenry/commit-ai.git
```

3. Check the Installation
```which commit-ai```

4. Usage
```sh
commit-ai
```

5. (Optional) create an alias for the tool
```sh
echo '' >> ~/.zshrc
echo '# Alias for commit-ai tool' >> ~/.zshrc
echo 'alias cai="commit-ai"' >> ~/.zshrc
source ~/.zshrc
```

If you just want to run the tool and not install it use:
```sh
uvx git+https://github.com/CalHenry/commit-ai.git
```
(this will launch the tool, get the git diff of the current directory and run the llm)

### Contribute or modify:
```sh
# Clone the repo
git clone https://github.com/yourusername/commit-ai.git
cd commit-ai

# Or install as a tool in development mode
uv tool install -e .

# ready
which commit-ai
```

## Requirements
- machine that has a gpu (or ARM) to run a small llm
- Ollama installed

## More informations

- The app is build with Typer
- Pydantic gives the response schema and validates the output
- You can use any model as long as it supports JSON output. Each model is different, you should try to find one that fits you best
- Default model is [Granite-4.0-H-Tiny](https://huggingface.co/ibm-granite/granite-4.0-h-tiny) (4.2 GB)

## 🛡️ License <a name="license"></a>
Project is distributed under [MIT License](https://github.com/CalHenry/commit-ai/blob/main/LICENSE)

--------------------------------------------------------
