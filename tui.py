from textual.app import App, ComposeResult
from textual.widgets import TextArea, Static, Footer
from textual.containers import Container


class EditableTextApp(App):
    # CSS_PATH = "scripts/tui_css.tcss" # can't manage to make the file readable so i keep the css below
    CSS = """
    Screen {
        background: transparent;
    }
    #title_container {
        height: 3;
        background: transparent;
        border: round $primary;
        padding: 0 1;
        margin-top: 1;
        margin-left: 5;
        margin-right: 5;
    }
    #title {
        width: 100%;
        content-align: center middle;
        text-style: bold;
        color: $text;
    }
    #text_container {
        height: 1fr;
        margin-top: 1;
        margin-left: 5;
        margin-right: 5;
        margin-bottom: 1;
        background: transparent;
        border: round $primary;
        padding: 1 2;
    }
    TextArea {
        background: transparent;
        border: none;
        padding: 0;
    }
    TextArea:focus {
        border: none;
    }
    TextArea .text-area--cursor {
        background: $secondary;
    }
    Footer {
        height: 1;
    }
    """

    BINDINGS = [
        ("escape", "app.quit", "Quit"),
        ("ctrl+s", "accept", "Accept"),
    ]

    def __init__(self, llm_response: str):
        super().__init__()
        self.my_text = llm_response

    def compose(self) -> ComposeResult:
        with Container(id="title_container"):
            yield Static("COMMIT MESSAGE EDITOR", id="title")
        with Container(id="text_container"):
            yield TextArea(self.my_text, id="text_area")
        yield Footer(show_command_palette=False)

    def on_mount(self) -> None:
        self.theme = "nord"
        text_area = self.query_one("#text_area", TextArea)
        text_area.focus()

    def action_accept(self) -> None:
        self.exit(result=self.query_one("#text_area", TextArea).text)


if __name__ == "__main__":
    app = EditableTextApp("default text")
    result = app.run()
    print("Accepted commit message:", result)
