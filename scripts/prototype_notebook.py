import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import subprocess
    import ollama
    import os
    return ollama, os, subprocess


@app.cell
def _(os):
    fake_repo_path = "./fake_repo"
    os.chdir(fake_repo_path)
    return


@app.cell
def _(subprocess):
    diff_output = subprocess.check_output(["git", "diff"], text=True)

    print(diff_output)
    return (diff_output,)


@app.cell
def _(diff_output):
    # ollama part
    prompt = f"""
    rewrite the git commit message

    {diff_output}
    """

    print(prompt)
    return (prompt,)


@app.cell
def _(ollama, prompt):
    llm_response = ollama.generate(model="qwen2.5:3b", prompt=prompt, stream=False)

    print(f"reponse: {llm_response}")
    return


@app.cell
def _():
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich.markdown import Markdown
    from rich.text import Text

    console = Console()

    # Simulated AI-generated commit message
    ai_commit = {
        "title": "feat: Add user authentication with JWT tokens",
        "body": """- Implement JWT-based authentication system
    - Add login and registration endpoints
    - Create middleware for token verification
    - Add password hashing with bcrypt
    - Include refresh token mechanism"""
    }

    def display_commit_message():
        """Display the AI-generated commit message in a nice panel"""
    
        # Create the commit message content
        content = Text()
        content.append("✨ AI-Generated Commit Message\n\n", style="bold blue")
        content.append("Title:\n", style="bold cyan")
        content.append(f"{ai_commit['title']}\n\n", style="green")
        content.append("Description:\n", style="bold cyan")
        content.append(ai_commit['body'], style="white")
    
        # Display in a panel
        panel = Panel(
            content,
            border_style="blue",
            padding=(1, 2)
        )
    
        console.print(panel)

    def main():
        console.clear()
    
        # Display the commit message
        display_commit_message()
    
        console.print()
    
        # Prompt for user action
        while True:
            choice = Prompt.ask(
                "[bold yellow]Accept this commit message?[/bold yellow]",
                choices=["y", "n", "e"],
                default="y"
            )
        
            if choice == "y":
                console.print("✓ [bold green]Commit message accepted![/bold green]")
                console.print("[dim]Committing changes...[/dim]")
                break
            elif choice == "n":
                console.print("✗ [bold red]Commit message rejected.[/bold red]")
                console.print("[dim]Generating new message...[/dim]")
                break
            elif choice == "e":
                console.print("[bold cyan]Opening editor...[/bold cyan]")
                break

    if __name__ == "__main__":
        main()
    return


if __name__ == "__main__":
    app.run()
