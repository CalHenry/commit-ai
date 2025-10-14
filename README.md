# AI agent to push better commit messages


- local LLM
- small LLM
- easy to acces with a CLI
- only for writting/ rewritting commit messages

I develop this for myself.
- I code in python for Data science and i have 'simple' repo to manage, usually a single branch and only a set of scripts.


#### LLM context from the Git repo:
- git diff (list of staged files + staged changes)
- previous commit
- potential pre-wrote (by me) commit message

##### LLM action:
- model loaded
- process the prompt with:
  - default prompt(s) to write a commit
  - context from the repo
- write a commit message
- show the commit message for my validation
- if i accept, commit the changes
