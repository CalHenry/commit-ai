# AI agent to write better commit messages

> ! DISCLAIMER
> First version of the project. It works but i have to add tests, robust paths and more.

AI commit messages writer from a single command line.

Use a local LLM to do a first version of the commit message. Editable and discardable.

How it works:
1. gather informations about the changes (git diff)
2. provide this information to a local llm (runs with ollama)
3. AI creates a commit message
4. Message is displayed in a TUI and is editable
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

- To contribute or modify:
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

--------------------------------------------------------

## Learning (DevObs)
- create a tool that uses ai as a small helper
- create a TUI  with **Textual** and a CLI with **Typer**
- build a python package that can be used in the command line
- learn more about **setuptools** and **pyproject**


#### LLM context from the Git repo:
- git diff's output (list of staged files + staged changes)
- previous commit
- potential pre-wrote (by me) commit message

### LLM action:
- model loaded
- process the prompt with:
  - default prompt(s) to write a commit
  - context from the repo
- write a commit message
- show the commit message for my validation
- if i accept, commit the changes

### workflow

- get git diff content to a var
```python
  subprocess.check_output(["git", "diff"], text=True)
```
- **!TODO** get commit message (with git hook)
- get llm response
```python
    ollama.generate(model, prompt, ...)
```
