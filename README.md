# AI agent to push better commit messages

## Learning (DevObs)
- create a tool that uses ai as a small helper
- create a TUI  with **Textual** and a CLI with **Typer**
- build a python package that can be used in the command line
- learn more about **setuptools** and **pyproject**

## Goals
- create a usefull agent
- get better with git
- develop a local solution, no LLM bills, no data sent to a server

- local LLM
- small LLM
- easy to acces with a CLI
- only for writting/ rewritting commit messages

I develop this for myself.
- I code in python for Data science and i have 'simple' repo to manage, usually a single branch and only a set of scripts.


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



### Nexct steps
- [X] better prompt
- model name to .env
- get commit message as well
- better looking app (add buttom)
