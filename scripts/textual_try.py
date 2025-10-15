from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.containers import Vertical, Horizontal

class CommitMessageApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #message {
        width: 60;
        height: auto;
        border: round white;
        padding: 1;
    }
    Button {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static("AI-Generated Commit Message:", id="title"),
            Static(
                "Fix bug in user authentication flow\n\n- Add input validation for email field\n- Improve error handling for invalid credentials",
                id="message",
            ),
            Horizontal(
                Button("Accept", id="accept"),
                Button("Reject", id="reject"),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "accept":
            self.notify("✅ Commit message accepted!", title="Success", timeout=3)
        elif event.button.id == "reject":
            self.notify("❌ Commit message rejected.", title="Rejected", timeout=3)
        self.exit()

if __name__ == "__main__":
    app = CommitMessageApp()
    app.run()
